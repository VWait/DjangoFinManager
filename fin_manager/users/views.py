from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .forms import SignInForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/finance/wallet/')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users_signup.html', context=context)


def log_out(request):
    logout(request)
    return redirect('/home/')


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = SignInForm()
    context = {
        'form': form
    }
    return render(request, 'users_login.html', context=context)
