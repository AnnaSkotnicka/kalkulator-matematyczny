from klasa_ulamek import Ulamek
from klasa_dzialania_na_ulamkach import DzialaniaNaUlamkach
import klasa_funkcja_kwadratowa

co_zrobic = input("Jeśli chcesz obliczyć miejsca zerowe funkcji kwadratowej wpisz miejsca zrowe\n"
                  "Jeśli chcesz wykonać działania na ułamkach wpisz ułamki\n")

match co_zrobic:
    case "miejsca zerowe":
        Funkcja1 = klasa_funkcja_kwadratowa.FunkcjaKwadratowa()
        Funkcja1.rozwiaz()
    case "ułamki":
        Pierwszy_ulamek = DzialaniaNaUlamkach(2, 5)
        Drugi_ulamek = DzialaniaNaUlamkach(7, 9)
        działanie = input("\nWpisz działanie z poniższej listy, które chcesz wykonać: \ndodawanie"
                          "\nodjemowanie\nmnozenie\ndzielenie\n")
        match działanie:
            case dodawanie:
                Ulamek(4,6)
                Pierwszy_ulamek.dodaj()



# Funkcja1 = FunkcjaKwadratowa.FunkcjaKwadratowa()
# Funkcja1.rozwiaz()