# dekoratory
# wykorzystują mechanizm funkcji wewnętrznej
# dekorator przyjmuje funkcję jako argument, dodaje nową funkcjonalnośc, zwraca wynik
def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew  # zwracamy adres funkcji


@dekor
def hej():
    print("Hej")


@dekor
def odejmij():
    print(7 - 9)


hej()
# Dekorujemy
# Hej
odejmij()
# Dekorujemy
# -2
