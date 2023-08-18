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

    def skroc(self, tak_lub_nie=True):
        self.licznik, self.mianownik = self.zwroc_skrocony(tak_lub_nie)

    def zwroc_skrocony(self, tak_lub_nie = True):
        minimum = min(self.licznik, self.mianownik)
        for i in range(minimum, 1, -1):
            if self.licznik % i == 0 and self.mianownik % i == 0:  # Jeśli da się skrócić
                self.licznik = self.licznik / i
                self.mianownik = self.mianownik / i
                if tak_lub_nie:
                    print("Po skróceniu: ", end="")
                    self.wyswietl()
                return self.licznik, self.mianownik
        if tak_lub_nie:
            print("Nie da się skrócić.")
        return self.licznik, self.mianownik

    # def rozszerz_ulamek(self):


