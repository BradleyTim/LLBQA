from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('<int:pk>/', views.detail, name='blog-detail'),
    path('<str:tag>/', views.get_by_tags, name='blog-by-tag'),
]
