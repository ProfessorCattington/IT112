from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from dbApp.models import Song

def songlist(request):
 
  songList = Song.objects.all()
  songNames = [{'id':song.id, 'name': song.name} for song in songList]
  return render(request, 'base.html', {'songNames': songNames})

def songDetail(request, pk):
  
  song = get_object_or_404(Song, pk = pk)
  return render(request, 'songDetail.html', {'song' : song})
 