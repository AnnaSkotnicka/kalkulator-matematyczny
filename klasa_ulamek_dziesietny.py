from klasa_ulamek_zwykly import UlamekZwykly


class UlamekDziesietny:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    @staticmethod
    def uzytkownik_input():
        wartosc = float(input("Ułamek dziesiętny: "))
        return UlamekDziesietny(wartosc)

    def zamien_na_ulamek_zwykly(self, mianownik=10):  # Gdy działanie będzie złożone z ulamków zwyklych i dziesietnych to program bedzie operowal na ulamkach zwyklych
        reszta = (self.wartosc * mianownik) % 1

        if reszta == 0:
            licznik = int(self.wartosc * mianownik)
            return UlamekZwykly(licznik, mianownik)

        return self.zamien_na_ulamek_zwykly(mianownik * 10)
