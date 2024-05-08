import csv

# pliki csv
# pliki w których dane oddzielone są separatorem (, tab ;)
# Radek, Maciek, Zenek

filename = 'records.csv'

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records2.csv'
dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'},
    {'name': 'tomek', 'branch': 'cot', 'year': 2, 'cgpa': '19.1'},
    {'name': 'zenek', 'branch': 'cor', 'year': 1, 'cgpa': '9.10'},
]

with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    # zapis jedego wiersza ze słownika
    # csvwriter.writerow(dictionary)
    # zapis z listy słowników
    csvwriter.writerows(dict_list)
