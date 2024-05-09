# pracownik - imie, nazwisko, pensja
# manager - imie, nazwisko, pensja, premia
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    """
    Klasa Manager dziedziczy po klasie Pracownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowlaski", 5000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Pracownik {pracownik.imie} {pracownik.nazwisko}, wynagrodzenie: {wyn_prac}")
# Pracownik Jan Kowlaski, wynagrodzenie: 5000

manago = Manager("Anna", "Nowak", 7000, 2500)
manago.przedstaw_sie()
wyn_m = manago.oblicz_pensje()
print(f"Manager {manago.imie} {manago.nazwisko}, wynagrodzenie: {wyn_m}")
# Manager Anna Nowak, wynagrodzenie: 9500
