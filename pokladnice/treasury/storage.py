from django.conf import settings
from django.core.files.storage import FileSystemStorage

class TreasuryStorage(FileSystemStorage):
    """Treasury storage system."""

    megabyte = 2 ** 20 # one megabyte in bytes

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        super(self.__class__, self).__init__()
        self.location = location
        self.limit = long(limit * self.megabyte) # converting megabytes to bytes

    def get_used_space(self, user):
        """Returns the amount of space used by saved files."""
        from treasury.models import FileUpload

        total_size = 0
        for file in FileUpload.objects.filter(user=user):
            total_size += file.size
        return total_size
