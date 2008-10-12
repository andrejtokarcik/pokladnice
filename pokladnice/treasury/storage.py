from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage


class TreasuryStorage(FileSystemStorage):
    """Treasury storage system."""

    megabyte = 1024 ** 2

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        self.location = location
        self.limit = long(limit * self.megabyte)  # converting megabytes to bytes

    def get_used_space(self):
        """Retuns the amount of used space within storage."""
        from models import UploadedFile

        total_size = 0
        for file in UploadedFile.objects.all():
            total_size += file.size
        return total_size
