from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.views.generic.simple import redirect_to

from django.conf import settings

urlpatterns = patterns('',
    # static files in media dir
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # django user authentication (will be replaced by klicnik)
    url(r'^prihlaseni/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^odhlaseni/$', logout, {'next_page': '/'}, name='logout'),


    url(r'^$', redirect_to, {'url': '/pokladnice/'}),
    url(r'^pokladnice/', include('treasury.urls'))
)
