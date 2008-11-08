import os

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

def get_file_path(instance, filename):
    return os.path.join(instance.user.username, filename)

class FileUpload(models.Model):
    file = models.FileField(_('File path'), upload_to=get_file_path)
    name = models.CharField(_('File name'), max_length=50)
    size = models.IntegerField()

    user = models.ForeignKey(User)

    class Meta:
        db_table = 'treasury_file_upload'
