# funkcja wewnętrzna, zagnieżdzona
# dekoratory - używają mechanizmu funkcji wewnętrznej

def fun1():
    print("To jest fun1")  # wyswietlenie napisu

    def fun2():  # zapamiętanie adresu fun2
        print("To jest fun2")

    return fun2  # zwracamy adres tej funkcji (referencje) fun2


fun1()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000013E993D98A0>
print(type(xFun))  # <class 'function'>
# uruchomienie funkcji
# nazwa fukcji i nawiasy() - ew. argumenty w nawiasach
xFun()
# To jest fun1
# To jest fun1
# <function fun1.<locals>.fun2 at 0x000002D8BBCE98A0>
# <class 'function'>
# To jest fun2
