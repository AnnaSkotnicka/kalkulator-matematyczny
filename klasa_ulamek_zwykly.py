class UlamekZwykly:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.dzielnik = self.najmniejszy_wspolny_dzielnik()

    def wyswietl(self):
        print(f"Licznik: {self.licznik}, mianownik: {self.mianownik} \n"
              f"Dziesiętny: {self.zamiana_na_ulamek_dziesietny()}")

    @staticmethod
    def użytkownik_input():
        licznik = int(input("Licznik: "))
        mianownik = int(input("Mianownik: "))

        if mianownik == 0:  # sprawdzanie, czy ułamek jest poprawny
            print("Niewłaściwy ułamek - nie da się dzielić przez zero.\n"
                  "Wpisz właściwy ułamek")
            return UlamekZwykly.użytkownik_input()  # Jeśli nie to ponownie wprowadź dane

        return UlamekZwykly(licznik, mianownik)

    def sprawdz_ulamek(self):
        if self.mianownik == 0:
            print("Niewłaściwy ułamek - nie da się dzielić przez zero.\n"
                  "Wpisz właściwy ułamek")
            return 0

    def zamiana_na_ulamek_dziesietny(self):
        try:
            dziesietny = self.licznik/self.mianownik
            dziesietny = round(dziesietny, 2)
            return dziesietny
        except ZeroDivisionError:
            print("Niewłaściwy ułamek - nie da się dzielić przez zero")
            return "Nie istnieje"

    def najmniejszy_wspolny_dzielnik(self):  # Jeśli istnieje najmniejszy wspólny dzielnik to go zwraca, jeśli nie to False
        minimum = min(self.licznik, self.mianownik)
        for dzielnik in range(minimum, 1, -1):
            if self.licznik % dzielnik == 0 and self.mianownik % dzielnik == 0:
                return dzielnik
        return 0

    def czy_podzielny(self):
        if self.najmniejszy_wspolny_dzielnik() > 1:
            return True
        else:
            return False

    def zwroc_skrocony(self, wyswietlanie_napisu=True):
        if self.czy_podzielny():
            self.licznik = self.licznik / self.dzielnik
            self.mianownik = self.mianownik / self.dzielnik
            self.komunikat(wyswietlanie_napisu)
            return self.licznik, self.mianownik
        self.komunikat(wyswietlanie_napisu)
        return self.licznik, self.mianownik

    def komunikat(self, wyswietlanie_napisu=True):
        if self.dzielnik > 0:
            if wyswietlanie_napisu:
                print("Po skróceniu: ", end="")
        elif self.dzielnik == 0:
            if wyswietlanie_napisu:
                print("Nie da się skrócić.")
