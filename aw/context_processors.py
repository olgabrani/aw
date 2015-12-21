from django.conf import settings
from aw.models import Application
from feincms.module.medialibrary.models import Category

def application(request):
    try:
        app = Application.current()
    except:
        app = 'aw'
    return {'APP': app, 'WORDS': settings.WORDS, 'GLOBAL_VARS': settings.GLOBAL_VARS,}

def test(request):
    galleries = Category.objects.filter(parent__title='Gallery').values()
    try:
	return { 'galleries':galleries }
    except:
	return { 'galleries': '[1,2]' }
