from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import UserAvatar


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    __user = None

    def clean(self):
        cleaned_data = super().clean()

        login = cleaned_data.get('login', '')
        password = cleaned_data.get('password', '')

        self.__user = authenticate(username=login, password=password)

        if self.__user is None:
            raise ValidationError('Неверный логин или пароль!')

        return cleaned_data

    def clean_login(self):
        cleaned_data = super().clean()
        login = cleaned_data.get('login', '')

        if not User.objects.filter(username=login).exists():
            raise ValidationError('логин не найден')

        return cleaned_data

    def get_user(self):
        return self.__user


class UserAvatarChangeForm(forms.ModelForm):
    class Meta:
        model = UserAvatar
        fields = ('image', )
