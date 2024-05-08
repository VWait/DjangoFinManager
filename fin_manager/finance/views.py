from django.shortcuts import render

from .models import Buffer
from .forms import CategoryForm


def wallet(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # form.save()
            pass
    else:
        form = CategoryForm()
    buffer = Buffer.get_buffer_by_user(request.user)
    context = {
        'incomes': [category.get_fields_for_table() for category in buffer.get_categories_income()],
        'expenses': [category.get_fields_for_table() for category in buffer.get_categories_expenses()],
        'buffer': buffer,
        'form': form
    }
    return render(request, 'journal.html', context=context)
