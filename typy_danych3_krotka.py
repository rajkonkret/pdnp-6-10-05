# krotka - kolekcja, jest niemutowalna
# krotka jednoelementowa - zmiennej - niezmienna (stała)

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>
tupla_names = ("Radek", "Tomek", "Asia", "Zbyszek", "Marek")
print(type(tupla_names))  # <class 'tuple'>
print(tupla_names)  # ('Radek', 'Tomek', 'Asia', 'Zbyszek', 'Marek')
tupla_names2 = "Radek", "Tomek", "Asia", "Zbyszek", "Marek"
print(type(tupla_names2))  # <class 'tuple'>
tupla_3 = ("Radek",)  # PEP8 zaleca tuple jednoelemntowa z nawaiasami
print(type(tupla_3))  # <class 'tuple'>
tupla_4 = "Radek",
print(type(tupla_4))  # <class 'tuple'>
print(tupla_4)  # ('Radek',)

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla_liczby[0] = 2  # TypeError: 'tuple' object does not support item assignment

print(tupla_names.count("Tomek"))  # 1
print(tupla_names.index("Tomek"))  # 1
print(sorted(tupla_names))  # sortowanie tupli daje liste ['Asia', 'Marek', 'Radek', 'Tomek', 'Zbyszek']

a, b = 1, 2
print(a)
print(b)

# rozpakowanie tupli
# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * worek na pozostałe dane
print(a)  # 1
print(b)  # [2, 3]

imie, *imie2, imie3 = tupla_names
print(imie, imie2, imie3)  # Radek ['Tomek', 'Asia', 'Zbyszek'] Marek

*imie, imie2, imie3 = tupla_names
print(imie, imie2, imie3)
# ['Radek', 'Tomek', 'Asia'] Zbyszek Marek


imie, imie2, *imie3 = tupla_names
print(imie, imie2, imie3)
# Radek Tomek ['Asia', 'Zbyszek', 'Marek']

lista = list(tupla_names)
print(lista)  # ['Radek', 'Tomek', 'Asia', 'Zbyszek', 'Marek']
print(type(lista))  # <class 'list'>
