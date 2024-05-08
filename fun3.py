a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne, nie wpływaja na wartośc globalną
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # wewnątrz funkcji używa globalnej zmiennej a
    a = 8
    b = 9
    print(a + b)


print("Wartość a z góry(globalne)", a)  # Wartość a z góry(globalne 10
dodaj()  # 13
print("Wartość a z góry(globalne)", a)  # Wartość a z góry(globalne 10
dodaj2()  # 20
print("Wartość a z góry(globalne)", a)  # Wartość a z góry(globalne 10
dodaj3()  # 17
print("Wartość a z góry(globalne)", a)  # Wartość a z góry(globalne) 8
dodaj2()  # 18
