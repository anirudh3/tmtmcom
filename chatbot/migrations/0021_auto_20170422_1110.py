# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0020_auto_20170422_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='acousticness',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='danceability',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='energy',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='instrumentalness',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='key',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='liveness',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='loudness',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='speechiness',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='tempo',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='time_signature',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='valence',
            field=models.DecimalField(decimal_places=6, default=None, max_digits=7, null=True),
        ),
    ]
