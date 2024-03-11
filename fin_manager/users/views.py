from django.shortcuts import render

from django.http import HttpResponse

from .models import User


def analytics(request):
    print(request.POST.get("name"))
    return render(request, 'analytics.html')


def journal(request):
    data = request.session.get("key", 0) + 1
    request.session['key'] = data
    context = {
        'messages': ['asdf', 'a']
    }
    return render(request, 'journal.html', context)


def category(request):
    request.session['key'] = 0
    return render(request, 'category.html')


def number(request, n=0, m=0):
    return HttpResponse(f"""
    <h1>{n} + {m} = {n + m}</h1>
    """)
