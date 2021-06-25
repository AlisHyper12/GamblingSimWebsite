from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.index, name="index"),
    path('', views.home, name="home"),
    path('downloads/', views.downloads, name="downloads")
]
