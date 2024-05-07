# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku (True lub False) wykonuje odpowiednnie działanie

# odp = True  # prawda
# odp = False
odp = "Radek"
# jezli odp będzie True wykona zadanie po :
# w przeciwnym wypadko ominie instrukcje po :
if odp:
    print("Brawo")  # obowiązkowe wciecie

print("Dalsza część programu")

print(odp == "Radek")  # True
if odp == "Radek":
    print("To jest Radek")

odp2 = False
if odp2:
    print("Brawo")
else:  # wartość domyslna
    print("Wartośc inna")

print("Dalsza częśc programu")

# podatek = 0
# zarobki = int(input("podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9

# print(f"Zapłacisz {zarobki * podatek}")
# dodac podatek 0.2 dla przedziału 10000 do 29999
# Pamiętać, że kolejnośc warunków elif ma znaczenie

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabacik = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienne będą przechowywać dane, które przyszły z innego systemu
# w zależności od danych, będziemy wykonywać różne zadania
# email, console, dowolny inny
# alert z konsoli - wydrukujemy gotowy komunikat
# np.: "Stało się coś strasznego" +
# zapiszemy komunikat do listy
# na koniec wypiszemy tą liste
# error, medium, inny
# w tej liscie ma być opis komunikatu

alert_system = 'email'
error = 'medium'

error_message = "Stało się coś strasznego"

lista_bledow = []  # pusta lisra

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    print("Alert z systemu email")
    if error == 'error':
        lista_bledow.append("Wystapił bład error")
    elif error == 'medium':
        lista_bledow.append("Wystąpiło ostrzeżenie")
    else:
        lista_bledow.append("Wystąpił inny bląd")
else:
    print("Nie znam takiego systemu")

print(lista_bledow)
# ['Wystąpiło ostrzeżenie']

# napisać test z.....
# zadać pytanie
# pobrać odpowiedź
# sprawdzić czy prawidłowa
# wyswietlić wynik

odp = input("Podaj datę Chrztu Polski")  # str
if odp == '966':
    print("Odpowiedź prawidłowa")
else:
    print("Masz w ksiązce na stronie 23")
