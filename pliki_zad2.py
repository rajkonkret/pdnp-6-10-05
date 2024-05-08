import chardet

# pip install chardet
# pip list - lista zainstalowanych pakietów

with open('test.log', 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6332532790369307, 'language': 'Turkish'}
# Po dodaniu większej ilośc polskich liter w pliku odczytał prawidłowo
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']

print(raw_data.decode(encoding=encoding))
# Radek
# Dodane
# Dodane dwa
# Dodane trzy
# Dośćśńdane trzy
