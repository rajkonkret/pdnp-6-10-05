import pakiet
from pakiet import fun  # importuje konkretny plik z pakietu
import pakiet.fun as pk  # importuje plik jako alias

# pakiet.powitanie()  # AttributeError: module 'pakiet' has no attribute 'powitanie'
pakiet.powitanie()  # Cześć - po dodaniu wpisu w __init__.py
fun.powitanie()  # Cześć
pk.powitanie()  # Cześć

# metody info() nie ma w __init__.py
# nie jest importowana przy imporcie pakietu
# pakiet.info()

# Przy imporcir pliku ta metoda jest widoczna
pk.info()
fun.info()
