from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
]
