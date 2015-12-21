from django.db import models
from django.template.loader import render_to_string
from django.conf.urls import patterns, url, include
from django.conf import settings
from feincms.content.application.models import reverse

from mptt.models import MPTTModel

from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey
from feincms.content.application import models as app_models

class Article(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    description = models.TextField(blank=True, null=True, default="")
    image = MediaFileForeignKey(MediaFile,blank=True,null=True, related_name ='image', help_text='This is the image that will appear in the articles list page')
    gallery_image = MediaFileForeignKey(MediaFile,blank=True,null=True, related_name='gallery_image', help_text='This is the image that will appear in the gallery. Dimensions should be 662px*300px. Otherwise, the image will be stretched accordingly.')
    category = models.ManyToManyField('aw.Category', blank=True, null=True)
    author = models.ForeignKey('aw.Reporter')
    is_featured = models.BooleanField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles.views.article_details', 'articles.urls', (), {
            'slideshow_url': settings.GLOBAL_VARS['ARTICLES_URL'],
            'slug': self.slug,
        })

    def get_absolute_url_slideshow(self):
        return reverse('articles.views.article_details', 'articles.urls', (), {
             'slideshow_url': settings.GLOBAL_VARS['ARTICLES_URL'],
             'slug': self.slug,
        })

class ArticlesSlideshow(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


    def render(self, **kwargs):
        return render_to_string(['articles_slideshow.html'], {'articles':Article.objects.all().filter(is_featured=True).order_by('-pub_date')[:3],'content': self})
