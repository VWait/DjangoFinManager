from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context=context)
