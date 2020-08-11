from .models import User
from django.forms import ModelForm, PasswordInput, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["login", "password"]
        widgets = {
            "login": TextInput(attrs={
                'class': 'login',
                'placeholder': 'Логин'
            }),
            "password": PasswordInput(attrs={
                'class': 'login',
                'placeholder': 'Пароль'
            })
        }