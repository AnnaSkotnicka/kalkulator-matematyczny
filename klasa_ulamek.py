class Ulamek:
    def __init__(self, licznik = 1, mianownik = 1):
        self.licznik = licznik
        self.mianownik = mianownik

    def wyswietl(self):
        print(f"Licznik: {self.licznik}, mianownik: {self.mianownik}")

    def użytkownik_input(self):
        self.licznik = int(input("Licznik: "))
        self.mianownik = int(input("Mianownik: "))
        print(f"Licznik: {self.licznik}, mianownik: {self.mianownik}")
        if self.sprawdz_ulamek() == 0:  # sprawdzanie czy ułamek jest poprawny
            self.użytkownik_input()  # Jeśli nie to ponownie wprowadź dane

    def sprawdz_ulamek(self):
        if self.mianownik == 0:
            print("Niewłaściwy ułamek - nie da się dzielić przez zero.\n"
                  "Wpisz właściwy ułamek")
            return 0

    def ulamek_dziesietny(self):
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

    def czy_podzielny(self,  wyswietlanie_napisu=True):
        if self.najmniejszy_wspolny_dzielnik() > 1:
            self.komunikat(wyswietlanie_napisu)
            return True
        else:
            self.komunikat(wyswietlanie_napisu)
            return False

    def zwroc_skrocony(self):
        if self.czy_podzielny():
            dzielnik = self.najmniejszy_wspolny_dzielnik()
            self.licznik = self.licznik / dzielnik
            self.mianownik = self.mianownik / dzielnik
            self.wyswietl()
            return self.licznik, self.mianownik
        return self.licznik, self.mianownik

    def komunikat(self, wyswietlanie_napisu=True):
        if self.najmniejszy_wspolny_dzielnik() > 0:
            if wyswietlanie_napisu:
                print("Po skróceniu: ", end="")
        elif self.najmniejszy_wspolny_dzielnik() == 0:
            if wyswietlanie_napisu:
                print("Nie da się skrócić.")

