from django import forms
from django.forms import PasswordInput
from base.models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }


class UserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'login')
        widgets = {
            # 'photo': forms.ImageField(widget=forms.ImageField),
            'email': forms.TextInput(),
            'password': forms.PasswordInput(),
            'login': forms.TextInput()
        }