# REST API - sposób komunikacji i wymiany danych pomięzy klientem a serwerem
# klient - przeglądarka - frontend
# serwer - backend, serwer który wystawia endpointy api i potrafi obłużyc te dane
# GET, POST, PUT/PATCH, DELETE - mettody http
# GET - pobiera dane (json, xml)
# POST - zapis danych, przeysła dane do serwera (json, xml)
# PUT/PATCH - modifikacja elemntu na zasobie
# DELETE - usunięcie
# CRUD - Create, Read, Update, Delete
# przeglądarka używa GET
import requests

# pip install requests
url = "http://api.open-notify.org/astros.json"

# GET
response = requests.get(url)
print(response)  # <Response [200]>
# 2xx - ok
# 3xx - przekierowanie
# 4xx - 404 - brak zasobu, 400 Bad request - błedne rządanie, błedy po stronie klienta
# 5xx - błędy po stronie serewra 500 Internal Server Error
print(response.text)
print(type(response.text))  # <class 'str'>
response_data = response.json()
print(response_data)
print(type(response_data))  # <class 'dict'>

# wypisać wszystkie klucze ze słownika
# klucze i wartości przypisane do nich

print(response_data.keys())  # dict_keys(['message', 'people', 'number'])
for k, v in response_data.items():
    print(k, "=>", v)
# message = > success
# people = > [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#             {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#             {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#             {'name': "Loral O'Hara", 'craft': 'ISS'}]
# number = > 7
print(response_data['message'])  # success
print(response_data['number'])  # 7
print(type(response_data['number']))  # <class 'int'>
print(response_data['people'][0])  # {'name': 'Jasmin Moghbeli', 'craft': 'ISS'}
for i in response_data['people']:
    print(i['name'])
# Jasmin Moghbeli
# Andreas Mogensen
# Satoshi Furukawa
# Konstantin Borisov
# Oleg Kononenko
# Nikolai Chub
# Loral O'Hara
