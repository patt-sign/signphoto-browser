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
  

W repozytorium znajduje się pełny, otwarty kod źródłowy aplikacji w pliku `signphoto_browser.pyw`.

Plik `signphoto_browser.exe` to skompilowana wersja tego kodu, która jest dostępna do pobrania przez użytkowników signphoto.pl

Plik `.exe` został przeskanowany w serwisie VirusTotal i jest wolny od złośliwego oprogramowania — szczegóły skanu można znaleźć w raporcie bezpieczeństwa powyżej.

   
# Raport bezpieczeństwa pliku `signphoto_browser.exe`

Niniejszy dokument potwierdza, że plik **`signphoto_browser.exe`** został gruntownie przebadany pod kątem obecności złośliwego oprogramowania.

## Wyniki skanowania VirusTotal

Plik został przesłany do serwisu [VirusTotal](https://www.virustotal.com) i poddany analizie przez ponad 70 różnych programów antywirusowych.

- **Hash pliku:** `1ce50087f92179c9a324db9ca4425c8df52cdd621e38a8d1e5c3e2f97f2fc01a`  
- **Data skanowania:** 2 sierpnia 2025  
- **Wynik:** 0/70 programów antywirusowych wykryło jakiekolwiek zagrożenie.

## Charakterystyka projektu

- Projekt jest **otwartoźródłowy**, a pełny kod źródłowy znajduje się publicznie dostępny na GitHubie pod adresem:  
  [https://github.com/patt-sign/signphoto-browser](https://github.com/patt-sign/signphoto-browser)  
- Kod jest udostępniony na licencji MIT, co pozwala każdemu na przeglądanie, analizę oraz modyfikację programu.  
- Plik `.exe` jest skompilowaną wersją tego właśnie kodu.

## Podsumowanie

Dzięki publicznemu repozytorium kodu oraz wynikom niezależnego skanowania VirusTotal, użytkownicy i firmy antywirusowe mogą mieć pewność, że **`signphoto_browser.exe` jest bezpieczny i nie zawiera złośliwego oprogramowania**.
