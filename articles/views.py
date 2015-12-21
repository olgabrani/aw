from django.shortcuts import render_to_response, get_object_or_404
from django.db import models
from articles.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def articles_all(request):
    first_article = Article.objects.all().order_by('-pub_date')[0]
    articles_list = Article.objects.all().order_by('-pub_date')[1:]
    paginator = Paginator(articles_list, settings.NEWS_PAGINATOR) # Show 5 news per page
    page = request.GET.get('page')
    show_more = settings.WORDS['SHOW_MORE']
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return 'articles_list.html', {'articles': articles, 'first_article':first_article,  'show_more':show_more, 'page':page }

def article_details(request, slug):
    article_details = Article.objects.filter(slug=slug)
    #article_details = get_object_or_404(Article, slug=slug)
    back = settings.WORDS['BACK']
    return 'article_details.html', {'article_details': article_details, 'back':back}

