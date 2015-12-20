from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$', 'news_all'),
    url(r'^(?P<pk>\d+)/', 'new_details'),
    url(r'^(?P<latest_url>\w+)/(?P<pk>\d+)/', 'new_details'),
)
