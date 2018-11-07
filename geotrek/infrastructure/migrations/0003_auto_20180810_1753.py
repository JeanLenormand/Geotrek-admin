# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geotrek.authent.models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0002_auto_20180608_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructurecondition',
            name='structure',
            field=models.ForeignKey(blank=True, db_column=b'structure', default=geotrek.authent.models.default_structure_pk, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.Structure', verbose_name='Related structure'),
        ),
    ]