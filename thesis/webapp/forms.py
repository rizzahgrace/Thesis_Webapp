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

class recordOwner(forms.ModelForm):
    last_name = forms.CharField(
        label="Last Name",
        required=True,
    )

    first_name = forms.CharField(
        label="First Name",
        required=True,
    )

    address = forms.CharField(
        label="Address",
        required=True,
    )

    class Meta:
        model = Owner
        fields = ['last_name','first_name','address']

class recordUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {'password': forms.PasswordInput()}
