from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('/finance/wallet/')
    return redirect('')


def home(request):
    render(request, 'no_auth')
