# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomgr', '0002_schilderij_formaat'),
    ]

    operations = [
        migrations.AddField(
            model_name='schilderij',
            name='zichtbaar',
            field=models.BooleanField(default=True),
        ),
    ]
