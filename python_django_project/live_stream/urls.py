from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('abc/', views.index, name='index'),
    path('', views.video_feed, name='video_feed'),
]