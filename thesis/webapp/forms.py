from .models import RawData_Weather
from django import forms
from django.contrib.auth.models import User
from .models import Owner

class UploadCSVFile(forms.Form):
    csvfile = forms.FileField()
    owner = forms.ModelChoiceField(
        label="Owner",
        queryset=Owner.objects.order_by('last_name'),
        required=True,
        empty_label='Choose an owner'
    )

class recordOwner(forms.Form):
    last_name = forms.CharField(label='Last Name', max_length=50)
    first_name = forms.CharField(label='First Name', max_length=50)

class recordUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {'password': forms.PasswordInput()}
