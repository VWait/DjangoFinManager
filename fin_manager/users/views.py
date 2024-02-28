from django.shortcuts import render

from random import randint


def users(request):
    context = {
        'number': randint(1, 100)
    }
    return render(request, 'table.html', context)
