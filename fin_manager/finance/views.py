from django.shortcuts import render

from .models import Buffer
from .forms import CategoryForm


def wallet(request):
    """Заглушка"""
    return render(request, 'journal.html')
