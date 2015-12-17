from django.conf.urls import patterns, include, url

urlpatterns = patterns('players.views',
    url(r'^$', 'players', name='players'),
)

