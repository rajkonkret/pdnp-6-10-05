# context manager - do usprawnienia pracy z plikami
# with
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler - uchwyt do pliku
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - tworzy nowy plik, usunie gdy ten już istnieje
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Radek\n")

# a - dopisanie danych na końcu pliku
with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane dwa\n")
    file.write("Dodane trzy\n")
    file.write("Dośdane trzy\n")

# file.write("TEST")  # ValueError: I/O operation on closed file.

# r - odczyt pliku
with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
