from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Song
from .serializers import SongSerializer

class SongListAPIView(generics.ListCreateAPIView):

  queryset = Song.objects.all()
  serializer_class = SongSerializer

class SongFindByNameAPIView(APIView):

  """
  200 - good
  400 - QP missing
  404 - Song not found
  500 - Other (internal)
  """

  def get(self, request, *args, **kwargs):

    songName = request.query_params.get('name')

    if not songName:
      return Response({"response": "query parameter is missing"}, status = status.HTTP_400_BAD_REQUEST)

    try:
      #iexact for case insesnsitive search.
      song = Song.objects.get(name__iexact=songName)
      serializer = SongSerializer(song)
      
      return Response(serializer.data, status=status.HTTP_200_OK)

    except Song.DoesNotExist:
      return Response({"response": "Song not found!"}, status = status.HTTP_404_NOT_FOUND)

    except Exception as e:
      return Response({"response": f"{str(e)}"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class SongDetail(APIView):
  """
  get (by primary key) a song into the DB 
  put (by primary key) new data into an existing entry in DB
  post a new song to the DB
  """
  
  def get_object(self, pk):
    try:
      return Song.objects.get(pk=pk)
    except Song.DoesNotExist:
      return Response({"response": "Song not found!"}, status = status.HTTP_404_NOT_FOUND)
    
  def get(self, request, pk, format=None):
    song = self.get_object(pk)
    serializer = SongSerializer(song)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    song = self.get_object(pk)
    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def post(self, request, format=None):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
