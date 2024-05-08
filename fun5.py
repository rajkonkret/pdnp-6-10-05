# stworyć funkcję kantor
# ma posiadać dwie funkcje wewnętrzne usd, eur
# w zależności od parametru zwraca wybraną funkcję
# mozliwośc przekazania dowolnej kwoty do wymiany

def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 4.01)

    def eur(kwota=0):
        print("Wymieniam euro", kwota * 4.31)

    # funkcje zwracamy bez nawiasu, zwracamy tylko adres funkcji
    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor("usd")
kantor_usd()
kantor_usd(500)  # Wymieniam dolary 2005.0

kantor_eur = kantor("eur")
kantor_eur(2000)  # Wymieniam euro 8620.0
