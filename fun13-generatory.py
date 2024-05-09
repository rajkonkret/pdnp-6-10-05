# generatory - funkcje zwracające kolejne wyniki
# nie przechowuje poprzednich wyników
# podstawia w kolejnosci
# efektywnie zarządza pamięcią
# leniwe generowanie - dane dostarczane są wtedy kiedy są konieczne do użycie
def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):  # range(5)  0..4
        yield x ** 2  # wykonuje opercja, zwraca wynik, zapamietuje gdzie jest, wartosc x


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x000001EEEB6B3780>
print(type(kwa))  # <class 'generator'>
print(next(kwa))
print(next(kwa))
print(next(kwa))
print('Zrób cokolwiek')
lista = []
lista.append("1234")
print(lista)
print(next(kwa))
# 0
# 1
# 4
# Zrób cokolwiek
# ['1234']
# 9
print(next(kwa))


# print(next(kwa))  # StopIteration - generator wyczerpał swoje działanie

def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def counter_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c2 = counter_down(10)
print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))

for i in counter_down(10):
    print(i)


def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c3 = counter_2(10)
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))
c3.send('ok')  # ok
try:
    c3.send('q')  # StopIteration
except StopIteration as e:
    print("Koniec generatora", e)  # Koniec generatora

# print(next(c3))  # StopIteration
