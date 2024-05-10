import requests as re

url = 'https://randomuser.me/api/'

response = re.get(url)
print(response.text)
data_resp = response.json()
user = data_resp['results'][0]
print(user)
# 'name': {'title': 'Mr', 'first': 'Leo', 'last': 'Barnes'}
print(f"Imię: {user['name']}")  # Imię: {'title': 'Mrs', 'first': 'Lela', 'last': 'Van Lopik'}
print(f"Imię: {user['name']['first']}")  # Imię: Enrique
print(f"Nazwisko: {user['name']['last']}")  # Nazwisko: Lee
photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")  # Link do zdjęcia: https://randomuser.me/api/portraits/women/34.jpg

respone_photo = re.get(photo_url)
with open('user_phot.jpg', 'wb') as f:
    f.write(respone_photo.content)

print("Zdjęcie zostało zapisane")
