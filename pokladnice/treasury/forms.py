from django import forms
from django.core.files.storage import default_storage as storage
from django.utils.translation import ugettext_lazy as _

from treasury.models import FileUpload

class FileUploadForm(forms.ModelForm):
    """A form that handles the most basic upload process."""

    class Meta:
        model = FileUpload
        fields = ['file']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(self.__class__, self).__init__(*args, **kwargs)

    def clean_file(self):
        """Check file size regarding the user's storage limit."""
        newsize = storage.get_used_space(self.user) + \
                self.cleaned_data['file'].size

        if newsize > storage.limit:
            raise forms.ValidationError(_('Storage limit exceeded.'))
        else:
            return self.cleaned_data['file']

    def save(self):
        """Process and save the file to model."""
        file = self.cleaned_data['file']
        args = {}
        args['name'] = file.name
        args['size'] = file.size
        args['user'] = self.user

        upl = FileUpload(**args)
        upl.file.save(file.name, file)
        upl.save()
