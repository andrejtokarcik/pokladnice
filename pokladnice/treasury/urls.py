from django.conf.urls.defaults import *
from views import main, profile

urlpatterns = patterns('',
    (r'^$', main),
    (r'^uzivatel/(?P<username>[a-zA-Z0-9._-]+)', profile)
)
