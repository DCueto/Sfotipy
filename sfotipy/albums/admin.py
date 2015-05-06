from django.contrib import admin
from sorl.thumbnail import get_thumbnail

from .models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'imagen_album')

	def imagen_album(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.cover, '50x50', format='PNG').url
	imagen_album.allow_tags = True

admin.site.register(Album, AlbumAdmin)