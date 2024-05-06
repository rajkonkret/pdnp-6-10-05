import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.1100001  # zmiennoprzecinkowy - float
liczba = 123456789123  # int

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300, str_digits_check_threshold=640)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# w tym sposobie sprawdza typy
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
print("witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, "wiek": wiek})  # witaj Tomek, masz teraz 39 lat.
print("witaj %(user)s, masz teraz %(age)d lat." % {'user': user, "age": wiek})  # witaj Tomek, masz teraz 39 lat.

# tu nie sprawdza typu
print("Witaj {}, masz teraz {} lat.".format(user, wiek))
print("Witaj {}, masz teraz {} lat.".format(wiek, user))
# Witaj Tomek, masz teraz 39 lat.
# Witaj 39, masz teraz Tomek lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat. f- f-string

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3.11)  # Używamy wersji Pythona 3.110000
print("Używamy wersji Pythona %.1f" % 3.11)  # Używamy wersji Pythona 3.1
print("Używamy wersji Pythona %.2f" % 3.11)  # Używamy wersji Pythona 3.11
# Przy wypisywaniu liczb zaokrągla
print("Używamy wersji Pythona %.0f" % 3.11)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("Nadal x się nie zmieniła", x)  # Nadal x się nie zmieniła 3.14

y = round(x)  # zaokrąglenie w sensie matematycznym
print("y=", y)  # y= 3
print(x)  # 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.1100001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.1
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 3
print(f"Używamy wersji Pythona {3.9:.0f}")  # Używamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^10}")  # "  Tomek   "
print(f"{user}")  # "Tomek"

print(liczba)  # 123456789123 - int
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 123,456,789,123
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 123.456.789.123
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 123 456 789 123

print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 123,456,789,123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
# Nasza duża liczba 123 456 789 123
# Nasza duża liczba 123.456.789.123

liczba2 = 123_345_678_900
print(liczba2)  # 123345678900
print(f"Nasza duża liczba2 {liczba2:,}".replace(",", "."))  # Nasza duża liczba2 123.345.678.900
