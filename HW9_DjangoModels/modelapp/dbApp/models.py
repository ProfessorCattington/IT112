from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Song(models.Model):

    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.IntegerField(blank=False)

    def prettyPrint(self):
        return f"{self.name} from the album {self.album} by {self.artist} released in {self.year}"
    
    def findSongByName(songName):
        try:
            return Song.objects.get(name = songName)
        except ObjectDoesNotExist:
            print(f"{songName} not found!")
        except Exception as e:
            print(e)

    def findSongsByArtist(queryArtist):
        return Song.objects.filter(artist = queryArtist)

    
    