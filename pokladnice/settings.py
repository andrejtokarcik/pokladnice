# Django settings for pokladnice project.

try:
    from config import *
except ImportError:
    import sys
    sys.stderr.write("Error: Config file not found\n")
    sys.exit(1)

from os import path
PROJECT_ROOT = path.join(path.dirname(path.abspath(__file__)))

# Processing some options fetched from config
MEDIA_ROOT = path.join(PROJECT_ROOT, MEDIA_ROOT)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'pokladnice.urls'

TEMPLATE_DIRS = (
    path.join(PROJECT_ROOT, 'templates/')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'pokladnice.treasury',
)


AUTH_PROFILE_MODULE = 'user.userprofile'
LOGIN_URL = '/prihlaseni'
LOGIN_REDIRECT_URL = '/'
DEFAULT_FILE_STORAGE = 'pokladnice.treasury.storage.TreasuryStorage'
FILE_UPLOAD_PERMISSIONS = 0644
