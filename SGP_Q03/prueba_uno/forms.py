__author__ = 'penagonzalez'
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

# Se establecen dos instancias ModelForm diferentes

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) # con PasswordInput se oculta la contrasenha

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'cedula')  #jojo