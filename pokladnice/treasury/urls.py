from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from treasury.views import main, upload, profile

urlpatterns = patterns('',
    (r'^$', redirect_to, {'url': '/pokladnice'}),
    (r'^pokladnice$', main),
    (r'^pokladnice/uzivatel/(?P<username>[a-zA-Z0-9._-]+)$', profile)
)
