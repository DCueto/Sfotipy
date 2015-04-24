from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from artists.views import ArtistDetailView

admin.autodiscover()  # automatic autodiscover should be turned off in settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^signout/', 'userprofiles.views.signout', name='signout'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),

)

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
	)