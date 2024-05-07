# set - zbiór - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# w zbiorze nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie, zamiana na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

zb2 = set()  # tworzenei pustego zbioru
print(zb2)  # pusty set ->  set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie elementu ze zbioru za pomocą pop() - zwraca usunięty, zwraca pierwszy
print(zbior.pop())  # 33

# usunięcie po elemencie
zbior.remove(55)
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()  # kopiowanie elemntów do drugiego zbioru
print(zbior_copy)  # {66, 18, 22, 777, 11, 44} - zmienił kolejność

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# zwraca sumę zbiorów, bazowe nie zostają zmienione
print(zbior | zbior2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}
print(zbior)  # {66, 777, 11, 44, 18, 22}
print(zbior2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior.union(zbior2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62}

# część wspólna
print(zbior & zbior2)  # {18, 11, 44}

# różnica
print(zbior - zbior2)  # {777, 66, 22}
print(zbior.difference(zbior2))  # {777, 66, 22}
# {66, 777, 11, 44, 18, 22} - {999, 11, 44, 12.34, 18, 52, 667, 62} = {66, 777, 22}

# łączy zbiory - zmienia bazowy
zbior.update(zbior2)
print(zbior)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 667, 62} - zmieniony
print(zbior2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior.update(zbior2))  # None
