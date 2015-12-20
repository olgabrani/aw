from django.shortcuts import render_to_response
from django.db import models
from news.models import New
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings


def news_all(request):
    news_list = New.objects.all().order_by('-pub_date')
    paginator = Paginator(news_list, settings.NEWS_PAGINATOR) # Show 5 news per page
    page = request.GET.get('page')
    show_more = settings.WORDS['SHOW_MORE']
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render_to_response('news_list.html', {'news': news, 'show_more':show_more})


def new_details(request, pk):
    new_details = New.objects.filter(pk=pk)
    back = settings.WORDS['BACK']
    return render_to_response('new_details.html', {'new_details': new_details, 'back':back})

