=========
CHANGELOG
=========

0.24 (unreleased)
-----------------

**New features**

* Public TREK export - hide block label if value is empty (fixes #873)
* Detail page : replace "Maintenance" by "Works" (fixes #889)
* Detail page : interventions on paths are now grouped together,
  and a small icon is shown (fixes #735)
* Detail page : show intervention costs (ref #958, fixes #764)
* Show project intervention total costs (fixes #958)
* Add POIs on trek GPX (fixes #774)
* Allow to override the Trek public document template
  (see *advanced configuration* in docs)
* Close list filter when click outside (fixes #916)
* Intervention disorders is not mandatory anymore (fixes #661)
* Rename recurrent field to subcontracting on intervention (fixes #911)
* Rename comments field to description on intervention (fixes #927)
* Show object type in ODT export (fixes #1000)
* Show POI name on hover instead of category in trek detail pages (fixes #1004)
* Show paths extremities on map (fixes #355)
* Close calendar after date choice in intervention form (fixes #928)
* Renamed Attachment submit button (fixes #925)
* Added a new setting ``PATH_SNAPPING_DISTANCE`` to control paths snapping distance
  in database (default: 1m)
* Allow to disable trails notion (fixes #997)
  (see *advanced configuration* in docs)
* Ability to reuse topology when adding objects from detail pages (fixes #574, fixes #998)
* Form tabs are now always visible while scrolling (fixes #926)
* Command to generate all elevation charts (fixes #799)
* SITRA support in Tourism datasources (fixes #1064)
* Added status field on feedback reports (fixes #1075)
* Documented the configuration of map layers apparence
* Show restricted areas by type in layer switcher (fixes #961)
* Show layers colors in layer switcher
* Publication status is now controlled by language (fixes #1003). Previous
  behaviour can restored by setting ``TREK_PUBLISHED_BY_LANG``` to False.
* Added publication date on trek (ref #1003)
* Ability to see a trek in the different published languages (ref #1003)
* A trek can now have several information desks (fixes #1001)
* Information desks are now shown in trek detail map (fixes #1001)
* Information desks now have optional photo and position, as well as some additional fields (fixes #1001)

**Bug fixes**

* Fixed Signage and Infrastructure year filter label (fixes #293)
* Fixed paths layers not always shown below other layers (fixes #912)
* Clarify legend and title for attachments (fixes #888)
* Fixed cannot clear trek fields in database (fixes #1095)
* Fixed missing translation of "Load local file" (fixes #1085)
* POI types are displayed as such in adminsite

**Internal changes**

* Added pictogram on difficulty, useful for *Geotrek-mobile* (fixes #1109)



0.23.5 (2014-06-19)
-------------------

**Bug fixes**

* Fix crash when TourInFrance has malformed website or phone
* Fix translations not being installed


0.23.4 (2014-06-18)
-------------------

**Bug fixes**

* Fix massive upgrade bug, where new migrations were ignored. Due to migration
  operation introduction in 0.22 installation script.

Special thanks to Noël Martinon, Félix Merzeau, Gil Deluermoz and Camille Montchicourt for their patience on this.


0.23.3 (2014-06-18)
-------------------

** Bug fixes **

* Fix static files compression when using Google Mercator projection in maps
* Fix intermediary points order in topology de/serialization, and remove useless 
  topology serialization optimizations (fixes #1031)


0.23.2 (2014-06-13)
-------------------

** Bug fixes **

* Fixed land records not shown in detail pages
* Fixed JSON DEM area extent for treks
* Fixed targets list for tourism datasources (fixes #1091)
* Cache tourism datasources for one day (setting ``CACHE_TIMEOUT_TOURISM_DATASOURCES``)
* Fix crashes with TourInFrance sources
* Add link to OSM in feedback email (fixes #1089, #1093)
* Fix feedback email translation (fixes #1087)
* Fix problem with permission check "read attachment" in detail page (fixes #1092)
* Fix measure control appearing twice in forms (fixes #1078)
* Fix 404 on download buttons from list views
* Fix POI translated fields not tabbed (fixes #1065)
* Fix missing translation of "Add a new POI" (fixes #1086)
* Fix invalid snapping when save path without editing geometry (fixes #1099)
* Add missing properties in feedback report detail page.
* Hide all modules information in report detail page.
* Add missing translations of feedback module.
* Show object type in ODT export (fixes #1000)


** Internal changes **

* Upgraded to Mapentity 1.4.0
* Upgraded to Leaflet 0.7.3

** Installation **

* Fixed content types migration of land to zoning apps (Thanks Noël Martinon)

* UbuntuGIS stable maintainers have *upgraded* (sic) GDAL to 1.10.0.
  Upgrading GDAL is painful, and PostGIS packages may have to be reinstalled
  (data shouldn't be lost though). *Remember it was recommended to run PostGIS
  on a different server*.

:notes:

    On June 2th 2014, the Ubuntu GIS stable repository switched from ``libgdal1``
    to ``libgdal1h``. It broke the deployment script of many projects, including
    *Geotrek*.

    It is a good thing, since it paves the way for the last Ubuntu LTS release (14.04). However, it breaks the *Long Term Support* philosophy of the previous one (12.04), supposed to be supported until 2019.

    **Morality** : we cannot trust the *Ubuntu GIS stable* repository anymore.

    Regarding *Geotrek*, such upgrades of Ubuntu packages is not supposed to be covered
    by its installation script. If you face any problems, please refer to the
    community or commercial support (such as *Makina Corpus* for example).


0.23.1 (2014-05-22)
-------------------

** Bug fixes **

* Fixed regression when editing topologies without modification
* Fixed widget for Trails to allow linear topologies only


0.23 (2014-05-22)
-----------------

** Breaking changes **

Read all release notes carefully.

* Trails are now managed as topologies (fixes #370).
  Existing trails geometries are likely to be **LOST** (*see below*)
* Rename ``mailadmin`` to ``mailadmins`` in ``etc/settings.ini``
* Permission systems has been refactored (*see below*)

** Bug fixes **

* Force browser cache revalidation of geojson data (fixes #843)
* Force browser cache revalidation for path graph (fixes #1029)
* Fix deletion porblems in AdminSite (fixes #1008)
* Trek advised parking and public transport are translatable (fixes #1024)
* Fix missing translation "no filters" and "current criterias" (fixes #884)
* Fix PDF versions of documents not being translated (fixes #1028)

** New features **

* Command to import shapefile with points into POI as topologies (fixes #952)
* Add views to serve DEM on object area as JSON (*Geotrek-Rando 3D*)
* New tourism module : external datasources can be configured from Adminsite (*GeoJSON, TourInFrance, ...*)
  and added to maps (by module, or published on *Geotrek-rando*...)
* Show number of attached files in tab (fixes #743)
* New permission to control download of attachments
* New permission to allow users or groups to bypass structure restrictions
* Add a setting to serve attached files as download (default: True) (fixes #976)
* Track objects creations, changes and deletions (fixes #300)
* Added a reader group (fixes #495)
* Topologies are not recreated if user did not edit field (fixes #833)
* Added static file for projection EPSG:32620
* Show land objects in menu (fixes #942)
* Documented configuration of custom projections (fixes #1037)
* Buttons in the list menu to add new objects easily
* Add fullscreen button on maps (fixes #904)
* Add all controls on detail map (fixes #907)
* Add a button to close filters (fixes #424)
* Added new sections in documention : *FAQ*, *User-manal* and *Advanced configuration*

** Internal changes **

* Enabled database connection pooling in production
* An error is raised if SRID has not unit in meters (fixes #921)
* Zoning and land modules are now splitted (fixes #954)
* Complete refactor of geographical form fields. Now uses *django-mapentity*
  from its own repository instead of internal orphan branch.
* Complete refactor of maps initialization, without inline preprocessed JavaScript
* Rely on Django permissions to control access to detail, list and exports (fixes #675)
* Core and altimetry modules are now splitted (fixes #996)
* Renamed treks POIs GeoJSON properties

:notes:

    * Before upgrading, backup your trail records and geometries, using pgAdmin ::

        CREATE TABLE backup_sentiers AS SELECT * FROM l_v_sentiers;
        CREATE TABLE backup_troncons_sentiers AS (
          SELECT l_t_troncon.id AS troncon, l_t_sentier.id, l_t_sentier.nom
          FROM l_t_troncon, l_t_sentier
          WHERE l_t_sentier.id = l_t_troncon.sentier
        );

    * Before upgrade, rename ``mailadmin`` to ``mailadmins`` and add
      a new line ``mailmanagers`` in ``etc/settings.ini``. See *Email settings*
      section in documentation.

    * Just before upgrading, delete the following folders  ::

        rm -rf lib/src/django-modeltranslation lib/src/mapentity

:notes:

    * After upgrading, load the default permissions of the previous groups, otherwise
      users won't have access to their modules ::

        bin/django loaddata geotrek/authent/fixtures/minimal.json
        bin/django loaddata geotrek/authent/fixtures/basic.json

    * After upgrading, make sure *Active* is checked for the user *__internal__*
      otherwise screenshotting won't work.

    * After upgrading, load basic data for the new module ::

        bin/django loaddata geotrek/feedback/fixtures/basic.json

    * After upgrading, make sure the user specified in *Geotrek-rando* is
      in the group *Geotrek-rando*, or has at least the following permissions
      in the AdminSite :

      - ``paperclip | attachment | Can read attachments``
      - ``trekking | Trek | Can read Trek``
      - ``trekking | Trek | Can export Trek``
      - ``trekking | POI | Can read POI``
      - ``trekking | POI | Can export POI``
      - ``feedback | Report | Can add report``

    * After upgrading, compare visually the resulting migrated trails using QGis,
      by opening both layers ``l_v_sentiers`` and ``backup_sentiers``.


0.22.6 (2014-04-27)
-------------------

* Remove hard-coded mentions of EPSG:2154 in database initial
  migrations (fixes #1020)
* Fix version download and unzip in installation script.

Thanks Noël Martinon, from Guadeloupe National Park, for reporting both issues.


0.22.5 (2014-03-19)
-------------------

* Fix compilation of translations (ref #970)
* Fix distinction between languages and translated languages (fixes #968)
* Fix history tabs not being shown after upgrade to Django 1.6 (fixes #975)
* Fix regression on land layer label colors (fixes #980)
* Fix attached files not shown after file upload/delete (fixes #933)
* Fix links being removed from trek descriptions (fixes #981)
* Fix missing thumbnail in trek and POI detail pages
* Fix black background on map captures (fixes #979)
* Increased scale text size on map captures (fixes #850)
* Show map attributions on map captures (fixes #852)
* Fix aspect ratios of map in trek public documents (fixes #849)
* Fix objects list not being filtered on map extent (fixes #982)
* Fix coherence of map layer when text search in objects list (fixes #702)
* Fix number of results not refresh on text search (fixes #865)

* Added north arrow in map image exports (fixes #851)
* Removed darker effect on backgrounds for map image exports, and added internal
  advanced setting ``MAPENTITY_CONFIG['MAP_BACKGROUND_FOGGED'] = True``


0.22.4 (2014-03-06)
-------------------

* Fix install.sh not compiling locale messages (fixes #965)
* Moved trek completeness fields to setting `TREK_COMPLETENESS_FIELDS`. Duration
  and difficulty were added, arrival was removed (fixes #967)
* Fix regression about source locale messages (fixes #970)
* Fix regression link `Back to application` lost from adminsite (fixes #971)
* Serve uploaded files as attachments (fixes #972)
* Remove help texts being shown from filter forms (fixes #966)
* Fix form pills for translated languages (fixes #968)

0.22.3 (2014-02-17)
-------------------

* Fix install.sh help not being shown
* Fix screenshots being empty if deployed behind reverse proxy with rool url (fixes #687)
* Fix GPX file layer circle marker size (fixes #930)
* Remove JS libraries from login page
* Fix install.log being removed during installation
* Fix execution characters being shown during DB backup prompt
* Fix PhantomJS and CasperJS installation and deployment
* Added more automatic frontend tests
* Default allowed hosts is now `*`

0.22.2 (2014-02-14)
-------------------

* Fix secured media URLs when using a non empty `rooturl` setting
* Fix proxy errors by disabling keep-alive (fixes #906)

0.22.1 (2014-02-13)
-------------------

* Prevent install script to delete existing media files from disk
  in some situations.

0.22 (2014-02-12)
-----------------

**Before upgrade**

* Backup your database.
* If you upgrade in the same application folder, first delete the `geotrek`
  sub-folder.
* Use `install.sh` to upgrade (`make deploy` won't be enough)
* After upgrade, make sure the following query returns only ~23 results:

    SELECT COUNT(*) FROM south_migrationhistory;


**BREAKING changes**

* For upgrades, Geotrek 0.21 is required.
* Uploaded files are now restricted to authenticated users (fixes #729)

:notes:

    *Geotrek-rando* 1.23 or higher is required to synchronize content.

**NEW features**

* In list view, click on map brings to detail page, mouse over highlights in list.
* Show path icon if intervention is not on infrastructure (fixes #909)
* Add spanish translation
* Add photographie into default attachments filetype
* Map location combobox (Cities, Districts, Areas) are not shown if empty or disabled.
* Several database views have been created (fixes #934)
* Remove dots from path icon (fixes #939)
* Intervention, infrastructure and project filters list of years is now dynamic (fixes #948)
* Application available languages (*english*, *french*, *italian*, *spanish*) are now
  distinct from translated content languages (`languages` value in :file:`settings.ini`)

Minor changes

* Improved apparence of map controls
* Improved apparence of path intermediary points
* Improved apparence of form validation buttons
* Add auto-generated docs at /admin/doc/
* Nicer installation script output

Installation script

* Scan and ortho attributions can now be set using `scan_attributions` and
* Propose to backup DB before Geotrek upgrade (fixes #804)
* Settings edition prompt only happens at first install
  `ortho_attributions` in *settings.ini*.

**BUG fixes**

* Fix convert urls behind reverse proxy with prefix
* Fix deployment problem if ``layercolor_others`` not overidden in settings.ini
* Fix topology kinds to be 'INTERVENTION' for intervention without signage/infrastructure
* Fix restricted areas types display in admin (fixes #943)
* Fix list ordering of trek relationships and web links (fixes #929)
* Fix nginx log files being already empty after logrotate (fixes #932)
* Fix project add button when no permission

:notes:

  List of restricted areas is not shown on map by default anymore. Restore
  previous behaviour with advanced setting `LAND_BBOX_AREAS_ENABLED` as True.

**Internal changes**

* Upgrade to Django 1.6 (fixes #938)
* Upgrade to Leaflet 0.7
* Upgrade a great number to python and JavaScript libraries
* An internal user (with login permission) is used to authenticate the Conversion
  and Capture services.
* Installation script is modular (standalone, geotrek only, ...)
* Developement server now listens on all interfaces by default
* Database migrations were resetted, no postgres `FATAL ERROR` message will
  be emitted on fresh install anymore (fixes #937). See *Troubleshooting* in documentation.


0.21.2 (2014-02-04)
-------------------

**BUG fixes**

* Warn on tiling landscape/portrait spatial extent only if map with local projection
* Safety check on thumbnailing if images are missing from disk (*useful for troubleshooting,
  when importing existing dumps*).
* Fix overlapping filter if no records present (fixes #931)


0.21.1 (2013-12-11)
-------------------

**Improvements**

* Smooth DEM drapping, improving altimetric information and profiles (fixes #840, ref #776)

**BUG fixes**

* Signage forms are now restricted by structure (fixes #917)
* Fix geometries computation when path split occurs on return topology (fixes #899)
* Add title on links in list views (fixes #913)
* Prevent horizontal scroll on forms, caused by textareas (fixes #914)
* Fix empty 3d geometry of point topologies with offset (fixes #918)

:notes:

    In order to recompute all paths topologies altimetry information, you can perform
    the following queries:

       ``UPDATE l_t_troncon SET geom = geom;``
       ``UPDATE e_t_evenement SET decallage = decallage;``

    Reading information from rasters is costly. Be prepared to wait for a while.


0.21 (2013-11-28)
-----------------

**Improvements**

* Increase height of multiple select (fixes #891)
* Add project field in intervention filter (fixes #896)
* Many minor improvements for infrastructures in adminsite (fixes #886)
* Add category in intervention filter (fixes #887)

**BUG fixes**

* Fix KML coordinates not being in 3D.
* GPX now has trek description (fixes #775)
* Order overlapping topologies by order of progression (fixes #777)
* Improved TinyMCE configuration, for resize and cleanup (fixes #351, #711)
* Changed trek duration interval for notion of days (fixes #880)
* Show city departure in trek public export (fixes #881)
* Document customization of TinyMCE config (fixes #882)
* Fix 404 error on path delete (fixes #900)
* Fix project constraints not being displayed in details (fixes #893)
* Fix organism translation in project form (fixes #892)
* Fix apparence of forms on small screen (fixes #744, #902)
* Fix modify button being hidden to editors (fixes #901)
* Fix overlap between map controls and label (fixes #883)
* Fix translation of district in list filters (fixes #890)
* Fix integrity error on land intersection on path update (fixes #897)
* Fix form layout problems (fixes #712, #879)

0.20.9 (2013-10-30)
-------------------

* Fix altimetric profile if topology geometry is wrong (fixes #875)
* Fix apparence of creation button in intervention list (fixes #877)
* Fix topology geometries that were sampled like paths 3D geometry (fixes #878)
* Fix topology lines geometries join in some situations (ref #722)
* Fix topology not well displayed if start/end on intersection (fixes #874)

0.20.8 (2013-10-22)
-------------------

* Public trek export : Fix various layout regressions (ref #848)
* Public trek export : Show POI theme pictogram (fixes #858)
* Public trek export : full width for information desk frame (fixes #856)
* Public trek export : add footer with trek title and page numbers (fixes #861)
* Public trek export : add floating picture in POI detail (fixes #860)
* Public trek export : fix POI thumbnails missing (fixes #869)
* Fix point offset lost on path update (fixes #867)
* Fix reconnect point topologies with offset to closest path (fixes #868)

0.20.7 (2013-10-16)
-------------------

* Fix topology geometry 3D being draped twice (fixes #863)
* Altimetric profile : Show max distance and round values (fixes #853)
* Altimetric profile : Add settings for colors (fixes #854)
* Public trek export : POIs list in two columns (fixes #855)
* Public trek export : POIs details without column break (fixes #857)
* Public trek export : Show pictures attributions (fixes #859)
* Public trek export : Use 10pt fonts in every text blocks (fixes #848)

:notes:

    # Empty profiles cache
    rm -rf var/media/profiles/*


0.20.6 (2013-10-14)
-------------------

* Remove 3D from JS WKT serializer
* Safety check if path is less than 1m
* Remove mentions of 2154 projection in schema migrations
* Fix performance issues in altimetric JSON (fixes #845)
* Fix filter forms missing from Trek and POI lists (fixes #847)
* Fix empty Nginx log files (fixes #846)


0.20.5 (2013-10-09)
-------------------

* Fix migration of draping utility function

0.20.4 (2013-10-09)
-------------------

* Fix sort stake by id (level) (fixes #835)
* Rename stake to maintenance stake (fixes #834)
* Add validity to path filter (fixes #836)
* Do not redrape topology geometries, use path 3D geometry (fixes #832)
* Fix document export of Trail objects (fixes #839)
* Fix trail helpers for land layers (fixes #838, ref #842)
* Fix install on fresh folder, missing folder ``lib/src`` (fixes #844)


0.20.3 (2013-09-30)
-------------------

**BUG fixes**

* Fix typo in french translation of Properties (fixes #815)
* Fix missing description from infrastructure/signage detail page (fixes #816)
* Fix Cities / Districts / Restricted Areas in project detail page (fixes #817)
* Fix only deleted topology can have geom = NULL (fixes #818)
* Fix geometries not editable in QGis by switching path and topologies
  geometries to 2D (fixes #688)
* Fix altimetric sampling precision setting not taken in account in SQL (ref #776)


0.20.2 (2013-08-27)
-------------------

* Fix convert urls behind reverse proxy with prefix
* Fix Trek public print conversion
* Fix display of trek length in public document (one decimal only)
* Fix altimetric graph delaying map display in detail pages

:notes:

    # Empty maps captures cache
    rm -rf var/media/maps/trek-*


0.20.1 (2013-08-26)
-------------------

* Add DB index for start and end columns
* Merge gunicorn logs with respective applications logs
* Lower logging level in production (WARNING -> INFO)

**BUG fixes**

* Fix deployment error with application's TITLE
* Fix deployment errors with mandatory external authent values
* Fix trek export layout: fit map image and altimetric profile in one page.


0.20 (2013-08-23)
-----------------

* Edit difficulty id in Admin site, mainly used to order difficulty levels (fixes #771)
* Use explicit list of fields in forms, instead of excluding model fields (fixes #736).
  Issue #712 was closed too, since most suspected cause was field listings. Please re-open
  if problem re-appears.
* Fix timeout on POI Shapefile and CSV exports (fixes #672)
* Altimetric profiles are now computed in PostGIS (fixes #778, #779)
* Positive and negative ascents are now computed using more DEM resolution (fixes #776)

:notes:

    Setting ``PROFILE_MAXSIZE`` was replaced by ``ALTIMETRIC_PROFILE_PRECISION`` which
    controls sampling precision in meters (default: 20 meters)

* Altimetric profiles were removed from object map images
* Altimetric profiles are now plotted using SVG
* Altimetric profiles are now inserted into path documents and trek public printouts (ref #626)
* Fix deletion of associated interventions when editing infrastructures (fixes #783)
* Latest record is updated (*touch*) when a DELETE is performed on table (refreshs cache) (fixes #698)

* Reworked settings mechanism to follow Django best practices

:notes:

    Replace all computed values from ``etc/settings.ini``. For example, replace "60 * 60"
    by 3600. (You can increase this value to several hours by the way)

* Allow server host to capture pages (fixes #733)
* Adjust map capture according to geometry aspect ratio (fixes #627)
* Always show path layer in detail pages (fixes #781)
* Fix restore of topology on loop paths (fixes #760)
* Fix topology construction when loop is formed by two convergent paths (fixes #768)
* Added small tool page at ``/tools/extents/`` to visualize configured extents (ref #732)
* Removed setting ``spatial_extent_wgs84``, now computed automatically from ``spatial_extent``,
  with a padding of 10%.

:notes:

    Have a look at ``conf/settings.ini.sample`` to clean-up unnecessary values from your
    settings file.

* Fix paths offset for portrait spatial extent (fixes #732)
* Rely on Tilecache default max resolution formulae (fixes #732)
* Due to bug in Leaflet/Proj4Leaflet (https://github.com/kartena/Proj4Leaflet/issues/37)
  landscape spatial extents are not supported. Please adjust spatial_extent to be a portrait or square,
  or application will raise *ImproperlyConfiguredError*.
* Reload map objects on zoom out too (fixes #435)
* Fix computation of *min_elevation* for point topologies (fixes #808)

:notes:

    In order to recompute all paths topologies altimetry information, you can perform
    the following query: ``UPDATE e_t_evenement SET decallage = decallage;``.
    Reading information from rasters is costly. Be prepared to wait for a while.


0.19.1 (2013-07-15)
-------------------

* Restore ``pk`` property in Trek GeoJSON layer


0.19 (2013-07-12)
-----------------

* Intervention length field (readonly if geometry is line)
* Fix apparence bug if no rights to add treks and pois (fixes #713)
* Fix extremities snapping (fixes #718)
* Show information desk in trek detail page (fixes #719)
* Fix topology adjustments after path split (fixes #720)
* On edition show global line orientation instead of individual paths (fixes #679)
* Fix invalid topology if trek goes twice on same path (fixes #671)
* Overlapping is now more precise (fixes #710)
* Reworked trek print layout
* Fix topology building if paths are taken twice (fixes #722)
* Fix tiling offset with horizontal bboxes
* Fix display of POI layer by default on list (fixes #696)
* Fix translation of not validated paths (fixes #730)
* Fix error if topology is required and empty (fixes #745)
* Fix duplication of N-N relations on path split (fixes #738)
* Fix project map in detail page (fixes #734)
* Fix project listed deleted interventions (fixes #739)
* Fix project listed infrastructures through interventions (fixes #740)
* Fix saving intervention form on infrastructure
* Repair serializing of properties after upgrade of django-geojson (fixes #755)
* Added ``public_transport`` and ``advised_parking`` to trek JSON detail API (fixes #758)
* Repair land layers colors after upgrade of django-geojson
* Upgraded to django-geojson 2.0
* Upgraded to Django 1.5

:notes:

    Specify allowed host (server IP) in ``etc/settings.ini`` (*for example*):
    * ``host = 45.56.78.90``
    Empty object caches:
    * ``sudo /etc/init.d/memcached restart``
    * ``rm -rf ./var/cache/*``


0.18 (2013-06-06)
-----------------

* Add pretty trek duration in JSON
* Add information desk field in Trek (fixes #624)


0.17 (2013-05-17)
-----------------

* Show trek duration as human readable in minutes, hours and days (fixes #471, #683)
* Fix hover on paths that interfered with clic for topology creation (fixes #680)
* Run API urls on different workers (ref #672)
* Fix redirect to root url after logout (fixes #264)
* Fix redirect to next after login (fixes #381)
* Switch to Memcached instead of local memory in production
* Move secret key to settings.ini
* Relate paperclip FileType to Structure (fixes #256)
* Relate PhysicalTypes to Structure (fixes #255)
* Relate Organisms to Structure (fixes #263)
* Compute max_resolution automatically
* Fix creation and edition of interventions on infrastructures (fixes #678)
* Change default objects color to yellow
* Restored Italian translations
* Fix regex for RAISE NOTICE (fixes #673)
* Initial public version

See project history in `docs/history.rst` (French).