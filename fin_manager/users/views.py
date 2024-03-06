from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User


def analytics(request):
    return render(request, 'analytics.html')


def journal(request):
    return render(request, 'journal.html')


def category(request):
    return render(request, 'category.html')


def create(request):
    user = User.objects.create_user('noadmin')
    user.save()
    return HttpResponse("""
    <p>Пользователь добавлен</p>
    <a href="/admin">Перейти в админку</a>
    """)
