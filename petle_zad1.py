# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # range() - generuje liczby 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    pass
    # print(_)

for i in range(10):
    print(i * 2)

lista_kula = list(range(1, 50))

lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(f"Liczba nr: {i}: {wyn}")
    lista_wylosowane.append(wyn)
# Liczba nr: 0: 8
# Liczba nr: 1: 49
# Liczba nr: 2: 41
# Liczba nr: 3: 44
# Liczba nr: 4: 5
# Liczba nr: 5: 46
print(lista_wylosowane)  # [46, 49, 36, 24, 28, 9]

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:
    if c > 10:
        print("Większe od 10")
    print(c)

for i in range(0, 10, 2):  # start, stop, krok 0..9 co 2
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # krok ujemny, petla do tyłu
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)

# Wyświetlić z tej listy elemnty w postaci
# 0 Radek

for i in range(len(imiona)):  # range(4) 0..3
    print(i, imiona[i])

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca numer i element kolejny
for p in enumerate(imiona):
    print(p)  # (1, 'Tomek')

a, b = (1, 'Tomek')
for i, p in enumerate(imiona):
    print(i, p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

# ludzie = ['Radek', 'Asia', "Tomek", "Janek"]
ludzie = ['Radek', 'Asia', "Tomek", "Janek", "Marek"]  # IndexError: list index out of range
wiek = [44, 55, 23, 32]

# wyswietlić w postaci Radek 44
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])
# Radek 44
# Asia 55
# Tomek 23
# Janek 32

# zip() - łaczenie kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Asia', 55)
# ('Tomek', 23)
# ('Janek', 32)

for p, w in zip(ludzie, wiek):
    print(p, w)
# Radek 44
# Asia 55
# Tomek 23
# Janek 32

# wyswietlić w postaci 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (2, ('Tomek', 23))

a, b = (2, ('Tomek', 23))
print(a)  # 2
print(b)  # ('Tomek', 23)
c, d = b
print(c)  # Tomek
print(d)  # 23
# (a, (c, d)) = (2, ('Tomek', 23))
a, (c, d) = (2, ('Tomek', 23))
print(a, c, d)

for i, (p, w) in enumerate(zip(ludzie, wiek)):
    print(i, p, w)
# 0 Radek 44
# 1 Asia 55
# 2 Tomek 23
# 3 Janek 32

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000017BD6F650D0>
# for zipp in zipped:
#     print(zipp)
# # ('Radek', 44)
# # ('Asia', 55)
# # ('Tomek', 23)
# # ('Janek', 32)
# # ('Marek', None)
# print("-------")
# for zipp in zipped:
#     print(zipp)
zip_list = list(zipped)
for item in zip_list:
    print(item)

for i, w in zip_list:
    print(i, w)
# Radek 44
# Asia 55
# Tomek 23
# Janek 32
# Marek None
# praca domowa - dodanie wyswietlania indeksu
