class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        # delta = -self.b - 4 * self.a * self.c
        delta = 0
        Funkcja1.sprawdz_ilosc_rozwiazan(delta)
        x1 = (-self.b - (delta ** (1 / 2))) / (2 * self.a)
        x2 = (-self.b + (delta ** (1 / 2))) / (2 * self.a)
        x1 = round(x1, 2)
        x2 = round(x2, 2)
        return x1, x2, delta

    @staticmethod
    def sprawdz_ilosc_rozwiazan(delta):
        if delta > 0:
            print("Funkcja ma 2 miejsce zerowe")
        elif delta == 0:
            print("Funkcja ma 1 miejsce zerowe")
        else:
            print("Brak miejsc zerowych")


Funkcja1 = FunkcjaKwadratowa((-9), 0, 1)
Funkcja1.rozwiaz()
