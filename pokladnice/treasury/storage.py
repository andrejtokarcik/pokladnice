from django.conf import settings
from django.core.files.storage import FileSystemStorage

class TreasuryStorage(FileSystemStorage):
    """Treasury storage system."""

    def __init__(self, location=settings.STORAGE_LOCATION, limit=settings.STORAGE_LIMIT):
        super(TreasuryStorage, self).__init__()
        self.location = location
        self.limit = limit

    def get_used_space(self, user):
        """Returns the amount of space used by saved files."""
        from treasury.models import FileUpload

        total_size = 0
        for file in FileUpload.objects.filter(user=user):
            total_size += file.size
        return total_size
