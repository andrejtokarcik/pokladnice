# -*- encoding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    #title = forms.CharField(label="Názov", max_length=50)
    file  = forms.FileField(label="Súbor")
