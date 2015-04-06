from django.contrib import admin

from .models import Artist
from tracks.models import Track
from albums.models import Album

# Register your models here.

class TrackInline(admin.StackedInline):
	model = Track
	extra = 1

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 0

class ArtistAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name',)
	inlines = [AlbumInline, TrackInline,]

admin.site.register(Artist, ArtistAdmin)