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

podatek = 0
zarobki = int(input("podaj dochód"))
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30000:
    podatek = 0.2
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"Zapłacisz {zarobki * podatek}")
# dodac podatek 0.2 dla przedziału 10000 do 29999
# Pamiętać, że kolejnośc warunków elif ma znaczenie
