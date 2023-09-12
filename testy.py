import pytest
import klasa_ulamek_zwykly


class TestUlamekZwykly:
    def test_tworzenie_ulamka(self):
        assert klasa_ulamek_zwykly.UlamekZwykly(2,4)
        with pytest.raises(Exception):
            klasa_ulamek_zwykly.UlamekZwykly(2,0)
            klasa_ulamek_zwykly.UlamekZwykly(0,7)

    def test_wyswietl(self, capsys):
        ulamek = klasa_ulamek_zwykly.UlamekZwykly(2,4)

        ulamek.wyswietl()
        out, err = capsys.readouterr()
        assert out == "Licznik: 2, mianownik: 4 \nDziesiętny: 0.5\n"
