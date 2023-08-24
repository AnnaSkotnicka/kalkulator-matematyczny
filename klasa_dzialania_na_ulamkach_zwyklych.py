from klasa_ulamek_zwykly import UlamekZwykly


class DzialaniaNaUlamkachZwyklych:
    def __init__(self, pierwszy_ulamek, drugi_ulamek):
        self.pierwszy_ulamek = pierwszy_ulamek
        self.drugi_ulamek = drugi_ulamek

    def rozszerz_ulamek(self):
        licznik_pierwszego = self.pierwszy_ulamek.licznik * self.drugi_ulamek.mianownik  # Rozszerzenie Licznika ułamka 1
        licznik_drugiego = self.drugi_ulamek.licznik * self.pierwszy_ulamek.mianownik  # Rozszerzenie licznika ułamka 2
        mianownik = self.pierwszy_ulamek.mianownik * self.drugi_ulamek.mianownik  # Wspólny mianownik

        return licznik_pierwszego, licznik_drugiego, mianownik

    def dodaj(self):
        licznik_pierwszego, licznik_drugiego, mianownik = self.rozszerz_ulamek()
        licznik = licznik_pierwszego + licznik_drugiego
        return UlamekZwykly(licznik, mianownik)

    def odejmij(self):
        licznik_pierwszego, licznik_drugiego, mianownik = self.rozszerz_ulamek()
        licznik = licznik_pierwszego - licznik_drugiego
        return UlamekZwykly(licznik, mianownik)

    def mnoz(self):
        licznik = self.pierwszy_ulamek.licznik * self.drugi_ulamek.licznik
        mianownik = self.pierwszy_ulamek.mianownik * self.drugi_ulamek.mianownik
        return UlamekZwykly(licznik, mianownik)

    def dziel(self):
        licznik = self.pierwszy_ulamek.licznik * self.drugi_ulamek.mianownik
        mianownik = self.pierwszy_ulamek.mianownik * self.drugi_ulamek.licznik
        return UlamekZwykly(licznik, mianownik)


#  Użyć operatorów przeciążenia