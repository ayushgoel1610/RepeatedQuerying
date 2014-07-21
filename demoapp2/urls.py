from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#     url(r'^$', index, name='index'),
#     url(r'^count$', countapi, name='countapi'),
#     url(r'^bargraph$', bargraph, name='bargraph'),
#     url(r'^buildingwise$', buildingwise, name='buildingwise'),
#     url(r'^peoplewise$', peoplewise, name='peoplewise'),
#     url(r'^samplewebsite$', samplewebsite, name='samplewebsite'),
#     url(r'^tabledata$', tabledata, name='tabledata'),
#     url(r'^query/(?P<change>.+)$', try1, name='try1'),
     url(r'^halfhour/(?P<param>.+)$', halfhour_single, name='halfhour_single'),
     url(r'^halfhour_day/(?P<param>.+)$', halfhour_day, name='halfhour_day'),
     url(r'^day/(?P<param>.+)$', day_single, name='day_single'),
     url(r'^day_month/(?P<param>.+)$', day_month, name='day_month'),
     url(r'^month/(?P<param>.+)$', month_single, name='month_single'),
     url(r'^month_year/(?P<param>.+)$', month_year, name='month_year'),
     url(r'^halfhour_particularday/(?P<day>.+)/(?P<dt1>.+)/(?P<dt2>.+)$', halfhour_particularday, name='halfhour_particularday'),
     url(r'^halfhour_any_month/(?P<month>.+)/(?P<year>.+)$', halfhour_any_month, name='halfhour_any_month'),
     url(r'^halfhour_any_week/(?P<week>.+)/(?P<month>.+)/(?P<year>.+)/(?P<t11>.+)/(?P<t12>.+)$', halfhour_any_week, name='halfhour_any_week'),
     url(r'^day_custom/(?P<d1>.+)/(?P<d2>.+)$', day_custom, name='day_custom'),
    # url(r'^demoapp2/', include('demoapp2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
