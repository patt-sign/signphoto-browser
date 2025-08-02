# signphoto_browser

Prosta aplikacja w Pythonie z GUI do otwierania strony [Signphoto.pl](https://signphoto.pl) oraz naprawy połączenia DNS.

---

## Funkcje

- Sprawdza i automatycznie naprawia ustawienia DNS (ustawia Google DNS 8.8.8.8 i 8.8.4.4)  
- Testuje połączenie z serwerem `signphoto.pl`  
- Udostępnia przycisk do ręcznego naprawiania połączenia  
- Połączenie działa? Możesz otworzyć stronę Signphoto w oknie przeglądarki osadzonej w aplikacji

---

## Wymagania

- Python 3.x  
- Biblioteki Python:  
  - `tkinter` (standardowa w Pythonie)  
  - `pywebview` (można zainstalować: `pip install pywebview`)

---

## Jak uruchomić

1. Upewnij się, że masz zainstalowany Python 3 i bibliotekę `pywebview`  
2. W katalogu z plikiem uruchom:  
   ```bash
   python signphoto_browser.pyw
