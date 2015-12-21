from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'schedule.views.events', name='events'),
)

