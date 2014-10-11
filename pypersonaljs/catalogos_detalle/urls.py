from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalogos_detalle.views import CatalogoDetallesViewSet 
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register(r'catalogos_detalle',CatalogoDetallesViewSet)

urlpatterns = patterns('catalogos_detalle.views',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'api/',include(router1.urls)),
    url(r'(?P<catalogod>[\w\-]+)/','catalogo_detalle_view', name='catalogo_detalle_view'),
)

