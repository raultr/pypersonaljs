from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('catalogos_detalle.views',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'(?P<catalogod>[\w\-]+)/','catalogo_detalle_view', name='catalogo_detalle_view'),
)

