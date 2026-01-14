# 🎬 Czary Mary - Moja Kolekcja Filmów (Filweb Style)

Nowoczesna aplikacja webowa napisana w Django do zarządzania domową biblioteką filmów. Projekt posiada unikalny, ciemny interfejs inspirowany platformami VOD (Dark Mode).

## ✨ Główne Funkcjonalności

* **🌑 Nowoczesny Interfejs:** Ciemny motyw z czerwonymi akcentami.
* **📂 Pełny CRUD:**
    * **Dodawanie:** Formularz do dodawania filmów wraz z plakatami i oceną.
    * **Edycja:** Możliwość zmiany danych i podmiany plakatu.
    * **Usuwanie:** Bezpieczne usuwanie filmów z potwierdzeniem.
* **🖼️ Obsługa Mediów:** Wgrywanie i wyświetlanie plakatów filmowych.
* **⭐ System Ocen:** Możliwość oceniania filmów w skali 1-10.
* **🔍 Wyszukiwarka:** Filtrowanie listy filmów po tytule w czasie rzeczywistym.
* **artInteraktywna Lista (Akordeon):**
    * Widok zwinięty: Tytuł + podgląd plakatu po najechaniu myszką.
    * Widok rozwinięty (po kliknięciu): Pełny opis, duży plakat, reżyser i przyciski akcji.

## 🛠 Technologie

* **Backend:** Python 3.11, Django 5.x
* **Baza danych:** SQLite
* **Frontend:** HTML5, CSS3 (Custom), JavaScript (Vanilla)
* **Obsługa obrazów:** Pillow

## 🚀 Jak uruchomić projekt?

1.  **Sklonuj repozytorium:**
    ```bash
    git clone [https://github.com/TWOJA-NAZWA/twoje-repo.git](https://github.com/TWOJA-NAZWA/twoje-repo.git)
    cd nazwa-repo
    ```

2.  **Zainstaluj wymagane biblioteki:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Jeśli nie masz pliku requirements.txt, zainstaluj ręcznie: `pip install django Pillow`)*

3.  **Przygotuj bazę danych:**
    ```bash
    python manage.py migrate
    ```

4.  **Uruchom serwer:**
    ```bash
    python manage.py runserver
    ```

Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`

## 📸 Zrzuty ekranu
*(Tutaj możesz wrzucić te screeny, które mi pokazywałeś, np. folderu screenshots)*
