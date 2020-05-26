from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Theme, Theming


def articles_list(request):
    template = 'articles/news.html'
    news = Article.objects.all()
    new_thems = Theming.objects.all().prefetch_related('theme', 'article')\
        .values('article__title', 'theme__name', 'main_theme').order_by('-main_theme', 'theme__name')
    context = {'object_list': news,
               'new_thems': new_thems
               }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
