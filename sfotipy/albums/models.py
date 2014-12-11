from django.db import models
from artists.models import Artist

# Create your models here.

class Album(models.Model):
	title = models.CharField(max_length=255)
	cover = models.ImageField(upload_to='albums')
	artist = models.ForeignKey(Artist)
