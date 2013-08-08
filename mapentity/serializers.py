# -*- coding: utf-8 -*-
import csv
import math
from HTMLParser import HTMLParser
from functools import partial
from collections import OrderedDict

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str
from django.utils.html import strip_tags
from django.db.models.fields.related import ForeignKey, ManyToManyField, FieldDoesNotExist
from django.core.serializers.base import Serializer
from django.contrib.gis.geos import Point, LineString, MultiPoint, MultiLineString
from django.contrib.gis.geos.collections import GeometryCollection
from django.contrib.gis.db.models.fields import (GeometryField, GeometryCollectionField,
                                                 PointField, LineStringField,
                                                 MultiPointField, MultiLineStringField)

import gpxpy

from .templatetags.timesince import humanize_timesince
from . import shape_exporter


def plain_text(html):
    h = HTMLParser()
    return h.unescape(strip_tags(html))


def smart_plain_text(s, ascii=False):
    if s is None:
        return ''
    try:
        # Converts to unicode, remove HTML tags, convert HTML entities
        us = plain_text(unicode(s))
        if ascii:
            return smart_str(us)
        return us
    except UnicodeDecodeError:
        return smart_str(s)


def field_as_string(obj, field, ascii=False):
    value = getattr(obj, field + '_csv_display', None)
    if value is None:
        value = getattr(obj, field + '_display', None)
        if value is None:
            value = getattr(obj, field)
    if hasattr(value, '__iter__'):
        return ','.join([smart_plain_text(item, ascii) for item in value])
    return smart_plain_text(value, ascii)


class DatatablesSerializer(Serializer):
    def serialize(self, queryset, **options):
        model = options.pop('model', None) or queryset.model
        columns = options.pop('fields')

        attr_getters = {}
        for field in columns:
            if hasattr(model, field + '_display'):
                attr_getters[field] = lambda obj, field: getattr(obj, field + '_display')
            else:
                modelfield = model._meta.get_field(field)
                if isinstance(modelfield, ForeignKey):
                    attr_getters[field] = lambda obj, field: unicode(getattr(obj, field) or _("None"))
                elif isinstance(modelfield, ManyToManyField):
                    attr_getters[field] = lambda obj, field: [unicode(o) for o in getattr(obj, field).all()] or _("None")
                else:
                    def fixfloat(obj, field):
                        value = getattr(obj, field)
                        if isinstance(value, float) and math.isnan(value):
                            value = 0.0
                        return value
                    attr_getters[field] = fixfloat
        # Build list with fields
        map_obj_pk = []
        data_table_rows = []
        for obj in queryset:
            row = [attr_getters[field](obj, field) for field in columns]
            data_table_rows.append(row)
            map_obj_pk.append(obj.pk)

        return {
            # aaData is the key looked up by dataTables
            'aaData': data_table_rows,
            'map_obj_pk': map_obj_pk,
        }


class CSVSerializer(Serializer):
    def serialize(self, queryset, **options):
        """
        Uses self.columns, containing fieldnames to produce the CSV.
        The header of the csv is made of the verbose name of each field
        Each column content is made using (by priority order):
            * <field_name>_csv_display
            * <field_name>_display
            * <field_name>
        """
        model = options.pop('model', None) or queryset.model
        columns = options.pop('fields')
        stream = options.pop('stream')
        ascii = options.get('ensure_ascii', True)

        headers = []
        for field in columns:
            c = getattr(model, '%s_verbose_name' % field, None)
            if c is None:
                try:
                    c = model._meta.get_field(field).verbose_name
                except FieldDoesNotExist:
                    c = _(field.title())
            headers.append(smart_str(unicode(c)))

        attr_getters = {}
        for field in columns:
            try:
                modelfield = model._meta.get_field(field)
            except FieldDoesNotExist:
                modelfield = None
            if isinstance(modelfield, ForeignKey):
                attr_getters[field] = lambda obj, field: smart_plain_text(getattr(obj, field), ascii)
            elif isinstance(modelfield, ManyToManyField):
                attr_getters[field] = lambda obj, field: ','.join([smart_plain_text(o, ascii) for o in getattr(obj, field).all()] or '')
            else:
                attr_getters[field] = partial(field_as_string, ascii=ascii)

        def get_lines():
            yield headers
            for obj in queryset:
                yield [attr_getters[field](obj, field) for field in columns]
        writer = csv.writer(stream)
        writer.writerows(get_lines())


class GPXSerializer(Serializer):
    """
    GPX serializer class. Very rough implementation, but better than inline code.
    """
    # TODO : this should definitely respect Serializer abstraction :
    # LineString -> Route with Point
    # Collection -> One route/waypoint per item
    def __init__(self, *args, **kwargs):
        self.gpx = None

    def serialize(self, queryset, **options):
        self.gpx = gpxpy.gpx.GPX()

        stream = options.pop('stream')
        geom_field = options.pop('geom_field')

        for obj in queryset:
            geom = getattr(obj, geom_field)
            objtype = unicode(obj.__class__._meta.verbose_name)
            name = '[%s] %s' % (objtype, unicode(obj))

            description = ''
            objupdate = getattr(obj, 'date_update')
            if objupdate:
                description = _('Modified') + ': ' + humanize_timesince(objupdate)
            if geom:
                assert geom.srid == settings.SRID, "Invalid srid"
                self.geomToGPX(geom, name, description)
        stream.write(self.gpx.to_xml())

    def _point_to_GPX(self, point, klass=gpxpy.gpx.GPXWaypoint):
        if isinstance(point, (tuple, list)):
            point = Point(*point, srid=settings.SRID)
        newpoint = point.transform(4326, clone=True)  # transformation: gps uses 4326
        # transform looses the Z parameter
        return klass(latitude=newpoint.y, longitude=newpoint.x, elevation=point.z)

    def geomToGPX(self, geom, name, description):
        """Convert a geometry to a gpx entity.
        Raise ValueError if it is not a Point, LineString or a collection of those

        Point -> add as a Way Point
        LineString -> add all Points in a Route
        Collection (of LineString or Point) -> add as a route, concatening all points
        """
        if isinstance(geom, GeometryCollection):
            for i, g in enumerate(geom):
                self.geomToGPX(g, u"%s (%s)" % (name, i), description)
        elif isinstance(geom, Point):
            wp = self._point_to_GPX(geom)
            wp.name = name
            wp.description = description
            self.gpx.waypoints.append(wp)
        elif isinstance(geom, LineString):
            gpx_route = gpxpy.gpx.GPXRoute(name=name, description=description)
            gpx_route.points = [self._point_to_GPX(point, klass=gpxpy.gpx.GPXRoutePoint) for point in geom]
            self.gpx.routes.append(gpx_route)
        else:
            raise ValueError("Unsupported geometry %s" % geom)


class ZipShapeSerializer(Serializer):
    def __init__(self, *args, **kwargs):
        super(ZipShapeSerializer, self).__init__(*args, **kwargs)
        self.layers = OrderedDict()

    def start_object(self, *args, **kwargs):
        pass

    def serialize(self, queryset, **options):
        columns = options.pop('fields')
        stream = options.pop('stream')
        model = options.pop('model', None) or queryset.model
        delete = options.pop('delete', True)
        # Zip all shapefiles created temporarily
        self._create_shape(queryset, model, columns)
        layers = [(k, v) for k, v in self.layers.items()]
        stream.write(shape_exporter.zip_shapefiles(layers, delete=delete))

    def _create_shape(self, queryset,  model, columns):
        """Split a shapes into one or more shapes (one for point and one for linestring)
        """
        geo_field = shape_exporter.geo_field_from_model(model, 'geom')
        get_geom, geom_type, srid = shape_exporter.info_from_geo_field(geo_field)

        if geom_type.upper() in (GeometryField.geom_type, GeometryCollectionField.geom_type):

            by_points, by_linestrings, multipoints, multilinestrings = self.split_bygeom(queryset, geom_getter=get_geom)

            for split_qs, split_geom_field in ((by_points, PointField),
                                               (by_linestrings, LineStringField),
                                               (multipoints, MultiPointField),
                                               (multilinestrings, MultiLineStringField)):
                if len(split_qs) == 0:
                    continue
                split_geom_type = split_geom_field.geom_type
                shp_filepath = shape_exporter.shape_write(split_qs, model, columns, get_geom, split_geom_type, srid)
                self.layers['shp_download_%s' % split_geom_type.lower()] = shp_filepath

        else:
            shp_filepath = shape_exporter.shape_write(queryset, model, columns, get_geom, geom_type, srid)
            self.layers['shp_download'] = shp_filepath

    def split_bygeom(self, iterable, geom_getter=lambda x: x.geom):
        """Split an iterable in two list (points, linestring)"""
        points, linestrings, multipoints, multilinestrings = [], [], [], []

        for x in iterable:
            geom = geom_getter(x)
            if geom is None:
                pass
            elif isinstance(geom, GeometryCollection):
                # Duplicate object, shapefile do not support geometry collections !
                subpoints, sublines, pp, ll = self.split_bygeom(geom, geom_getter=lambda geom: geom)
                if subpoints:
                    clone = x.__class__.objects.get(pk=x.pk)
                    clone.geom = MultiPoint(subpoints, srid=geom.srid)
                    multipoints.append(clone)
                if sublines:
                    clone = x.__class__.objects.get(pk=x.pk)
                    clone.geom = MultiLineString(sublines, srid=geom.srid)
                    multilinestrings.append(clone)
            elif isinstance(geom, Point):
                points.append(x)
            elif isinstance(geom, LineString):
                linestrings.append(x)
            else:
                raise ValueError("Only LineString and Point geom should be here. Got %s for pk %d" % (geom, x.pk))
        return points, linestrings, multipoints, multilinestrings