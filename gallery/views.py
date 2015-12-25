from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.db import models
from gallery.models import Gallery
from django.conf import settings
from datetime import date
from aw.settings import STATIC_URL

def gallery_list(request, pk=6):
    gallery = Gallery.objects.get(pk=pk)
    gallery_list = Gallery.objects.all()
    return render_to_response('gallery_list.html', {'gallery_list': gallery_list, 'gallery': gallery })

def gallery_details(request, pk):
    gallery_details = Gallery.objects.filter(pk=pk)
    return render_to_string(['gallery_details.html'], {'gallery_details':gallery_details, 'STATIC_URL':STATIC_URL, })
