from klasa_ulamek import Ulamek


class DzialaniaNaUlamkach:
    def __init__(self, Pierwszy_ulamek, Drugi_ulamek):
        self.Pierwszy_ulamek = Pierwszy_ulamek
        self.Drugi_ulamek = Drugi_ulamek

    def dodaj(self):
        licznik_pierwszego = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik  # Rozszerzenie Licznika ułamka 1
        licznik_drugiego = self.Drugi_ulamek.licznik * self.Pierwszy_ulamek.mianownik  # Rozszerzenie licznika ułamka 2

        licznik = licznik_pierwszego + licznik_drugiego
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik  # Wspólny mianownik

        Wynik = Ulamek(licznik, mianownik)
        print("Po dodaniu: ")
        Wynik.wyswietl()
        return licznik, mianownik

    def odejmij(self):
        licznik = self.Pierwszy_ulamek.licznik - self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik - self.Drugi_ulamek.mianownik
        Wynik = Ulamek(licznik, mianownik)
        print("Po odjęciu: ")
        Wynik.wyswietl()
        return licznik, mianownik

    def mnoz(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik
        Wynik = Ulamek(licznik, mianownik)
        print("Po pomnożeniu: ")
        Wynik.wyswietl()
        return licznik, mianownik

    def dziel(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.licznik
        Wynik = Ulamek(licznik, mianownik)
        print("Po podzieleniu: ")
        Wynik.wyswietl()
        return licznik, mianownik
