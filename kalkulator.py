from klasa_ulamek_zwykly import UlamekZwykly
from klasa_dzialania_na_ulamkach_zwyklych import DzialaniaNaUlamkachZwyklych
import klasa_funkcja_kwadratowa
from klasa_ulamek_dziesietny import UlamekDziesietny

co_zrobic = input("Jeśli chcesz obliczyć miejsca zerowe funkcji kwadratowej wpisz miejsca zrowe\n"
                  "Jeśli chcesz wykonać działania na ułamkach wpisz ułamki\n")
# co_zrobic = "ułamki dziesietne"

match co_zrobic:
    case "miejsca zerowe":
        funkcja1 = klasa_funkcja_kwadratowa.FunkcjaKwadratowa()
        funkcja1.rozwiaz()
    case "ułamki zwykle":
        pierwszy_ulamek = UlamekZwykly.użytkownik_input()
        działanie = input("Wpisz działanie z poniższej listy, które chcesz wykonać: +, -, *, /\n")
        drugi_ulamek = UlamekZwykly.użytkownik_input()
        dzialanie1 = DzialaniaNaUlamkachZwyklych(pierwszy_ulamek, drugi_ulamek)

        match działanie:
            case "+":
                wynik_dodawania = dzialanie1.dodaj()
            case "-":
                wynik_odejmowania = dzialanie1.odejmij()
            case "*":
                wynik_mnożenia = dzialanie1.mnoz()
            case "/":
                wynik_dzielenia = dzialanie1.dziel()

    case "ułamki dziesietne":
        pierwszy_dziesietny = UlamekDziesietny.uzytkownik_input()
        print(pierwszy_dziesietny)

