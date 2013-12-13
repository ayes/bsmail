# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
#from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('acp.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^grappelli/', include('grappelli.urls')),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	#url(r'^admin/filebrowser/', include(site.urls)),
)
