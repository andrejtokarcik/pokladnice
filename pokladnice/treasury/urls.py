from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('treasury.views',
    url(r'^$', 'index', name='treasury-index'),
    url(r'^(?P<username>\w+)/profil/$', 'profile', name='treasury-profile'),
    url(r'^smazat/(?P<id>\d+)/$', 'delete', name='treasury-file-delete')
)
