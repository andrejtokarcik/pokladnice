from django import forms
from django.core.files.storage import default_storage as storage
from django.utils.translation import ugettext_lazy as _

from models import UploadedFile

class UploadFileForm(forms.ModelForm):
    """
    A form that handles the most basic upload process.
    """

    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        """
        Check file size regarding the storage limit.
        """
        newsize = storage.get_used_space() + self.cleaned_data['file'].size
        if newsize > storage.limit:
            raise forms.ValidationError(_('Storage limit exceeded'))
        else:
            return self.cleaned_data['file']

