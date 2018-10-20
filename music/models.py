from django.db import models

# Create your models here.

#class Users(models.Model):
#    username = models.CharField(primary_key=True, max_length=100)
#    password = models.CharField(max_length=100)
#    email = models.CharField(max_length=100)
#    album_logo = models.CharField(max_length=1000)

#class Admins(models.Model):
#    username = models.CharField(primary_key=True, max_length=100)
#    password = models.CharField(max_length=100)
#    email = models.CharField(max_length=100)

#class Videos(models.Model):
#    videoid = models.IntegerField(primary_key=True, max_length=1000)
#    videotitle = models.CharField(max_length=100)
#    videologo = models.CharField(max_length=100)
#    releasedate = models.DateField()

class Songs(models.Model):
    songid = models.IntegerField(primary_key=True, max_length=1000)
    artist = models.CharField(max_length=100)
    songtitle = models.CharField(max_length=100)
    albumtitle = models.CharField(max_length=100)
    albumlogo = models.CharField(max_length=100)
    releasedate = models.DateField()
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.songtitle + ' by ' + self.artist
#class VideoDetails(models.Model):
#    videoid = models.ForeignKey(Videos, max_length=1000)

#class SongsDetails(models.Model):
#    songid = models.ForeignKey(Songs, max_length=1000)

class SongDetails(models.Model):
    songid = models.ForeignKey(Songs, on_delete=models.CASCADE)
    songhits = models.IntegerField()
    #is_favourite = models.BooleanField(default=False)
