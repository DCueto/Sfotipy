from django.test import TestCase

# Create your tests here.

from .models import Track
from artists.models import Artist
from albums.models import Album

class TestTracks(TestCase):

	def setUp(self):
		self.artist = Artist.objects.create(first_name='David', last_name='Bowie')
		self.album = Album.objects.create(title='Heroes', artist=self.artist)
		self.track = Track.objects.create(title='Heroes', artist=self.artist, album=self.album, order=0, track_file='media/sa')

	def test_usuario_logueado(self):
		res = self.client.get('/tracks/%s/' % self.track.title)
		self.assertEqual(res.status_code, 302)