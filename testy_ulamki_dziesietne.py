from klasa_ulamek_dziesietny import UlamekDziesietny


class TestZamiana:
    def test_zamien_na_ulamek_zwykly(self):
        dziesietny_na_zwykly = UlamekDziesietny.zamien_na_ulamek_zwykly(UlamekDziesietny(-0.22))
        assert (dziesietny_na_zwykly.zwroc_licznik(), dziesietny_na_zwykly.zwroc_mianownik()) == (-22, 100)

        dziesietny_na_zwykly = UlamekDziesietny.zamien_na_ulamek_zwykly(UlamekDziesietny(0.457963))
        assert (dziesietny_na_zwykly.zwroc_licznik(), dziesietny_na_zwykly.zwroc_mianownik()) == (457963, 1000000)
