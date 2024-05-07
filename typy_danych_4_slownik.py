# słownik - para klucz wartość
# {'klucz':'wartość'}
# json - słownik jest odpowiednikiem jsona
# klucz może wystąpić tylko raz

# pusty słownik - tworzennie i wypisywanie
dictionary = dict()
print(dictionary)  # {} - pusty słownik
dictionary1 = {}
print(dictionary1)
print(type(dictionary))  # <class 'dict'>
print(type(dictionary1))  # <class 'dict'>

# dodanie elemntu do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

# nadpisanie - gdy klucz juz istnieje
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Tomek', 39])
# dict_items([('imie', 'Tomek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('imie'))  # Tomek
print(dictionary.get('Imie', 'default'))  # default

tekst = input("Wpisz tekst")  # input() - pobiera dane np.: od użytkownika
print(tekst)  # tekst wpisany przez Radka

# napisac aplikacje słownik polsko - angielski
# załadować słownik danymi
# wypisac klucze ze słownika
# pobrac od uzytkownika słowo do przetłumaczenia
# wypisać ze słownika wartośc dla tego klucza
