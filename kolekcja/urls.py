from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmy_lista, name='filmy_lista'),
]