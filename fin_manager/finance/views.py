from django.shortcuts import render

from .forms import WalletForm
from .models import Wallet


def wallet(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        value = request.POST.get("value", 0)
        wal = Wallet(name=name, value=value, user=request.user)
        wal.save()
    form = WalletForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context=context)
