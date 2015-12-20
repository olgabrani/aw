from django.db import models
from django.template.loader import render_to_string
from django.conf.urls import patterns, url, include
from django.conf import settings
from feincms.content.application.models import reverse
from feincms.content.application.models import ApplicationContent
from feincms.module.page.extensions.navigation import NavigationExtension
from feincms.module.page.extensions.navigation import PagePretender
from feincms.module.page.models import Page

class New(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    content = models.TextField()

    def __unicode__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('news.views.new_details', 'news.urls', (), {
            'pk': self.pk,
        })

    def get_absolute_url_latest(self):
        return reverse('news.views.new_details', 'news.urls', (), {
             'latest_url': settings.GLOBAL_VARS['NEWS_URL'],
	     'pk': self.pk,
        })

class LatestNews(models.Model):
    title = models.CharField(max_length=255)
    limit = models.PositiveIntegerField(default=5)

    class Meta:
        abstract = True


    def render(self, **kwargs):
        return render_to_string(['latest_news.html'], {'news':New.objects.all().order_by('-pub_date')[:self.limit], 'content': self})
 
