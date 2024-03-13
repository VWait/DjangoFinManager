from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', required=True)
    comment = forms.CharField(label='Комментарий', required=False)
    age = forms.IntegerField(label='Возраст', initial=18)
