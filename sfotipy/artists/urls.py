from django.conf.urls import patterns, url
#from .views import LoginView
from .views import AlbumListView

urlpatterns = patterns('',
	url(r'^albums/$', AlbumListView.as_view(), name='album_list'),
	url(r'^albums/(?P<artist>[\w\-]+)/$', AlbumListView.as_view(), name='album_list'),
)	