from django.shortcuts import render

from .forms import WalletForm


def wallet(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        value = request.POST.get("value", 0)
        print(name, value)
    form = WalletForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context=context)
