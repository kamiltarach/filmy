from django.shortcuts import render, redirect, get_object_or_404
from .models import Film
from .forms import FilmForm

def filmy_lista(request):
    szukaj = request.GET.get('szukaj') 
    
    if szukaj:
        filmy = Film.objects.filter(tytul__icontains=szukaj)
    else:
        filmy = Film.objects.all()
        
    return render(request, 'kolekcja/filmy_lista.html', {'filmy': filmy})
def nowy_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('filmy_lista')
    else:
        form = FilmForm()
    
    return render(request, 'kolekcja/filmy_form.html', {'form': form})

def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('filmy_lista')
    else:
        form = FilmForm(instance=film)

def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    
    if request.method == "POST":
        film.delete()
        return redirect('filmy_lista')
    
    return render(request, 'kolekcja/potwierdz_usun.html', {'film': film})
    
    return render(request, 'kolekcja/filmy_form.html', {'form': form})