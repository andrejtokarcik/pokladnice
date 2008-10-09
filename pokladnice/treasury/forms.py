from django import forms
from django.utils.translation import ugettext_lazy as _

class UploadFileForm(forms.Form):
    #title = forms.CharField(label=_('Title'), max_length=50)
    file  = forms.FileField(label=_('File path'))
