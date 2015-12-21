from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('articles.views',
    url(r'^$', 'articles_all', name='articles_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'article_details', name='article_details'),
    url(r'^(?P<slideshow_url>\w+)/(?P<slug>[-\w]+)/$', 'article_details', name='article_details'),
)

