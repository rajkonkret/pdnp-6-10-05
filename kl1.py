# klasa - przepis, szablon
# pola - np.: name
# funkcje -
# obiekt - instancja klasy, obiekt zbudowany na podstawie klasy (przepisu)

# deklaracja klasy - tu nic się nie wykona
class Human:
    """
    Klasa Human definiująca człowiek w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


# tworzenie obiektu kalsy Human
cz1 = Human()
print(type(cz1))  # <class '__main__.Human'>
print(cz1)  # <__main__.Human object at 0x000002AB7CDB1A30>
print(Human.__doc__)  # wypisanie dokumentacji
#     Klasa Human definiująca człowiek w Pythonie
print(print.__doc__)
# pydoc -b
# pydoc -w kl1 - generowanie pliku html z dokumntacja dla tego pliku
# python -m pydoc
print("imię", cz1.imie)
print("płeć", cz1.plec)
print("wiek", cz1.wiek)
# imię
# płeć k
# wiek None

cz1.imie = "Ania"
cz1.wiek = 36
print("imię", cz1.imie)
print("płeć", cz1.plec)
print("wiek", cz1.wiek)
# imię Ania
# płeć k
# wiek 36

# stwórzcie obiekt innej płci, nadać imie, wiek, płeć
# wyświetlić jakie ma parametry

cz2 = Human()
cz2.plec = "m"
cz2.imie = "Zenek"
cz2.wiek = 65
print("imię", cz2.imie)
print("płeć", cz2.plec)
print("wiek", cz2.wiek)
# imię Zenek
# płeć m
# wiek 65
