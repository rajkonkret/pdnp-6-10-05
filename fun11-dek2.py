# dwa dekoratory
# zamienia wynik działania funkcji na duże litery
# wyswiatla tekst pogrubiony

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()
        return "\033[1m" + result + "\033[0m"

    return wrapper


# kolejność dekoratorów ma znaczenie
@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
