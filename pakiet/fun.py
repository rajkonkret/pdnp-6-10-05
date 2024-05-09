def powitanie():
    print("Cześć")


def info():
    print("Jestem pakietem")


# ten kod wykona się tylko gdy plik zostanie uruchomiony bezpośrednio
# nie będzie się wykonywał podczas importowania tego pliku
if __name__ == '__main__':
    powitanie()
    print("Coś tam")
