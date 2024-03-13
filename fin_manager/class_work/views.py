from django.shortcuts import render

from .models import Message


def messages(request):
    messages = Message.objects.all()
    titles = list(map(lambda x: x.title, messages))
    context = {
        'titles': titles
    }
    return render(request, 'messages.html', context=context)


def message_id(request, id=0):
    messages = Message.objects.all()
    if not 0 <= id < len(messages):
        title = messages[0].title
    else:
        title = messages[id].title
    context = {
        'title': title
    }
    return render(request, 'message_id.html', context=context)
