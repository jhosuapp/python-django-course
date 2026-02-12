from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    song_name = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    singer = models.ForeignKey(Singer, on_delete=models.PROTECT, related_name='singers')
    duration = models.IntegerField()
    
    def __str__(self):
        return self.song_name