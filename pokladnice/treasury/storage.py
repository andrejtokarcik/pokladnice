import os

from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

__all__ = ['TreasuryStorage', 'StorageLimitExceeded']

class TreasuryStorage(FileSystemStorage):
    """Treasury storage system"""

    megabyte = 1024 ** 2

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        self.location = os.path.abspath(location)
        self.limit = long(limit * self.megabyte)  # converting megabytes to bytes
        self.limit_error = StorageLimitExceeded
        self._specified = False

    def _save(self, name, content):
        filename = super(self.__class__, self)._save(name, content)

        if (self.limit - self.get_used_space()) < 0:
            self.delete(filename)
            raise self.limit_error(self.get_used_space())
        else:
            return filename

    def specify_location(self, str):
        if not self._specified:
            self.location = self.path(str)
        self._specified = True
        return True  # hack because of the storage_location decorator

    def get_used_space(self):
        """
        Retuns the amount of used space within storage
        """

        def get_dir_size(directory):
            # http://pcheruku.wordpress.com/2008/09/08/python-code-to-get-directory-size/
            dir_size = 0
            for path, dirs, files in os.walk(directory):
                for file in files:
                    dir_size += os.path.getsize(os.path.join(path, file))
                for dir in dirs:
                    dir_size += get_dir_size(os.path.join(path, dir))
            return dir_size
        return get_dir_size(self.location)

class StorageLimitExceeded(Exception):
    def __init__(self, actual_dir_size):
        self.dir_size = actual_dir_size
