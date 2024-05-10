# baza danych - przechowywanie danych
# sql, nosql
import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych zostałą podłączona")

    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as f:
        sql_script = f.read()

    # c.execute(query)
    # conn.commit()  # utrwalenie zmian

    # uruchominie skryptu wczytanego z pliku
    c.executescript(sql_script)
except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
