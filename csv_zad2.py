import csv

fields = []
rows = []

filename = 'records2.csv'
with open(filename, "r") as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect.delimiter, dialect.quotechar)
    file.seek(0)  # ustwienie ponownie odczytu na początek pliku
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x000001E661EC15A0>

    fields = next(csvreader)  # odczyta bieżacy elemnt i ustawi wskaźnik na następny
    for row in csvreader:
        # print(row)
        rows.append(row)

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)  # [['radek', 'coe', '3', '9.1']]
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '9.1'], ['tomek', 'cot', '2', '19.1'], ['zenek', 'cor', '1', '9.10']]
