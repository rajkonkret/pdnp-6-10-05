# funkcje zwracające wynik
def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(7, 5))
wyn = dodaj(8, 45)
print(wyn)  # 53

print(odejmij())
print(odejmij(1))
print(odejmij(2, 3))
print(odejmij(2, 3, 4))
print(odejmij(b=8, c=9))  # -17

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=18, cena=20000))
# 1230.0
# 1080.0
# 23600.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0

if zm == 1230:
    print("Działa")

print(dodaj(6, 10) + odejmij(78, 90, 34))  # -30
