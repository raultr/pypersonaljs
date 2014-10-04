from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('userprofiles.views',
    # Examples:
    # url(r'^$', 'pypersonaljs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'','signup', name='signup'),
)