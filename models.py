# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Record(models.Model):
    artist = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    catalog_no = models.CharField(max_length=56, null=True, blank=True)
    style = models.CharField(max_length=199, null=True, blank=True)
    discogs = models.CharField(max_length=128, null=True, blank=True)
    thumb = models.CharField(max_length=128, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.artist + ' - ' + self.title + ' - ' + self.label

    class Meta:
        db_table = 'records_new'
        get_latest_by = "updated_at"
        ordering = ['label','artist','title']
