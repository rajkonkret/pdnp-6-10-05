# while - sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komuniak!!!")
    if licznik > 10:
        break

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print('Komunikat2 !! !! !!')

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['1', '2', '3', '4', '5', '78', '90', '0']  str
# [1, 2, 3, 4, 5, 78, 90, 0]  int
