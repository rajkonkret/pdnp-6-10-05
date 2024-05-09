class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # __ - oznacza, że pole jest prywatne, hermetyzacja

    # wystawienie metod do odczytu i zapisu wartośći pól - enkapsulacja
    def gaz(self):
        self.__predkosc += 10

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")


car1 = Car("Opel", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# Po oznaczeniu pola jako prywatne nie ma możliwosci odczytania wartości tego pola poza klasą
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 20 km/h
car1.__predkosc = 0  # dodanie pola o nazwie __predkosc o zasięgu globalnym
car1.licznik()  # Prędkość wynosi 0 km/h,
# po oznaczeniu __predkosc jako prywatne Prędkość wynosi 20 km/h
print(car1.__predkosc)  # 0
