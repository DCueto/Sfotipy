from django.test import TestCase

# Create your tests here.

from .models import Artist

class TestArtists(TestCase):

	def setUp(self):
		self.artist = Artist.objects.create(first_name='David', last_name='Bowie')

	def test_existe_vista(self):
		res = self.client.get('/artists/%d/' % self.artist.id)
		self.assertEqual(res.status_code, 200)
		self.assertTrue('David' in res.content)

	def test_no_existe_vista(self):
		id_viejo = self.artist.id
		self.artist.delete()
		res = self.client.get('/artists/%d/' % id_viejo)
		self.assertEqual(res.status_code, 404)
