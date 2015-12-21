from django.db import models
from django.template.loader import render_to_string
from django.conf.urls import patterns, url, include
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class Event(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    CATEGORIES_OPTIONS = (
        ('INL', 'Inline Training'),
        ('ICE', 'Ice Training'),
        ('EVE', 'Events'),
        ('GAM', 'Games'),
    )	
    category = models.CharField(max_length=3, choices=CATEGORIES_OPTIONS)
    link = models.CharField(max_length=200, blank=True, null=True)    
 
    def __unicode__(self):
        return self.title
