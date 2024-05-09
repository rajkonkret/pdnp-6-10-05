# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z kalsy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # kolejność ma znaczenie
    """
    Klasa dziedziczy po kalsie B i A
    """


class D(A, B):
    def method(self):
        super().method()  # dziedziczy po klasie nadrzędnej


class E(B, A):
    def method(self):
        print("Metoda z kalsy E")  # nadpisujemy całkowicie metodę


class G(A, B):
    def method(self):
        B.method(self)  # wskazanie z której klasy ma dzidziczyć metodę tu: B


class H(A, B):
    def method(self):
        super().method()
        B.method(self)
        print("Metoda z kalsy H")


a = A()
a.method()  # Metoda z kalsy A
b = B()
b.method()  # Metoda z klasy B
c = C()
c.method()  # Metoda z klasy B
# kolejność rozwiązywania nazw
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
d = D()
d.method()  # Metoda z kalsy A
e = E()
e.method()  # Metoda z kalsy E
g = G()
g.method()  # Metoda z klasy B
h = H()
h.method()
# Metoda z kalsy A
# Metoda z klasy B
# Metoda z kalsy H
print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
