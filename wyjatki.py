# wyjątki - obsługa i rzucanie
# gdy wystąpi bład python rzuca wyjątek
# my powinnismy przechwycic i obsłużyc wyjątki
# print("')
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-6-10-05\wyjatki.py", line 2
#     print("')
#           ^
# SyntaxError: unterminated string literal (detected at line 2)

try:
    # print(5 / 0)
    # print(5 / "00")
    wynik = 5 / 1
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Bład typu")
except Exception as e:  # łapie pozostałe błedy
    print("Bład", e)
else:  # wykona się tylko wtedy kiedy nie wystąpi błąd
    print("Wynik", wynik)
finally:  # wykona się zawsze
    print("Zawsze")

print("Program nadal działa")
# try - except [else-finally]
