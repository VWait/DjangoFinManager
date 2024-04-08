from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import UserAvatar


class SignInForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    __user = None

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')

        self.__user = authenticate(username=username, password=password)

        if self.__user is None:
            raise ValidationError('Неверный логин или пароль!')

        return cleaned_data

    def get_user(self):
        return self.__user


class UserAvatarChangeForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = ('image', )
