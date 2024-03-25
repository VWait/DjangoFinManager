from django.shortcuts import render


def wallet(request):
    return render(request, 'journal.html')
