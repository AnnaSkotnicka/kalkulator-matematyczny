from klasa_ulamek_zwykly import UlamekZwykly


class DzialaniaNaUlamkach:
    def __init__(self, Pierwszy_ulamek, Drugi_ulamek):
        self.Pierwszy_ulamek = Pierwszy_ulamek
        self.Drugi_ulamek = Drugi_ulamek

    def rozszerz_ulamek(self):
        licznik_pierwszego = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik  # Rozszerzenie Licznika ułamka 1
        licznik_drugiego = self.Drugi_ulamek.licznik * self.Pierwszy_ulamek.mianownik  # Rozszerzenie licznika ułamka 2
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik  # Wspólny mianownik

        return licznik_pierwszego, licznik_drugiego, mianownik

    def dodaj(self):
        licznik_pierwszego, licznik_drugiego, mianownik = self.rozszerz_ulamek()
        licznik = licznik_pierwszego + licznik_drugiego
        Wynik = UlamekZwykly(licznik, mianownik)
        print("Po dodaniu: ")
        Wynik.zwroc_skrocony(False)  # Argument False - odpowiada za nie wyświetlanie informacji czy ułamek jest skrócony
        Wynik.wyswietl()  # Wyświetla nowy licznik i mianownik
        return licznik, mianownik

    def odejmij(self):
        licznik_pierwszego, licznik_drugiego, mianownik = self.rozszerz_ulamek()
        licznik = licznik_pierwszego - licznik_drugiego
        Wynik = UlamekZwykly(licznik, mianownik)
        print("Po odjęciu: ")
        Wynik.zwroc_skrocony(False)
        Wynik.wyswietl()
        return licznik, mianownik

    def mnoz(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik
        Wynik = UlamekZwykly(licznik, mianownik)
        print("Po pomnożeniu: ")
        Wynik.zwroc_skrocony(False)
        Wynik.wyswietl()
        return licznik, mianownik

    def dziel(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.licznik
        Wynik = UlamekZwykly(licznik, mianownik)
        print("Po podzieleniu: ")
        Wynik.zwroc_skrocony(False)
        Wynik.wyswietl()
        return licznik, mianownik
