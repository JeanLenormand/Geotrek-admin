# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensitivity', '0002_sensitivearea_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensitivearea',
            name='category',
            field=models.IntegerField(default=1, verbose_name='Category', db_column=b'categorie', choices=[(1, 'Species'), (2, 'Regulatory')]),
        ),
    ]
