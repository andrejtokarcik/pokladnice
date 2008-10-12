
### Pokladnice specific settings
# Maximum amount of storage for a user (in megabytes)
STORAGE_LIMIT = 5

# Directory where uploaded files will be stored
STORAGE_LOCATION = '/var/tmp'

### Webtests
# on which port to run cherrypy server, used to wrap webtests
# must be same as in URL_ROOT 
CPSERVER_PORT = 8000

# on which port is your selenium server running
SELENIUM_PORT = 4444

# selenium browser command, as specified in seenium docs
# usually: *firefox, *iexplore, *konqueror, *opera
# on *nix with firefox, you must usually specify path to firefox bin
SELENIUM_BROWSER_COMMAND = '*firefox'

### Django settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     # ('Almad', 'bugs at almad.net'),
)
MANAGERS = ADMINS

URL_ROOT = "http://localhost:8000/"

SITE_ID = 1

# Database settings:
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'pokladnice'
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''
DATABASE_OPTIONS = {"init_command": "SET storage_engine=INNODB" } 

TIME_ZONE = 'Europe/Prague'
LANGUAGE_CODE = 'cs'
FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'
USE_I18N = True

MEDIA_ROOT = "media"  # will be prepended with the project root
MEDIA_URL = "/media/"
ADMIN_MEDIA_PREFIX = "/adminmedia/"

SECRET_KEY = 'dxg%z*wf$0m^=3a_c9b=j_kd!zy^c1yj*(g^4yajn*!9^a&bxcqwp0'
