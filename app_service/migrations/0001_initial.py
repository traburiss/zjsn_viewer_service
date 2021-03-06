# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KanmusuEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(max_length=12)),
                ('equipment_name', models.TextField()),
                ('equipment_level', models.IntegerField()),
                ('equipment_type', models.CharField(max_length=24)),
                ('equipment_suit_type', models.TextField()),
                ('equipment_from', models.TextField()),
                ('equipment_make_time', models.CharField(max_length=24)),
                ('equipment_make_threshold', models.CharField(max_length=24)),
                ('equipment_discard', models.CharField(max_length=24)),
                ('equipment_range', models.CharField(max_length=4)),
                ('equipment_fire', models.IntegerField(default=0)),
                ('equipment_torpedo', models.IntegerField(default=0)),
                ('equipment_antisubmarine', models.IntegerField(default=0)),
                ('equipment_boom', models.IntegerField(default=0)),
                ('equipment_antiair', models.IntegerField(default=0)),
                ('equipment_armor', models.IntegerField(default=0)),
                ('equipment_hit', models.IntegerField(default=0)),
                ('equipment_flee', models.IntegerField(default=0)),
                ('equipment_tracking', models.IntegerField(default=0)),
                ('equipment_lucky', models.IntegerField(default=0)),
                ('equipment_antiair_correct', models.FloatField(default=0)),
                ('equipment_special_effect', models.TextField()),
                ('equipment_info', models.TextField()),
            ],
        ),
    ]
