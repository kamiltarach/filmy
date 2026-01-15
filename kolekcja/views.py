from django.shortcuts import render, redirect, get_object_or_404
from .models import Film
from .forms import FilmForm
from django.db.models.functions import Lower # <--- TO JEST NOWY IMPORT

# 1. Widok listy filmów (z ulepszonym sortowaniem)
def filmy_lista(request):
    szukaj = request.GET.get('szukaj')
    sortuj = request.GET.get('sortuj')
    
    filmy = Film.objects.all()

    # Filtrowanie (Wyszukiwarka)
    if szukaj:
        filmy = filmy.filter(tytul__icontains=szukaj)

    # Sortowanie
    if sortuj == 'tytul_asc':
        # Lower('tytul') sprawia, że 'Avatar' i 'avatar' są traktowane tak samo
        filmy = filmy.order_by(Lower('tytul')) 
    elif sortuj == 'ocena_desc':
        filmy = filmy.order_by('-ocena')
    elif sortuj == 'ocena_asc':
        filmy = filmy.order_by('ocena')
    elif sortuj == 'data_asc':
        filmy = filmy.order_by('id')
    else:
        # Domyślnie: najnowsze dodane na górze
        filmy = filmy.order_by('-id')

    return render(request, 'kolekcja/filmy_lista.html', {'filmy': filmy})

# ... (Reszta funkcji: nowy_film, edytuj_film, usun_film zostaje bez zmian) ...
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
    return render(request, 'kolekcja/filmy_form.html', {'form': form})

def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect('filmy_lista')
    return render(request, 'kolekcja/potwierdz_usun.html', {'film': film})