from distutils.command.upload import upload
from unittest import result
from django import forms

from neuralnetwork.models import ImgUpload  

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImgUpload
        fields = ['file']