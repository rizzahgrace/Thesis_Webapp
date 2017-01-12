from .models import RawData
from django import forms

class UploadCSVFile(forms.Form):
    csvfile = forms.FileField()
