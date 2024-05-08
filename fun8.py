def allparams(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


# allparams()  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
allparams(1, 2)  # a, b 1 2
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, 3, 4)  # c, d 3 4
allparams(1, 2, c=6)  # c, d 6 256


# allparams(b=7, a=9,c=9)  # TypeError: allparams() got some positional-only
# arguments passed as keyword arguments: 'a, b'
# / oddziele argumnty, które mogą być przekzane po nazwie o d tych, które musza być przekzane po pozycji

def allparams_2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a ,b", a, b)
    print("c ,d", c, d)
    print("args", args)
    print("kwargs", kwargs)


#
allparams_2(1, 2)
allparams_2(1, 2, 3)
allparams_2(1, 2, c=3)
allparams_2(1, 2, d=10)  # c, d 42 10  d musi byc po nazwie bo jest po *args
allparams_2(1, 2, 3, 4)  # args (4,)
allparams_2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15)  # args (4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15)
allparams_2(1, 2, 3, 4, 5, d=8, name="Radek")  # kwargs {'name': 'Radek'}
allparams_2(1, 2, 3, 4, 5, d=8, a=1, name="Radek")
# kwargs {'a': 1, 'name': 'Radek'}
