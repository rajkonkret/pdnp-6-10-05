# funkcje - wydzielony fragment kodu, można wykonać wielokrotnie, można wywołąć w dowolnej chwili
# deklaracja funkcji musi być wcześniej niż jej wywołanie

a = 8
b = 9


# deklaracja funkcji - tu funkcja się nie wykonuje
def dodaj():  # funkcja bez argumentów
    print(a + b)  # zmienne globalne wykorzystane wewnątrz funkcji


def dodaj2(a, b):  # ma dwa obowiązkowe argumenty
    print(a + b)  # a,b są lokalne


# można zdefiniowac parametry o wartościach domyślnych tu c=0
# to pozwala zasymulowac w pythonie przeciązanie funkcji liczbą argumentów
def odejmij(a, b, c=0):
    print(a - b - c)


# wykonanie funkcji
dodaj()  # 17
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(6, 10)  # 16
odejmij(6, 7)
odejmij(6, 7, 8)  # przekazywanie argumentów po pozycji
odejmij(b=9, a=9, c=8)  # -8  argumenty przekazane po nazwie
odejmij(5, c=8, b=9)  # sposób mieszny, pozycyjne muszą być przed nazwanymi
# odejmij(a=5, b=8, 9)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None
# print(dodaj() + dodaj2(9, 7))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
