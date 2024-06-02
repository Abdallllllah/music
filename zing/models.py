from django.db import models

# Create your models here.

class playlist(models.Model):
    name =  models.CharField(max_length=100)
    numberOfSongs = models.IntegerField()
    def __str__(self):
        return self.name
class songs(models.Model):
    Track = models.CharField(max_length=100)
    Artist = models.CharField(max_length=100)
    Album = models.CharField(max_length=100)
    Length = models.TimeField(max_length=100)
    playlist = models.ManyToManyField('playlist')
    def __str__(self):
        return self.Track