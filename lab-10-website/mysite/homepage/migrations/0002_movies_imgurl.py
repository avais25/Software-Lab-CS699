# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='imgUrl',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
