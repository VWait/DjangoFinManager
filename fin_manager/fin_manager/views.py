from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('/finance/wallet/')
    return redirect('home/')


def home(request):
    return render(request, 'no_auth.html')
