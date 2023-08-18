from klasa_ulamek import Ulamek
from klasa_dzialania_na_ulamkach import DzialaniaNaUlamkach

if __name__ == "__main__":
    Pierwszy_ulamek = Ulamek()  # Tworzenie obiektu ułamek
    Pierwszy_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    if Pierwszy_ulamek.sprawdz_ulamek() == 0:  # Sprawdzanie wartości od użytkownika (mianownik != 0)
        Pierwszy_ulamek.użytkownik_input()  # Wartość niepoprawna = ponowne wpisanie wartości
    Pierwszy_ulamek.zwroc_skrocony(True)  # Do skrócenia ułamka - False nie wyświetla inf czy da się skrócić
    print(f"Ułamek dzisiętny: {Pierwszy_ulamek.ulamek_dziesietny()}\n")

    Drugi_ulamek = Ulamek()  # Tworzenie obiektu ułamek
    Drugi_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    if Drugi_ulamek.sprawdz_ulamek() == 0:  # Sprawdzanie wartości od użytkownika
        Drugi_ulamek.użytkownik_input()  # Wartość niepoprawna = ponowne wpisanie wartości
    Drugi_ulamek.zwroc_skrocony()  # Do skrócenia ułamka
    Drugi_ulamek.wyswietl()  # Do wyświetlenia skróconego ułamka
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