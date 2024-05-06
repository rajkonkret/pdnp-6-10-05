import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# SyntaxError: unterminated string literal (detected at line 5)
# print("Nazywam się Radek')  - bład cudzysłowiów
# ctrl / - komentarz automatyczny
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie linijek

# type() - sprawdzenie typu danych
print(type("Nazywam się Radek"))  # <class 'str'> typ tekstowy (string)

print(39)
print(type(39))  # <class 'int'> - liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300, str_digits_check_threshold=640)

print("54" + "28")  # 5428 - konkatenacja (łączenie) stringów
print(54 + 28)  # 82

print(5 * "4")  # 44444
print(25 * "168")  # 168168168168168168168168168168168168168168168168168168168168168168168168168

print(int("54") + int(28))  # 82 int() - jawne rzutownie na typ liczbowy

# print("54" + 28)  # TypeError: can only concatenate str (not "int") to str
# silne typowanie
print(str(54) + str(28))  # 5428 - str() - zamiana na string

# zmienna - pudełko na dane
imie = "Radek"
print(imie)  # wypisanie zawartości zmmiennej, Radek
print(type(imie))  # <class 'str'>

wiek = 48
print(type(wiek))  # <class 'int'>
print(wiek)

# zmienne typowanie dynamicznie
wiek = "Radek"
print(wiek)  # Radek
print(type(wiek))  # <class 'str'>

# print(wiek + 1)  # TypeError: can only concatenate str (not "int") to str

print(wiek + str(1))  # Radek1

# print(int(wiek) + 1)  # ValueError: invalid literal for int() with base 10: 'Radek'
print(chr(38))  # & - znak wg kodu ascii
print(ord("A"))  # kod ascii znaku 65

age: int = 67  # :int - podpowiedź typów
print(age)
print(type(age))  # <class 'int'>
age = "Radek"
print(age)  # Radek
