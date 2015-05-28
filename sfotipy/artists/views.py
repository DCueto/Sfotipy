from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic.detail import DetailView
from rest_framework import viewsets
from django.views.generic import ListView, DetailView
from albums.models import Album
from .models import Artist
from .serializers import ArtistSerializer
from userprofiles.mixins import LoginRequiredMixin

# Mixins

class JsonResponseMixin(object):
	def response_handler(self):
		format = self.request.GET.get('format', None)
		if format == 'json':
			return self.json_to_response()

		context = self.get_context_data()
		return self.render_to_response(context)

	def json_to_response(self):
		data = self.get_data()
		return JsonResponse(data, safe=False)

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

# Albums Views - Need to replace to albums app

class AlbumListView(LoginRequiredMixin, JsonResponseMixin, ListView):
	model = Album
	template_name = 'album_list.html'
	#paginate_by = 2

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		return self.response_handler()

	def get_data(self):
		data = list()
		for album in self.object_list:
			data.append({
				'cover': album.cover.url,
				'title': album.title,
				'slug': album.slug,
				'artist': album.artist.nickname,
			})
		return data

	def get_queryset(self):
		if self.kwargs.get('artist'):
			#Devolver albumes de artista
			queryset = self.model.objects.filter(artist__slug__contains=self.kwargs.get('artist'))
		else:
			queryset = super(AlbumListView, self).get_queryset()

		return queryset

class AlbumDetailView(LoginRequiredMixin, JsonResponseMixin, DetailView):
	model = Album
	template_name = 'album_detail.html'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return self.response_handler()

	def get_data(self):
		data = {
			'album':{
				'cover': self.object.cover.url,
				'title': self.object.title,
				'slug': self.object.slug,
				'artist': self.object.artist.nickname,
				'tracks': [t.title for t in self.object.track_set.all()]
			}
		}
		return data
