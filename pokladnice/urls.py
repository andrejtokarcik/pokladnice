from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

from pokladnice import treasury
from pokladnice.settings import MEDIA_ROOT

urlpatterns = patterns('',
    # static files in media dir
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

    (r'^', include('treasury.urls')),

    (r'^prihlaseni', login, {'template_name': 'login.html'}),
    (r'^odhlaseni', logout, {'template_name': 'logout.html'}),
)
