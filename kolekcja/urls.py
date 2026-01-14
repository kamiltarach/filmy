from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmy_lista, name='filmy_lista'),
    path('nowy/', views.nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', views.edytuj_film, name='edytuj_film'),
    # TEJ LINIJKI BRAKUJE i dlatego jest błąd:
    path('usun/<int:id>/', views.usun_film, name='usun_film'),
]