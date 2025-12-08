from django.shortcuts import render
from .models import Film

def filmy_lista(request):
    filmy = Film.objects.all() 
    return render(request, 'kolekcja/filmy_lista.html', {'filmy': filmy})