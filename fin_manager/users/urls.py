from django.urls import path
from . import views


urlpatterns = [
    path('analytics/', views.analytics, name='analytics'),
    path('category/', views.category, name='category'),
    path('journal/', views.journal, name='journal'),
    path('number/<int:n>/<int:m>', views.number, name='number'),
]
