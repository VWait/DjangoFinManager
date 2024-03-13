from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('postuser/', views.post_user, name='post_user'),
]
