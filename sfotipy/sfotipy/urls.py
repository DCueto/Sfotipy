from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

from artists.views import ArtistDetailView, ArtistListView, ArtistViewSet
from albums.views import AlbumViewSet
from tracks.views import TrackViewSet

admin.autodiscover()  # automatic autodiscover should be turned off in settings

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    url(r'admin/password_reset/done$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^signout/', 'userprofiles.views.signout', name='signout'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
    url(r'^artists/', ArtistListView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', include('userprofiles.urls')),

)

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
	)