from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalogos/', include('catalogos.urls')),
    url(r'^catalogos_detalle/', include('catalogos_detalle.urls')),
    url(r'^signup/', include('userprofiles.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),)
