from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^get_address/$', 'koaddress.views.get_address', {}, 'koaddress-get'),
    (r'^search/$', direct_to_template, {'template': 'koaddress/search.html'}, 'koaddress-search'),
)