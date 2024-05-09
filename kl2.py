class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metodda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # Stworzyć metodę co wypisze wiek
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 56, 178, "m")
print("Imię:", cz1.imie)
print("Wiek:", cz1.wiek)
print("Wzrost:", cz1.wzrost)
print("Płeć:", cz1.plec)
# Imię: Radek
# Wiek: 56
# Wzrost: 178
# Płeć: m
cz1.powitanie()  # Nazywam się Radek
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Nazywam się Radek
# Mam 56 lat.
# Mam 178 cm wzrostu.
cz1.ruszaj()

cz2 = Human("Ania", 25, 170)
print("Imię:", cz2.imie)
print("Wiek:", cz2.wiek)
print("Wzrost:", cz2.wzrost)
print("Płeć:", cz2.plec)
cz2.ruszaj()
# Nazywam się Radek
# Mam 56 lat.
# Mam 178 cm wzrostu.
# Ruszyłem w drogę
# Imię: Ania
# Wiek: 25
# Wzrost: 170
# Płeć: k
# Ruszyłam w drogę
