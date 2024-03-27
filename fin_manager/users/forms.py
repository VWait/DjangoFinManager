from django import forms

from django.contrib.auth import authenticate

from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    __user = None

    def clean(self):
        cleaned_data = super().clean()

        login = cleaned_data.get('login', '')
        password = cleaned_data.get('password', '')

        print(login, password)

        self.__user = authenticate(username=login, password=password)

        if self.__user is None:
            raise ValidationError('Неверный логин или пароль!')

        return cleaned_data

    def get_user(self):
        return self.__user
