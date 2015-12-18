# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string 
from mptt.models import MPTTModel
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext

from feincms.module.blog.models import Entry, EntryAdmin
from feincms.module.page.models import Page
from feincms.module.page.extensions.navigation import NavigationExtension, PagePretender
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey

from feincms.content.raw.models import RawContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.application.models import ApplicationContent, app_reverse
from feincms.content.richtext.models import RichTextContent
from feincms.content.section.models import SectionContent
from feincms.content.contactform.models import ContactFormContent

Page.register_templates({
    'key': 'base',
    'title': 'Base Template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main region'),
        ('sidebar', 'Sidebar', 'inherited'),
        ('bottom','Bottom','inherited'),
        ),
    },{
    'key': 'base_sitemap',
    'title': 'Base Sitemap Template',
    'path': 'base_sitemap.html',
    'regions': (
        ('main', 'Main region'),
        ('sidebar', 'Sidebar', 'inherited'),
        ('bottom','Bottom','inherited'),
        ),
    })
Page.create_content_type(RawContent, regions=('bottom'))
Page.create_content_type(RichTextContent)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))

def get_admin_fields(form, *args, **kwargs):
    return {
        'exclusive_subpages': forms.BooleanField(
            label=capfirst(_('exclusive subpages')),
            required=False,
            initial=form.instance.parameters.get('exclusive_subpages', False),
            help_text=_('Exclude everything other than the application\'s content when rendering subpages.'),
            ),
    }

Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('blog_urls', 'Blog', {'admin_fields': get_admin_fields}),
    ('news.urls', 'News Application'),
    ('articles.urls', 'Articles Application'),
    ('players.urls', 'Players'),
    ('schedule.urls','Calendar'),
    ('gallery.urls','Gallery New'),
    ))


Entry.register_regions(
    ('main', 'Main region'),
    )
Entry.create_content_type(RawContent, regions=(''))
Entry.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))



Page.register_extensions(
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.sites',
    )


class Category(MPTTModel):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

class Single(models.Model):
    title = models.CharField(max_length=200, blank=False)    
    content = models.TextField() 
     
    class Meta:
        abstract = True
        verbose_name=_('Single page block')

    def render(self, **kwargs):
        return render_to_string(['content/single_box.html'], {'content': self})

class Double(models.Model):
    title = models.CharField(max_length=200, blank=False)    
    contentLeft = models.TextField()
    contentRight = models.TextField()
     
    class Meta:
        abstract = True
        verbose_name=_('Double page block')

    def render(self, **kwargs):
        return render_to_string(['content/double_box.html'], {'content': self})

class Triple(models.Model):
    title = models.CharField(max_length=200, blank=False)    
    contentOne = models.TextField()
    contentTwo = models.TextField()
    contentThree = models.TextField()

    class Meta:
        abstract = True
        verbose_name=_('Triple page block')

    def render(self, **kwargs):
        return render_to_string(['content/triple_box.html'], {'content': self})

class Simple(models.Model):
    title = models.CharField(max_length=200, blank=False)    
    text = models.TextField()
     
    class Meta:
        abstract = True
        verbose_name=_('Simple page block')

    def render(self, **kwargs):
        return render_to_string(['content/simple_box.html'], {'content': self})

class Advertisment(models.Model):    
    link = models.CharField(max_length=200, blank=False)
    sponsor = models.CharField(max_length=200, blank=True, null=True )
    image = MediaFileForeignKey(MediaFile,blank=True,null=True)

    class Meta:
        abstract = True
        verbose_name=_('advertisment')

    def render(self, **kwargs):
        return render_to_string(['content/advertisment.html'], {'content': self})

Page.create_content_type(Double, regions=('main','bottom'))
Page.create_content_type(Triple, regions=('main','bottom')) 
Page.create_content_type(Simple, regions=('main','bottom'))
Page.create_content_type(Single)
Page.create_content_type(Advertisment) 
Entry.create_content_type(Simple)
