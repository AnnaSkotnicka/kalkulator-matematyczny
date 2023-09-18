from klasa_ulamek_zwykly import UlamekZwykly


class DzialaniaNaUlamkachZwyklych:
    def __init__(self, pierwszy_ulamek, drugi_ulamek):
        self.pierwszy_ulamek = pierwszy_ulamek
        self.drugi_ulamek = drugi_ulamek

    def rozszerz_ulamek(self):
        if self.pierwszy_ulamek.zwroc_mianownik() == self.drugi_ulamek.zwroc_mianownik():
            return self.pierwszy_ulamek.zwroc_licznik(), self.drugi_ulamek.zwroc_licznik(), self.drugi_ulamek.zwroc_mianownik()

        # Rozszerzenie Licznika ułamka 1
        licznik_pierwszego = self.pierwszy_ulamek.zwroc_licznik() * self.drugi_ulamek.zwroc_mianownik()
        # Rozszerzenie licznika ułamka 2
        licznik_drugiego = self.drugi_ulamek.zwroc_licznik() * self.pierwszy_ulamek.zwroc_mianownik()
        # Wspólny mianownik
        mianownik = self.pierwszy_ulamek.zwroc_mianownik() * self.drugi_ulamek.zwroc_mianownik()

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
        licznik = self.pierwszy_ulamek.zwroc_licznik() * self.drugi_ulamek.zwroc_licznik()
        mianownik = self.pierwszy_ulamek.zwroc_mianownik() * self.drugi_ulamek.zwroc_mianownik()
        return UlamekZwykly(licznik, mianownik)

    def dziel(self):
        licznik = self.pierwszy_ulamek.zwroc_licznik() * self.drugi_ulamek.zwroc_mianownik()
        mianownik = self.pierwszy_ulamek.zwroc_mianownik() * self.drugi_ulamek.zwroc_licznik()
        return UlamekZwykly(licznik, mianownik)
