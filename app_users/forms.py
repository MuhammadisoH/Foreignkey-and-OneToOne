from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
