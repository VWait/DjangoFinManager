from django.shortcuts import render

from .forms import UserForm


def login(request):
    user_form = UserForm
    return render(request, 'login.html', {'form': user_form})


def post_user(request):
    name = request.POST.get("name", [])
    print(name)
    context = {
        "name": name
    }
    return render(request, 'post_user.html', context=context)