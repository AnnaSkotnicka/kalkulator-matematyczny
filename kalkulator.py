import moduł_ułamek
import modul_funkcja_kwadratowa

co_zrobic = input("Jeśli chcesz obliczyć miejsca zerowe funkcji kwadratowej wpisz miejsca zrowe\n"
                  "Jeśli chcesz wykonać działania na ułamkach wpisz ułamki\n")

match co_zrobic:
    case "miejsca zerowe":
        Funkcja1 = modul_funkcja_kwadratowa.FunkcjaKwadratowa()
        Funkcja1.rozwiaz()
    case "ułamki":
        Pierwszy_ulamek = moduł_ułamek.DzialaniaNaUlamkach(2, 5)
        Drugi_ulamek = moduł_ułamek.DzialaniaNaUlamkach(7, 9)
        działanie = input("\nWpisz działanie z poniższej listy, które chcesz wykonać: \ndodawanie"
                          "\nodjemowanie\nmnozenie\ndzielenie\n")
        match działanie:
            case dodawanie:
                moduł_ułamek.DzialaniaNaUlamkach(4,6)
                Pierwszy_ulamek.dodaj()



# Funkcja1 = FunkcjaKwadratowa.FunkcjaKwadratowa()
# Funkcja1.rozwiaz()