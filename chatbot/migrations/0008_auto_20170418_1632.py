# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_searchres_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatters',
            old_name='spotify',
            new_name='spotify_auth',
        ),
    ]
