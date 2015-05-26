from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'artist'
	template_name = 'artist.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artists'
	template_name = 'artist.html'

class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	filter_fields = ('id',)
	paginate_by = 1

from django.views.generic import ListView
from albums.models import Album

class AlbumListView(ListView):
	model = Album
	template_name = 'album_list.html'
	paginate_by = 2

	def get_queryset(self):
		if self.kwargs.get('artist'):
			#Devolver albumes de artista
			queryset = self.model.objects.filter(artist__slug__contains=self.kwargs.get('artist'))
		else:
			queryset = super(AlbumListView, self).get_queryset()

		return queryset
