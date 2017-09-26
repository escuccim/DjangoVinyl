# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('label', models.CharField(max_length=128)),
                ('catalog_no', models.CharField(blank=True, max_length=56, null=True)),
                ('style', models.CharField(blank=True, max_length=199, null=True)),
                ('discogs', models.CharField(blank=True, max_length=128, null=True)),
                ('thumb', models.CharField(blank=True, max_length=128, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['label', 'artist', 'title'],
                'db_table': 'records_new',
                'get_latest_by': 'updated_at',
            },
        ),
    ]