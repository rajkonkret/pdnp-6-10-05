dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}

# wyswietla klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietlenie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for p in dictionary.items():
    print(p)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
print("Radek", end='')  # ustawiamy znak końca lini na pusty, kolejny print pisze w tej samej linii
print("Tomek")  # RadekTomek, tu juz domyslnie znak końca linii \n
print("Następny")  # Następny

dictionary2 = {'name': 'imie', 'company': "Inny"}
d = {}
for k, v in dictionary2.items():
    d[v] = k
print(d)  # {'imie': 'name', 'Inny': 'company'}
print({value: key for key, value in dictionary2.items()})  # {'imie': 'name', 'Inny': 'company'}
