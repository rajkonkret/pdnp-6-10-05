# lista - kolekcja, przechowuje wiwle danych, różnego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów do listy

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Zenek")
print(lista)  # ['Radek', 'Maciek', 'Jaśko', 'Zenek']
#                   0(-4)     1(-3)    2(-2)     3(-1)
print(lista[0])  # Radek
print(lista[2])  # Jaśko
print(len(lista))  # 4 elemnty, ale ostatni indeks 3, bo od numerowane od 0
# print(lista[len(lista)])  # IndexError: list index out of range
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])  # Ostatni element z listy Zenek
print(lista[-4])  # Radek
# wypisywanie części koekcji (slicowanie)
print(lista[0:3])  # ['Radek', 'Maciek', 'Jaśko'] -> 0,1,2
print(lista[:3])  # ['Radek', 'Maciek', 'Jaśko']
print(lista[2:])  # ['Jaśko', 'Zenek']
print(lista[:])  # ['Radek', 'Maciek', 'Jaśko', 'Zenek']
print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'Maciek']
print(lista[2:3])  # ['Jaśko']
print(lista[2:10])  # ['Jaśko', 'Zenek']
print(lista[7:10])  # []
print(lista[10:10])  # []
print(lista[2:2])  # []

# nadpisanie elementu
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek']

# wstawić element we wskazene miejsce (indeks)
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek']
lista.insert(11, "Andrzej")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek', 'Andrzej']
# print(lista[11])  # IndexError: list index out of range

# usuniecie elementu (o niższym indeksie)
lista.remove("Zenek")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Andrzej']
lista.append("Radek")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Andrzej', 'Radek']
lista.remove("Radek")
print(lista)  # ['Marcin', 'Maciek', 'Mikołaj', 'Andrzej', 'Radek']

# sprawdzenie indeksu dla elementu
indeks = lista.index("Andrzej")
print(indeks)  # 3

# usunięcie elemntu po indeksie
print(lista.pop(indeks))  # Andrzej - zwraca elemnt jaki usunęła
print(lista)  # ['Marcin', 'Maciek', 'Mikołaj', 'Radek']

print(lista.pop())  # Radek - usunie ostatni element
print(lista)  # ['Marcin', 'Maciek', 'Mikołaj']

a = 1
b = 3
a = b
print(a)  # 3

b = 7
print(a)  # 3

lista2 = lista  # a = b, skopiowalismy adres pamięci (referencje)
lista_copy = lista.copy()  # kopiowanie elemntow jedej listy do drugiej
print(lista2)
print(lista)
lista.clear()  # b = 7
print(lista2)  # print(a), [], zmienilismy pod adresem pamieci dane, ten sam adres wskazuje na obie listy
print(lista)  # []
print(lista_copy)  # ['Marcin', 'Maciek', 'Mikołaj']
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 1690932007296
# 1690932007296
# 1690932328320

liczby = [54, 999, 34, 22, 12.34, 687]
# liczby = [54, 999, 34, 22, 12.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(type(liczby))  # <class 'list'>

print(liczby)  # [54, 999, 34, 22, 12.34, 687]
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999] - zmienia bazową kolekcję
print(liczby.sort())  # None

lista_osoby = ['radek', 'ola', 'agata', 'lena']
lista_osoby.sort()
print(lista_osoby)  # ['agata', 'lena', 'ola', 'radek']
lista_osoby.sort(reverse=True)  # sortuje i odwraca kolejność
print(lista_osoby)  # ['radek', 'ola', 'lena', 'agata']

liczby.reverse()  # odwrócenie listy
print(liczby)  # [999, 687, 54, 34, 22, 12.34]

liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])  # drugi od końca
print(liczby[-3:])  # [6666, 22, 12.34]

liczby.remove(54)
print(liczby)

print(liczby.pop(2))  # 6666
print(len(liczby))  # długość 4

print(liczby[0:4:2])  # [999, 22] [start:stop:krok]
print(liczby[::-1])  # wypisz odwrotnie

tekst = "Python"
lista1 = list(tekst)  # list() - rzutowanie na liste - rozpakowanie sekwencji
print(lista1)  # ['P', 'y', 't', 'h', 'o', 'n']

lista2 = [tekst]
print(lista2)  # ['Python'] dostajemy liste z elementem "Python"

liczba = 123456
# print(list(liczba))  # TypeError: 'int' object is not iterable
print([liczba])  # [123456]

krotka = tuple(liczby)  # tuple() - rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 687, 22, 12.34)
