 import modul_funkcja_kwadratowa

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        print(f'licznik: {self.licznik}, mianownik: {self.mianownik}')

    def ulamek_dziesietny(self):
        dziesietny = self.licznik/self.mianownik
        dziesietny = round(dziesietny, 2)
        return f"Ułamek dziesiętny: {dziesietny}"

class DzialaniaNaUlamkach:
    def __init__(self, Pierwszy_ulamek, Drugi_ulamek):
        self.Pierwszy_ulamek = Pierwszy_ulamek
        self.Drugi_ulamek = Drugi_ulamek
        print(f'licznik: {self.Pierwszy_ulamek}, mianownik: {self.Drugi_ulamek}')

    def skroc(self):
        przedział = min(self.licznik, self.mianownik)
        for i in range(przedział + 1, 2, -1):
            if self.licznik % i == 0 and self.mianownik % i == 0:
                licznik = self.licznik / i
                mianownik = self.mianownik / i
                print("Ułamek skrócony: ")
                return Pierwszy_ulamek.wyswietlanie(licznik, mianownik)

    @staticmethod
    def wyswietlanie(licznik, mianownik):
        print(f"Licznik: {licznik}, mianownik: {mianownik}")

    def dodaj(self):
        licznik = self.licznik + Drugi_ulamek.licznik
        mianownik = self.mianownik + Drugi_ulamek.mianownik
        print("Po dodaniu: ")
        wynik = DzialaniaNaUlamkach(licznik, mianownik)
        return wynik

    def odejmij(self):
        licznik = Pierwszy_ulamek.licznik - Drugi_ulamek.licznik
        mianownik = Pierwszy_ulamek.mianownik - Drugi_ulamek.mianownik
        print("Po odjęciu: ")
        wynik = DzialaniaNaUlamkach(licznik, mianownik)
        return wynik

    def mnoz(self):
        licznik = Pierwszy_ulamek.licznik * Drugi_ulamek.licznik
        mianownik = Pierwszy_ulamek.mianownik * Drugi_ulamek.mianownik
        print("Po mnoz: ")
        wynik = DzialaniaNaUlamkach(licznik, mianownik)
        return wynik

    def dziel(self):
        try:
            licznik = Pierwszy_ulamek.licznik * Drugi_ulamek.mianownik
            mianownik = Pierwszy_ulamek.mianownik * Drugi_ulamek.licznik
            print("Po podzieleniu: ")
            wynik = DzialaniaNaUlamkach(licznik, mianownik)
        except ZeroDivisionError:
            print("Nie da się podzielić przez zero")


if __name__ == "__main__":
    Pierwszy_ulamek = Ulamek(2, 5)
    print(Pierwszy_ulamek.ulamek_dziesietny())

    Drugi_ulamek = Ulamek(7, 9)
    print(Drugi_ulamek.ulamek_dziesietny())



# Pierwszy_ulamek.skroc()
# Pierwszy_ulamek.dodaj()
# Pierwszy_ulamek.odejmij()
# Pierwszy_ulamek.mnoz()
# Pierwszy_ulamek.dziel()


#  wpisywanie obu ułamków przez użytkownika