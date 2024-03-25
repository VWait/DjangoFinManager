from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/finance/wallet/')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context=context)
