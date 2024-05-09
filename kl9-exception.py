class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# try:
#     # print(5 / 0)
#     # raise ZeroDivisionError("Dzielenie przez zero")  # rzucenie wyjątku
#     raise MyException("Tekst")
# except ZeroDivisionError as e:
#     print("Nie dziel przez zero", e)
# # Traceback (most recent call last):
# #   File "C:\Users\CSComarch\PycharmProjects\pdnp-6-10-05\kl9-exception.py", line 9, in <module>
# #     raise   MyException("Tekst")
# # MyException: Tekst

x = 0
try:
    if x == 0:
        raise MyException("X nie może być 0")
except MyException as e:
    print("X nie może być 0", e)
# X nie może być 0 X nie może być 0
