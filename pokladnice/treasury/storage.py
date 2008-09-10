import os

from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

class TreasuryStorage(FileSystemStorage):
    """Treasury storage system"""

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        self.location = os.path.abspath(location)

        self.limit = limit * (1024 ** 2)  # converting megabytes to bytes
        self.limit_error = StorageLimitExceeded

    def _save(self, name, content):
        filename = super(self.__class__, self)._save(name, content)
        try:
            self.check_limit()
        except self.limit_error, e:
            self.delete(filename)
            raise e
        else:
            return filename

    def check_limit(self):
        """Check if the storage limit is not exceeded"""

        def get_dir_size(directory):
            dir_size = 0
            for path, dirs, files in os.walk(directory):
                for file in files:
                    dir_size += os.path.getsize(os.path.join(path, file))
                for dir in dirs:
                    dir_size += get_dir_size(os.path.join(path, dir))
            return dir_size

        dir_size = get_dir_size(self.location)
        if dir_size >= self.limit:
            raise self.limit_error(dir_size)

    def specify_location(self, str):
        self.location = self.path(str)

    def url(self, *args, **kwargs):
        pass

class StorageLimitExceeded(Exception):
    def __init__(self, actual_dir_size):
        self.dir_size = actual_dir_size
