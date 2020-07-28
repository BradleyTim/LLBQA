from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('<str:tag>/', views.get_by_tags, name='blog-by-tag'),
    path('<int:pk>/<slug:slug>/', views.detail, name='blog-detail'),
]
