# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_waypoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('population', models.FloatField()),
                ('density', models.FloatField()),
                ('created', models.DateField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4236)),
            ],
        ),
    ]
