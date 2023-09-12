class UlamekZwykly:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise Exception("Mianownik musi być różny od zera.")

        self.__licznik = licznik
        self.__mianownik = mianownik
        self.__dzielnik = self.najmniejszy_wspolny_dzielnik()

    def wyswietl(self):
        print(f"Licznik: {self.__licznik}, mianownik: {self.__mianownik} \n"
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
        if self.__mianownik == 0:
            print("Niewłaściwy ułamek - nie da się dzielić przez zero.\n"
                  "Wpisz właściwy ułamek")
            return 0

    def zamiana_na_ulamek_dziesietny(self):
        try:
            dziesietny = self.__licznik/self.__mianownik
            dziesietny = round(dziesietny, 2)
            return dziesietny
        except ZeroDivisionError:
            print("Niewłaściwy ułamek - nie da się dzielić przez zero")
            return "Nie istnieje"

    def najmniejszy_wspolny_dzielnik(self):  # Jeśli istnieje najmniejszy wspólny dzielnik to go zwraca, jeśli nie to False
        minimum = min(self.__licznik, self.__mianownik)
        for __dzielnik in range(minimum, 1, -1):
            if self.__licznik % __dzielnik == 0 and self.__mianownik % __dzielnik == 0:
                return __dzielnik
        return 0

    def czy_podzielny(self):
        if self.najmniejszy_wspolny_dzielnik() > 1:
            return True
        else:
            return False

    def zwroc_skrocony(self, wyswietlanie_napisu=True):
        if self.czy_podzielny():
            self.__licznik = self.__licznik / self.__dzielnik
            self.__mianownik = self.__mianownik / self.__dzielnik
            self.komunikat(wyswietlanie_napisu)
            return self.__licznik, self.__mianownik
        self.komunikat(wyswietlanie_napisu)
        return self.__licznik, self.__mianownik

    def komunikat(self, wyswietlanie_napisu=True):
        if self.__dzielnik > 0:
            if wyswietlanie_napisu:
                print("Po skróceniu: ", end="")
        elif self.__dzielnik == 0:
            if wyswietlanie_napisu:
                print("Nie da się skrócić.")

    def zwroc_licznik(self):
        return self.__licznik

    def zwroc_mianownik(self):
        return self.__mianownik
