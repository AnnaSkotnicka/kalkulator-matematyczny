import pytest
import klasa_ulamek_zwykly


class TestUlamekZwykly:
    def test_tworzenie_ulamka(self):
        assert klasa_ulamek_zwykly.UlamekZwykly(2, 4)
        with pytest.raises(Exception):
            klasa_ulamek_zwykly.UlamekZwykly(2, 0)
            klasa_ulamek_zwykly.UlamekZwykly(0, 7)

    def test_wyswietl(self, capsys):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(2, 4)

        ulamek.wyswietl()
        out, err = capsys.readouterr()
        assert out == "Licznik: 2, mianownik: 4 \nDziesiętny: 0.5\n"

    @pytest.mark.parametrize("licznik, mianownik, result", [(2, 4, 0.5),
                                                            (2, 3, 0.67),
                                                            (0, 4, 0),
                                                            (9, 4, 2.25)
                                                            ])
    def test_zamiana_na_ulamek_dziesietny(self, licznik, mianownik, result):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(licznik, mianownik)
        assert ulamek.zamiana_na_ulamek_dziesietny() == result

    @pytest.mark.parametrize("licznik, mianownik, result", [(2, 4, 2),
                                                            (27, 45, 9),
                                                            (0, 4, 0),
                                                            (9, 4, 0),
                                                            (-48, 128, 16),
                                                            (48, -128, 16)
                                                            ])
    def test_najwiekszy_wspolny_dzielnik(self, licznik, mianownik, result):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(licznik, mianownik)
        assert ulamek.najwiekszy_wspolny_dzielnik() == result

    @pytest.mark.parametrize("licznik, mianownik, result", [(2, 4, True),
                                                            (3, 5, False),
                                                            ])
    def test_czy_podzielny(self, licznik, mianownik, result):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(licznik, mianownik)
        assert ulamek.czy_podzielny() == result

    @pytest.mark.parametrize("licznik, mianownik, skrocony_licznik, skrocony_mianownik", [(4, 8, 1, 2),
                                                                                          (-4, 8, 1, 2),
                                                                                          (3, 5, 3, 5),
                                                                                          ])
    def test_zwroc_skrocony(self, licznik, mianownik, skrocony_licznik, skrocony_mianownik):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(licznik, mianownik)
        assert ulamek.zwroc_skrocony() == (skrocony_licznik, skrocony_mianownik)

    def test_komunikat(self, capsys):
        ulamek1 = klasa_ulamek_zwykly.UlamekZwykly(2, 4)
        ulamek1.komunikat()
        out1, err = capsys.readouterr()
        assert out1 == "Po skróceniu: "  # Nie ma znaku nowej linii, jest end=="" w tym princie

        ulamek2 = klasa_ulamek_zwykly.UlamekZwykly(2, 5)
        ulamek2.komunikat()
        out2, err = capsys.readouterr()
        assert out2 == "Nie da się skrócić.\n"
