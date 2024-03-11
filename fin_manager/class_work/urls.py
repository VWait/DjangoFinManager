from django.urls import path
from . import views


urlpatterns = [
    path('messages/', views.messages, name='messages'),
    path('message/<int:id>', views.message_id, name='message_id')
]
