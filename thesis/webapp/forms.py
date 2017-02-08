from .models import RawData_Weather
from django import forms

class UploadCSVFile(forms.Form):
    csvfile = forms.FileField()
