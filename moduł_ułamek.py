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

    def skroc(self):
        self.licznik, self.mianownik = self.zwroc_skroc()

    def zwroc_skroc(self):
        minimum = min(self.licznik, self.mianownik)
        for i in range(minimum, 1, -1):
            if self.licznik % i == 0 and self.mianownik % i == 0:  # Jeśli da się skrócić
                licznik = self.licznik / i
                mianownik = self.mianownik / i
                print("Po skróceniu: ", end="")
                return licznik, mianownik
        print("Nie da się skrócić: ", end="")
        return self.licznik, self.mianownik


class DzialaniaNaUlamkach:
    def __init__(self, Pierwszy_ulamek, Drugi_ulamek):
        self.Pierwszy_ulamek = Pierwszy_ulamek
        self.Drugi_ulamek = Drugi_ulamek

    @staticmethod
    def wyswietlanie(licznik, mianownik):
        print(f"Licznik: {licznik}, mianownik: {mianownik}")

    def dodaj(self):
        licznik = self.Pierwszy_ulamek.licznik + self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik + self.Drugi_ulamek.mianownik
        print("Po dodaniu: ")
        return licznik, mianownik

    def odejmij(self):
        licznik = self.Pierwszy_ulamek.licznik - self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik - self.Drugi_ulamek.mianownik
        print("Po odjęciu: ")
        return licznik, mianownik

    def mnoz(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.licznik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.mianownik
        print("Po pomnożeniu: ")
        return licznik, mianownik

    def dziel(self):
        licznik = self.Pierwszy_ulamek.licznik * self.Drugi_ulamek.mianownik
        mianownik = self.Pierwszy_ulamek.mianownik * self.Drugi_ulamek.licznik
        print("Po podzieleniu: ")
        return licznik, mianownik


if __name__ == "__main__":
    Pierwszy_ulamek = Ulamek()  # Tworzenie obiektu ułamek
    Pierwszy_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    if Pierwszy_ulamek.sprawdz_ulamek() == 0:  # Sprawdzanie wartości od użytkownika (mianownik != 0)
        Pierwszy_ulamek.użytkownik_input()  # Wartość niepoprawna = ponowne wpisanie wartości
    Pierwszy_ulamek.skroc()  # Do skrócenia ułamka
    Pierwszy_ulamek.wyswietl()  # Do wyświetlenia skróconego ułamka
    print(f"Ułamek dzisiętny: {Pierwszy_ulamek.ulamek_dziesietny()}\n")

    Drugi_ulamek = Ulamek()  # Tworzenie obiektu ułamek
    Drugi_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    if Drugi_ulamek.sprawdz_ulamek() == 0:  # Sprawdzanie wartości od użytkownika
        Drugi_ulamek.użytkownik_input()  # Wartość niepoprawna = ponowne wpisanie wartości
    Pierwszy_ulamek.skroc()  # Do skrócenia ułamka
    Pierwszy_ulamek.wyswietl()  # Do wyświetlenia skróconego ułamka
    print(f"Ułamek dziesiętny: {Drugi_ulamek.ulamek_dziesietny()}\n")

    Działanie1 = DzialaniaNaUlamkach(Pierwszy_ulamek, Drugi_ulamek)  # Tworzenie obiektu

    Wynik_dodawania = Ulamek(*Działanie1.dodaj())
    print(f"Ułamek dziesiętny: {Wynik_dodawania.ulamek_dziesietny()}")

    Wynik_odejmowania = Ulamek(*Działanie1.odejmij())
    print(f"Ułamek dziesiętny: {Wynik_odejmowania.ulamek_dziesietny()}")

    Wynik_mnożenia = Ulamek(*Działanie1.mnoz())
    print(f"Ułamek dziesiętny: {Wynik_mnożenia.ulamek_dziesietny()}")

    Wynik_dzielenia = Ulamek(*Działanie1.dziel())
    print(f"Ułamek dziesiętny: {Wynik_dzielenia.ulamek_dziesietny()}")

#  Zabezpieczyć sytuację gdy po dodaniu lub odjęciu mianowników wychodzi zero - co wtedy metoda ma robić
#  Nie wyświetlać ułamka, jeśli nie udało się go skrócić



# Zamiana licznika i mianownika II ułamka, aby funkcja sprawdź ułamek była uniwersalna
# template = self.Drugi_ulamek.licznik  # Przechowuję licznik II w pomocniczej zmiennej
# self.Drugi_ulamek.licznik = self.Drugi_ulamek.mianownik  # Nadpisuje mianownik na licznik
# self.Drugi_ulamek.licznik = template  # Nadpisuję wartość z pomocniczej zmiennej na licznik