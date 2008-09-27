from django.db import models
from django.contrib.auth.models import User

def get_file_path(instance, filename):
    from os.path import join
    return join(instance.user.username, filename)

class UploadedFile(models.Model):
    file = models.FileField(upload_to=get_file_path)
    size = models.IntegerField()
    user = models.ForeignKey(User)
