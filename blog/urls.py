from django.conf.urls import url
from django.urls import path
from pages.views import index
from .views import get_by_tags, detail

urlpatterns = [
    path('', index, name='blog-index'),
    path('topic-<str:tag>/', get_by_tags, name='blog-by-tag'),
    path('<int:pk>/<slug:slug>/', detail, name='blog-detail'),
]
