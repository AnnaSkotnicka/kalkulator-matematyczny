from klasa_ulamek import Ulamek


class DzialaniaNaUlamkach:
    def __init__(self, Pierwszy_ulamek, Drugi_ulamek):
        self.Pierwszy_ulamek = Pierwszy_ulamek
        self.Drugi_ulamek = Drugi_ulamek

    @staticmethod
    def wyswietlanie(licznik, mianownik):
        print(f"Licznik: {licznik}, mianownik: {mianownik}")

    def dodaj(self):
        licznik = self.Pierwszy_ulamek.licznik + self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik + self.Drugi_ulamek.mianownik
        print("Po dodaniu: ")
        return licznik, mianownik

    def odejmij(self):
        licznik = self.Pierwszy_ulamek.licznik - self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik - self.Drugi_ulamek.mianownik
        print("Po odjęciu: ")
        return licznik, mianownik

    def mnoz(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik
        print("Po pomnożeniu: ")
        return licznik, mianownik

    def dziel(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.licznik
        print("Po podzieleniu: ")
        return licznik, mianownik
