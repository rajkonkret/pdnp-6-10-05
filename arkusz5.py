import pandas as pd

df = pd.DataFrame(
    {"Osoba": ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
     'wynik': [18, 25, 67]}
)


def sprawdz_wynik(wynik):
    if wynik > 19:
        return "zdany"
    else:
        return "oblany"


print(df)
#                   Osoba  wynik
# 0          Michał Jakub     18
# 1              Ewa Noga     25
# 2  Krzysztof Zawierucha     67
df.wynik = df.wynik.apply(
    sprawdz_wynik
)
print(df)
#                   Osoba   wynik
# 0          Michał Jakub  oblany
# 1              Ewa Noga   zdany
# 2  Krzysztof Zawierucha   zdany

df.to_excel('wyniki.xlsx', index=False)
