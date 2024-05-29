Robert Mikoś
s26294

# PPY-Projekt Tic-Tac-Toe
Opis:

Program Tic-Tac-Toe to gra konsolowa umożliwiająca rozgrywkę pomiędzy dwoma graczami lub graczem i komputerem. Jednakże posiada ona dodatkową regułę: na planszy każdy zawodnik może mieć maksymalnie 3 symbole, a więc przy każdym kolejnym ruchu w tym samym momencie zostanie usunięty z planszy najwcześniej wykonany ruch. W turze, w której jest usuwany symbol, nie można wykonać ruchu w jego miejsce. Pole jednak staję się już dostępne od kolejnej tury przeciwnika.

Wymagania:

- tryb gry: gracz vs komputer oraz gracz vs gracz,
- co każdy ruch pokazywana jest plansza z obecną sytuacją na polu,
- podczas każdego ruch, gracz widzi, poprzez podkreślenie, który symbol zniknie po wykonaniu swojego ruchu,
- gracz wygrywa poprzez ułożenie swoich symboli w jednym rzędzie, kolumnie lub na przekątnej,
- gracz ma możliwość ustawienia wyglądów symboli,
- w menu istnieje opcja z wyświetleniem zasad gry,
- walidacja poprawności wprowadzonych danych oraz komunikaty o błędach, np. ustawienie takich samych symboli, wykonanie nieprawdiłowego ruchu oraz że dane pole jest już zajęte przez inny symbol.

Struktura programu:

- main.py: Plik główny uruchamiający program.
- board.py: Moduł zarządzający stanem planszy oraz sprawdzaniem warunków wygranej.
- player.py: Moduł reprezentujący gracza.
- computer.py: Moduł reprezentujący komputer.
