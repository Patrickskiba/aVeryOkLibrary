# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 01:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_checked_out_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checked_out_date',
            field=models.CharField(default=datetime.datetime(2016, 4, 19, 1, 10, 33, 424000, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.CharField(default=datetime.datetime(2016, 4, 19, 1, 10, 49, 489000, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
