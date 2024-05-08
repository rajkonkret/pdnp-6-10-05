# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliwośc deklaracji w miejscu użycia
from functools import reduce


def odejmij2(a, b):
    return a - b


print(odejmij2(4, 5))

odejmij = lambda a, b: a - b  # # return jest domyślny
print(odejmij(4, 5))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 3, 24, 50, 100, 500]
# wypisaniu wartości z tej listy pomnożnych przez 2

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 48, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 48, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 48, 100, 200, 1000]

# funkcje wyższego rzędu

# map() - pobiera element z kolekcji, wykonuje zaddanie podane funkcją
print(f"Zastosowanie map(): {list(map(zmien, lista))}")  # Zastosowanie map(): [2, 4, 6, 48, 100, 200, 1000]
# zastosowanie lambdy jako funkcji anonimowej
# zdefiniowana w miejscu wykonania
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map(): [2, 4, 6, 48, 100, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")  # Zastosowanie map(): [4, 8, 12, 96, 200, 400, 2000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - pobiera elemnt, sprawdza czy spełnia warunek, zwraca gdy spełnia
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
# x > 20, x > 50, x > 3 i x < 50
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 20, lista))}")  # Zastosowanie filter(): [24, 50, 100, 500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 50, lista))}")  # Zastosowanie filter(): [100, 500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 50, lista))}")  # Zastosowanie filter(): [24]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 50, lista))}")  # Zastosowanie filter(): [24]

# reduce()
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5)
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lista_reduce))  # 15
# wynik poprzedniego działania + kolejny element kolekcji
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(reduce(lambda a, b: a * b, lista_reduce))  # 120
# 1 * 2 = 2
# 2 * 3 = 6
# 6 + 4 = 24
# 24 * 5 = 120
