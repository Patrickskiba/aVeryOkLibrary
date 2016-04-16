# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 13:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checked_out_by',
            field=models.CharField(default=datetime.datetime(2016, 4, 16, 13, 23, 11, 581920, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
