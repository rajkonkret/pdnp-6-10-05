wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>
wiek2 = 37, 5  # to nie jest float!
print(type(wiek2))  # <class 'tuple'>

print(5 * wiek)  # 235
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # wynik typu float
# 95128
# 2071
# -1977
# 0.023221343873517788

print(rok // wiek)  # 43 - częśc całkowita dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia wynik 3
print(5 % 2)  # 1 bo 2 * 2 = 4 + 1 = 5
print(type((5 % 2)))  # <class 'int'>
print(wiek ** rok)
# policzyc ile ma cyfr ta liczba
# len()
print(len(str(wiek ** rok)))  # 3385 cyfr

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0 float
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# przy liczbach typu float występuje błąd zaokrąglenia
print(f"{0.2 + 0.7:.1f}")  # 0.9

print(f"Sprawdzanie zmiennej {temp} {wiek}")  # Sprawdzanie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda lub fałsz
# True False
czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))  # <class 'bool'> - typ logiczny
# prawda - 1, fałsz - 0
print(int(czy_znasz_python))  # True = 1
print(int(False))  # False = 0
x = 1  # True
print(bool(x))  # bool() - rzutwnanie na typ logiczny
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = 0
print(bool(x))  # False
x = "Radek"
print(bool(x))  # True
x = ''
print(bool(x))  # False
x = None  # nic, stan nieokreślony - null
print(bool(x))  # False

# działania logiczne
# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# True
# False
# False
# False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
# True
# True
# True
# False

# not - negacja
print(not False)
print(not True)
# True
# False

x = 0
print(not x == 1)  # True, == porównanie

a = 8
b = 6
print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # porównanie (dwa znaki równa ==)
print(f"Porównanie {a} != {b}", a != b)  # != - czy rózne, True gdy rózne, # Porównanie 8 != 6 True
print(f"Porównanie {a} >= {b}", a >= b)
print(f"Porównanie {a} <= {b}", a <= b)
# Porównanie 8 > 6 True
# Porównanie 8 < 6 False
# Porównanie 8 == 6 False
# Porównanie 8 != 6 True
# Porównanie 8 >= 6 True
# Porównanie 8 <= 6 False
