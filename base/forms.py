from django import forms
from base.models import Users
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'password', 'login')
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'})
        }


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'password', 'login')
        widgets = {
            'email': forms.TextInput(),
            'password': forms.PasswordInput(),
            'login': forms.TextInput()
        }

