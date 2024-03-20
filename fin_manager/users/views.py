from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context=context)
