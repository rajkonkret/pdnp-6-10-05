from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opsująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatuek):
        super().__init__(gatuek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać:)")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("kieer kier kir")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa dziedziczy po klasie Ptak
    """


# Po oznaczeniu klasy jako abstrakcyjna, nie można tworzyć obiektów tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł Bielik", 45)
# or1.latam()  # Tu Orzeł Bielik Lecę z szybkością 45
# or1.wydaj_odglos()
#
# kur1 = Ptak("Kura Domowa", 0)
# kur1.latam()  # Tu Kura Domowa Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura Domowa")
kur2.latam()  # Tu Kura Domowa Ja nie latam
kur2.wydaj_odglos()  # ko ko ko ko

or2 = Orzel("Orzeł Bielik", 55)
or2.latam()
or2.wydaj_odglos()
# Tu Kura Domowa Ja nie latam
# ko ko ko ko
# Tu Orzeł Bielik Lecę z szybkością 55
# kieer kier kir

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# bo klasa Sowa nie nadpisuje metody wydaj_odglos()
# sowa1 = Sowa("Sowa", 15)
or2.poluj()  # Tu Orzeł Bielik Rozpoczynam polowanie
kur2.dziobanie()  # Tu Kura Domowa Idę sobie podziobać:)
