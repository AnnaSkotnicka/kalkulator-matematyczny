from klasa_ulamek_zwykly import UlamekZwykly
from klasa_dzialania_na_ulamkach_zwyklych import DzialaniaNaUlamkachZwyklych
import klasa_funkcja_kwadratowa
from klasa_ulamek_dziesietny import UlamekDziesietny

# co_zrobic = input("Jeśli chcesz obliczyć miejsca zerowe funkcji kwadratowej wpisz miejsca zrowe\n"
#                   "Jeśli chcesz wykonać działania na ułamkach wpisz ułamki\n")
co_zrobic = "ulamki"

if co_zrobic == "miejsca zerowe":
    funkcja1 = klasa_funkcja_kwadratowa.FunkcjaKwadratowa()
    funkcja1.rozwiaz()
elif co_zrobic == "ulamki":
    jakie_ulamki = input("Jaki? zw/dz: ")
    if jakie_ulamki == "zw":
        pierwszy_ulamek = UlamekZwykly.użytkownik_input()
    elif jakie_ulamki == "dz":
        dziesietny = UlamekDziesietny.uzytkownik_input()
        pierwszy_ulamek = dziesietny.zamien_na_ulamek_zwykly()
    dzialanie = input("Wpisz działanie z poniższej listy, które chcesz wykonać: +, -, *, /\n")
    while dzialanie != "end":
        jakie_ulamki = input("Jaki? zw/dz: ")
        if jakie_ulamki == "zw":
            drugi_ulamek = UlamekZwykly.użytkownik_input()
        elif jakie_ulamki == "dz":
            dziesietny = UlamekDziesietny.uzytkownik_input()
            drugi_ulamek = dziesietny.zamien_na_ulamek_zwykly()
        dzialanie1 = DzialaniaNaUlamkachZwyklych(pierwszy_ulamek, drugi_ulamek)

        match dzialanie:
            case "+":
                wynik = dzialanie1.dodaj()
            case "-":
                wynik = dzialanie1.odejmij()
            case "*":
                wynik = dzialanie1.mnoz()
            case "/":
                wynik = dzialanie1.dziel()

        pierwszy_ulamek = wynik
        wynik.zwroc_skrocony(False)  # Argument False - odpowiada za nie wyświetlanie informacji czy ułamek jest skrócony
        print("Wynik: ", end="")
        wynik.wyswietl()  # Wyświetla nowy licznik i mianownik

        dzialanie = input("Wpisz działanie z poniższej listy, które chcesz wykonać: +, -, *, /, end\n")