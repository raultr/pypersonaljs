from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalogos.views import CatalogoView,CatalogoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'catalogos',CatalogoViewSet)

urlpatterns = patterns('catalogos.views',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'elnuevo/','prueba_mia', name='prueba_mia'),
	url(r'api/',include(router.urls)),
	url(r'(?P<pk>[\d]+)/',CatalogoView.as_view()),
	url(r'(?P<catalogo>[\w\-\W]+)/','catalogo_view', name='catalogo_view'), 
	
	)

