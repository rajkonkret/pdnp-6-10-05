# klasa - przepis, szablon
# pola - np.: name
# funkcje -
# obiekt - instancja klasy, obiekt zbudowany na podstawie klasy (przepisu)

# deklaracja klasy - tu nic się nie wykona
class Human:
    """
    Klasa Human definiująca człowiek w Pythonie
    """


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
