from datetime import date, timedelta, datetime

today = date.today()
print("Dzisiejsza data", today)  # Dzisiejsza data 2024-05-07

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-05-07 15:05:44.101506
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutro będzie", tomorrow)  # Jutro będzie 2024-05-08

print(time.time())
print(today.day)
# 15:11:04.217648
# 7

formatted_date = datetime.now().strftime('%d/%m/%Y')
print(f"Sformatowana data {formatted_date}")  # Sformatowana data 07/05/2024

formatted_time = datetime.now().strftime('%H:%M')
print("Sformatowany czas:", formatted_time)  # Sformatowany czas: 15:13

# czas w formacie 12h
formatted_time_12h = datetime.now().strftime('%I:%M %p')
print("Czas 12h:", formatted_time_12h)  # Czas 12h: 03:15 PM

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 99.99},
]

# print(products)
for p in products:
    # print(p)  # {'sku': 1, 'exp_date': datetime.date(2024, 5, 7), 'price': 100.0}
    if p['exp_date'] == today:
        p['price'] *= 0.8  # price = price * 0.8
        print(f"""
Price for sku {p['sku']}
is now {p['price']}""")

for p in products:
    if p['exp_date'] != today:
        continue  # wróc na początek, weź kolejny element
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""
    Price for sku {p['sku']}
    is now {p['price']}""")
