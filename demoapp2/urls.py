from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', index, name='index'),
     url(r'^count$', countapi, name='countapi'),
     url(r'^bargraph$', bargraph, name='bargraph'),
     url(r'^buildingwise$', buildingwise, name='buildingwise'),
     url(r'^peoplewise$', peoplewise, name='peoplewise'),
     url(r'^samplewebsite$', samplewebsite, name='samplewebsite'),
     url(r'^tabledata$', tabledata, name='tabledata'),
    # url(r'^demoapp2/', include('demoapp2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
