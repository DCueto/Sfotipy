from django.db import models

from artists.models import Artist
from albums.models import Album

# Create your models here.

class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)

	def player(self):
		return """
		<audio controls>
			<source src="%s" type="audio/mpeg">
			Your browser does not support the audio tag.
		<audio/>
		""" % self.track_file.url

	player.allow_tags = True
	player.admin_order_field = 'track_file'

	def __unicode__(self):
		return self.title