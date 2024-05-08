def connect(**opcje):  # ** - argumenty słownikowe, dowolna ilośc argumentów nazwanych
    print(opcje)
    connect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    connect_param['pwd'] = opcje
    print(connect_param)


def all_args(*args, **kwargs):
    print(args, kwargs)


# k=6 - argumenty nazwane
# klucz=wartość
# {"klucz":"wartosc"}
connect()  # {}
connect(a=9)  # {'a': 9}
connect(a=9, b=10, e=56)  # {'a': 9, 'b': 10, 'e': 56}
connect(name="Radek")  # {'name': 'Radek'}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'name': 'Radek'}}

all_args()
all_args(1, 2, 3)
all_args(a=1, b=2, c=9)
# () {}
# (1, 2, 3) {}
# () {'a': 1, 'b': 2, 'c': 9}
# all_args(a=7, 9)  # SyntaxError: positional argument follows keyword argument
