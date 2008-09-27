from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage

__all__ = ['TreasuryStorage', 'StorageLimitExceeded']

class TreasuryStorage(FileSystemStorage):
    """Treasury storage system"""

    megabyte = 1024 ** 2

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        self.location = location
        self.limit = long(limit * self.megabyte)  # converting megabytes to bytes
        self.limit_error = StorageLimitExceeded

    def check_limit(self, file):
        size = self.get_used_space() + file.size
        if (self.limit - size) < 0:
            raise self.limit_error(size)

    def get_used_space(self):
        """
        Retuns the amount of used space within storage
        """
        from models import UploadedFile

        total_size = 0
        for file in UploadedFile.objects.all():
            total_size += file.size
        return total_size

class StorageLimitExceeded(Exception):
    def __init__(self, dir_size):
        self.dir_size = dir_size
