from django.forms import Form, ModelForm, CharField, PasswordInput, TextInput
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserForm(ModelForm):
    password1 = CharField(label="Password", max_length=50, widget=PasswordInput())
    password2 = CharField(label="Password confirmation", max_length=50, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        # widgets = {
        #     'first_name': TextInput(attrs={
        #         'class': 'text-red-600 border border-red-600 px-2 py-4',
        #     })
        # }
