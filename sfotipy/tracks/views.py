from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Track

# Create your views here.

def track_view(request, title):

	'''	try:
		track = Track.objects.get(title=title)
	except Track.DoesNotExist:
		raise Http404 '''

	track = get_object_or_404(Track, title=title) 
	bio = track.artist.biography



	return render(request, 'track.html', {'track': track, 'bio': bio})