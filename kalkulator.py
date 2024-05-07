# napisać program kalkulator z wykorzystaniem pętli while True
# menu z dostępnymi opcjami
# pobrać wybraną opcje
# pobrać od użytkownika liczby do obliczeń
# wyswietlić wynik działania
# obsłużyć wyjątki

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj opcje z menu")
    if odp == '5':
        break

    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))
        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == '2':
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"Wynik odejmowania {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Dzielenie przez zero")
    except TypeError:
        print("Bład typu")
    except ValueError:
        print("Błąd wartości")
    except Exception as e:
        print("Bład", e)
    else:
        print("Obliczenia wykonane poprawnie")
    finally:
        print("Skońćzyłem obliczenia")

wyr = "5*7+9-10"
print(eval(wyr))  # oblicza wyrażenie  34
