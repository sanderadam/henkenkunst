# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomgr', '0003_schilderij_zichtbaar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schilderij',
            name='beschrijving',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='schilderij',
            name='formaat',
            field=models.CharField(max_length=500),
        ),
    ]
