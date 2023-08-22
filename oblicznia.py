from klasa_ulamek_zwykly import UlamekZwykly
from klasa_dzialania_na_ulamkach import DzialaniaNaUlamkach

if __name__ == "__main__":
    Pierwszy_ulamek = UlamekZwykly()  # Tworzenie obiektu ułamek
    Pierwszy_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    # Pierwszy_ulamek.komunikat(wyswietlanie_napisu=True)
    # Pierwszy_ulamek.zwroc_skrocony()  # Do skrócenia ułamka - False nie wyświetla inf czy da się skrócić
    # print(f"Ułamek dzisiętny: {Pierwszy_ulamek.zamiana_na_ulamek_dziesietny}\n")

    Drugi_ulamek = UlamekZwykly()  # Tworzenie obiektu ułamek
    Drugi_ulamek.użytkownik_input()  # Wprowadzanie wartości przez użytkowanika
    # Drugi_ulamek.zwroc_skrocony()  # Do skrócenia ułamka
    # print(f"Ułamek dziesiętny: {Drugi_ulamek.zamiana_na_ulamek_dziesietny}\n")

    Dzialanie1 = DzialaniaNaUlamkach(Pierwszy_ulamek, Drugi_ulamek)  # Tworzenie obiektu

    Wynik_dodawania = UlamekZwykly(*Dzialanie1.dodaj())  # Gwiazdka rozdziela krotkę na dwa osobne argumenty
    # print(f"Ułamek dziesiętny: {Wynik_dodawania.zamiana_na_ulamek_dziesietny()}")

    Wynik_odejmowania = UlamekZwykly(*Dzialanie1.odejmij())
    # print(f"Ułamek dziesiętny: {Wynik_odejmowania.zamiana_na_ulamek_dziesietny}")

    Wynik_mnożenia = UlamekZwykly(*Dzialanie1.mnoz())
    # print(f"Ułamek dziesiętny: {Wynik_mnożenia.zamiana_na_ulamek_dziesietny}")

    Wynik_dzielenia = UlamekZwykly(*Dzialanie1.dziel())
    # print(f"Ułamek dziesiętny: {Wynik_dzielenia.zamiana_na_ulamek_dziesietny}")


#  Notatki

# Osobna klasa na ulamki dziesietne
# Testy
