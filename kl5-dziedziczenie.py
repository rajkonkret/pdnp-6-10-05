# dzidziczenie
# przejęcie cech innej klasy, nadpisanie, modyfikacja, rozszerzenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    """
    Klasa Samochód
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)  # obowiązkowo musimy wywołac konstruktor klasy wyższej (super)
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołać metode z klasy wyższej super
        print(f"Marka: {self.marka}")


poj = Pojazd("Czerwony")
poj.info()  # Kolor: Czerwony

sam = Samochod("Zielony")
sam.info()  # Kolor: Zielony
# Kolor: Zielony
# Marka: None

sam2 = Samochod("Czerwony", "Ferrari")
sam2.info()
# Kolor: Czerwony
# Marka: Ferrari

# polimorfizm - możliwośc wykorzystania cech wspólnych dla obiektów róznych klas ale dziedziczących po wspólnej klasie
lista = [poj, sam, sam2]
for i in lista:
    i.info()

# Kolor: Czerwony
# Kolor: Zielony
# Marka: None
# Kolor: Czerwony
# Marka: Ferrari
