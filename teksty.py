tekst = "Witaj świecie"
print(tekst)  # <class 'str'>
print(type(tekst))  # Witaj świecie

tekst.upper()  # zamiana na duże litery, zwraca kopie. baza nie zostaje zmieniona
print(tekst)  # Witaj świecie
""" Return a copy of the string converted to uppercase. """

print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie

tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE
# teksty są niemutowalne
# spróbujcie zrobić zamiane na małe litery
print(tekst.lower())  # witaj świecie
print(tekst)  # Witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # "Witaj świecie" - baza nie uległa zmianie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie' - b - postac binarna(bajtowa)
print(type(encoded_s))  # <class 'bytes'> - bajty
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # sprawdzamy od indeksu 0 do indeksu 3 ( zbiór z prawej otwarty) -> 0123
# Witaj świecie
# 01234
# Wita
print(tekst.count("j", 0, 4))  # 0
print(len(tekst))  # len() - długość - 13

imie = "Radek"
# f - string - sformatowany string
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"  # f - sformatowany string
print(tekst_format)
# "	 Mam na imię Radek
#  i lubię Pythona"
# \ znak sterujący
# t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s"  # %s - string
print(starszy % imie)  # Witaj Radek

print("""
Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

print("Witaj {}".format(imie))  # Witaj Radek
