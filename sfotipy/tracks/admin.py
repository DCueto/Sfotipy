from django.contrib import admin

from .models import Track
from actions import export_as_excel

class TrackAdmin(admin.ModelAdmin):

	list_display = ('title', 'artist', 'album', 'order', 'listen', 'player', 'es_pharrel')
	list_filter = ('artist', 'album')
	search_fields = ('title', 'artist__first_name', 'artist__last_name')
	list_editable = ('artist', 'album')
	actions = (export_as_excel,)
	raw_id_fields = ('artist',)

	def es_pharrel(self, obj):
		return obj.id == 1

	es_pharrel.boolean = True

# Register your models here.

admin.site.register(Track, TrackAdmin)