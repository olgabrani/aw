from django.conf.urls import patterns, url
from gallery.admin import admin_thumbnail

urlpatterns = patterns('gallery.views',
    url(r'^$', 'gallery_list', name='gallery_list'),
    url(r'^thumbnail/$', admin_thumbnail, name='gallery_admin_thumbnail'),
    url(r'^(?P<pk>\d+)/', 'gallery_list', name='gallery_list'),
)
