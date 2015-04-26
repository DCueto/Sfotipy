import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Track
from .serializers import TrackSerializer

# Create your views here.

@login_required
def track_view(request, title):

	'''	try:
		track = Track.objects.get(title=title)
	except Track.DoesNotExist:
		raise Http404 '''

	track = get_object_or_404(Track, title=title) 
	bio = track.artist.biography

	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': bio
		}
	}
	#json_data = json.dumps(data)

	
	#return HttpResponse(json_data, content_type='application/json')

	return render(request, 'track.html', {'track': track, 'bio': bio})

from rest_framework import viewsets

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
