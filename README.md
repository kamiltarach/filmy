# 🎬 Czary Mary - Filmowa Strona Informacyjna

Nowoczesna aplikacja webowa typu CRUD do zarządzania domową biblioteką filmów. Projekt wyróżnia się unikalnym stylem wizualnym (Glassmorphism) oraz interaktywnym interfejsem użytkownika.

![Logo](kolekcja/static/img/logo-czary.png)

## ✨ Główne Funkcjonalności

### 🎨 Design i UX
* **💎 Glassmorphism UI:** Nowoczesny interfejs z efektem półprzezroczystego, matowego szkła.
* **🌑 Cinematic Dark Mode:** Ciemny motyw z głębokim tłem i czerwonymi akcentami, idealny do przeglądania w nocy.
* **🖱️ Interaktywny Akordeon:**
    * Karty filmów domyślnie zwinięte (tytuł + dymek z plakatem po najechaniu).
    * Po kliknięciu rozwijają się szczegóły (opis, reżyser, duży plakat, ocena).

### ⚙️ Funkcje Techniczne
* **⚡ Błyskawiczne Sortowanie (JS):** Sortowanie filmów (po tytule, ocenie, dacie) odbywa się w czasie rzeczywistym bez przeładowania strony (JavaScript).
* **🔍 Wyszukiwarka:** Filtrowanie bazy danych po tytułach.
* **📂 Pełny CRUD:**
    * **Dodawanie:** Formularz z obsługą wgrywania plików (plakaty).
    * **Edycja:** Możliwość zmiany danych i podmiany zdjęć.
    * **Usuwanie:** Bezpieczne usuwanie z ekranem potwierdzenia.
* **⭐ System Ocen:** Skala 1-10 z wizualną odznaką gwiazdki.

## 🛠 Technologie

* **Backend:** Python 3.11, Django 5.x
* **Frontend:** HTML5, CSS3 (Flexbox, Backdrop-Filter), JavaScript (Vanilla)
* **Baza danych:** SQLite
* **Media:** Biblioteka `Pillow` do obsługi obrazów.

## 🚀 Instalacja i Uruchomienie

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/TWOJA-NAZWA/twoje-repo.git](https://github.com/TWOJA-NAZWA/twoje-repo.git)
    cd nazwa-repo
    ```

2.  **Zainstaluj wymagane biblioteki:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Wykonaj migracje bazy danych:**
    ```bash
    python manage.py migrate
    ```

4.  **Uruchom serwer:**
    ```bash
    python manage.py runserver
    ```

Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`

## 📸 Struktura plików (Ważne elementy)
* `kolekcja/static/css/` - Arkusze stylów (efekt szkła).
* `kolekcja/static/img/` - Pliki graficzne (tło, logo).
* `media/plakaty/` - Tutaj trafiają plakaty wgrane przez użytkownika.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/46eb245c-2594-45a3-be7f-67cd8940c44c" />

*Projekt stworzony w celach edukacyjnych - nauka frameworka Django.*