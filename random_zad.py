import random  # do generowania liczb pseudolosowych

print(random)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\random.py'>

# help(random)

print(random.randint(1, 100))  # int 1..100 włącznie
print(random.randrange(1, 100))  # int 1..99
print(random.randrange(7))  # int 0 .. 6
print(random.random())  # float 0.5169854883636108 od 0 do 0.999999
print(random.random() * 10)  # float 0 do 9.999999

lista = [1, 2, 3, 45, 67, 89, 90]
print(random.choice(lista))  # losuje liczbę z listy

lista_kula = list(range(1, 50))  # range() - generuje liczby od 1 do 49
# print(lista_kula)

# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))
# print(random.choice(lista_kula))

# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kula)
# lista_kula.remove(wyn)
# print(wyn)

print(random.choices(lista_kula, k=6))  # losuje z powtórzeniami [27, 43, 19, 43, 49, 48]
print(random.sample(lista_kula, 6))  # bez powtórzeń
print(random.sample(lista_kula, k=6))  # bez powtórzeń [28, 49, 39, 26, 24, 27]
