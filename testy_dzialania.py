import pytest
from klasa_dzialania_na_ulamkach_zwyklych import DzialaniaNaUlamkachZwyklych
from klasa_ulamek_zwykly import UlamekZwykly
from klasa_ulamek_dziesietny import UlamekDziesietny


class TestDzialania:
    @pytest.mark.parametrize("licznik1, mianownik1, licznik2, mianownik2, n_licznik1, n_licznik2, n_mianownik",
                             [
                                 (2, 3, 5, 7, 14, 15, 21),
                                 (2, 7, 1, 7, 2, 1, 7),
                                 (0, 6, 1, 7, 0, 6, 42),
                                 (-5, 6, 4, 5, -25, 24, 30)
                             ])
    def test_rozszerz_ulamek(self, licznik1, mianownik1, licznik2, mianownik2, n_licznik1, n_licznik2, n_mianownik):
        dzialanie1 = DzialaniaNaUlamkachZwyklych(UlamekZwykly(licznik1, mianownik1), UlamekZwykly(licznik2, mianownik2))

        assert dzialanie1.rozszerz_ulamek() == (n_licznik1, n_licznik2, n_mianownik)

    @pytest.fixture
    def dane(self):
        dzialanie1 = DzialaniaNaUlamkachZwyklych(UlamekZwykly(2, 3), UlamekZwykly(4, 5))
        dzialanie2 = DzialaniaNaUlamkachZwyklych(UlamekZwykly(-5, 6), UlamekZwykly(4, 5))
        return dzialanie1, dzialanie2

    def test_dodaj(self, dane):
        wynik1, wynik2 = dane[0].dodaj(), dane[1].dodaj()
        assert (wynik1.zwroc_licznik(), wynik1.zwroc_mianownik()) == (22, 15)
        assert (wynik2.zwroc_licznik(), wynik2.zwroc_mianownik()) == (-1, 30)

    def test_odejmij(self, dane):
        wynik1, wynik2 = dane[0].odejmij(), dane[1].odejmij()
        assert (wynik1.zwroc_licznik(), wynik1.zwroc_mianownik()) == (-2, 15)
        assert (wynik2.zwroc_licznik(), wynik2.zwroc_mianownik()) == (-49, 30)

    def test_mnoz(self, dane):
        wynik1, wynik2 = dane[0].mnoz(), dane[1].mnoz()
        assert (wynik1.zwroc_licznik(), wynik1.zwroc_mianownik()) == (8, 15)
        assert (wynik2.zwroc_licznik(), wynik2.zwroc_mianownik()) == (-20, 30)

    def test_dziel(self, dane):
        wynik1, wynik2 = dane[0].dziel(), dane[1].dziel()
        assert (wynik1.zwroc_licznik(), wynik1.zwroc_mianownik()) == (10, 12)
        assert (wynik2.zwroc_licznik(), wynik2.zwroc_mianownik()) == (-25, 24)
