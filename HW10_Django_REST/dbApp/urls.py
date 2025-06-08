from django.urls import path
from .views import *

urlpatterns = [
    path('songs/', SongListAPIView.as_view(), name='songlist'),
    path('songs/find/', SongFindByNameAPIView.as_view(), name ='songfindbyname'),
    path('songs/<int:pk>/', SongDetail.as_view(), name='songdetail'),
]
