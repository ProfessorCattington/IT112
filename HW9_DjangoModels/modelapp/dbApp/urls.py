from django.urls import path
from . import views

urlpatterns = [
    path('', views.songlist, name='songlist'),
    path('songs/<int:pk>/', views.songDetail, name = 'songDetail'),
]
