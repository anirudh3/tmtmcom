# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0012_playlistres_ownerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=160)),
                ('uri', models.CharField(max_length=160)),
                ('img', models.CharField(max_length=160)),
                ('popularity', models.CharField(max_length=160)),
                ('created', models.DateTimeField(default=None)),
                ('ordering', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.CharField(max_length=160)),
                ('artist', models.CharField(max_length=160)),
                ('album', models.CharField(max_length=160)),
                ('img', models.CharField(max_length=160)),
                ('uri', models.CharField(max_length=160)),
                ('popularity', models.CharField(max_length=160)),
                ('created', models.DateTimeField(default=None)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='chatters',
            name='top_artists',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topartists', to='chatbot.Artists'),
        ),
        migrations.AddField(
            model_name='chatters',
            name='top_tracks',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toptracks', to='chatbot.Tracks'),
        ),
    ]
