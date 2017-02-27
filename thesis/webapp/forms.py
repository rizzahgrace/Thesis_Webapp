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
        exclude = ['AMPS_user']

class recordUser(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data