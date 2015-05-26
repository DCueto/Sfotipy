from django.db import models
from datetime import datetime

# Create your models here.

class Artist(models.Model):
	nickname = models.CharField(max_length=100)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField(blank=True)
	slug = models.CharField(max_length=100, blank=True)
	favorite_songs = models.ManyToManyField('tracks.Track', related_name='favorite_tracks', blank=True)

	def es_pharrel(self):
		return self.id == 1

	def __unicode__(self):
		return self.first_name
