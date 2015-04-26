from rest_framework import serializers

from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artist
		fields = ('id', 'first_name', 'last_name', 'es_pharrel')