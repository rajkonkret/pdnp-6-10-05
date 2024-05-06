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
