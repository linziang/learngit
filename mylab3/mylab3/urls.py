from django.conf.urls import patterns, include, url
from lab3.views import *
from django.contrib import admin
#from mylab3 import settings
# Uncomment the next two lines to enable the admin:
# admin.autodiscover()

urlpatterns = patterns('',
    #('^hello/$',hello),
     url(r'^admin/', include(admin.site.urls)),
    ('^show/$',show),
    ('^search/$',search),
    ('^delete/$',delete),
    ('^click/$',click),
    # Examples:
    # url(r'^$', 'mylab3.views.home', name='home'),
    # url(r'^mylab3/', include('mylab3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
   

    # Uncomment the next line to enable the admin:
)
