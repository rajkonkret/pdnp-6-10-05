# funkcja obliczająca średnią
def liczby(name=None, *cyfry):  # * przyjmuje dowolną ilość argumntów pozycyjnych 1,2,3,4,5,6
    print(cyfry)
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Uczeń {name}, średnia wynosi: {avg}")
    finally:
        print("Koniec działania")


# Uczeń imie, średnia wynosi: średnia

liczby()  # ()
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
# liczby(a=1)  # TypeError: liczby() got an unexpected keyword argument 'a'
liczby("Radek", 4, 5, 6)  # Uczeń Radek, średnia wynosi: 5.0
# a, *b = "Radek", 4, 5, 6
# name=None, *cyfry = "Radek", 4, 5, 6
