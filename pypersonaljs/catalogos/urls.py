from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalogos.views import CatalogoView
urlpatterns = patterns('catalogos.views',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

  #  url(r'(?P<catalogo>[\w\-\W]+)/','catalogo_view', name='catalogo_view'),   
    url(r'(?P<pk>[\d]+)/',CatalogoView.as_view()),

)

