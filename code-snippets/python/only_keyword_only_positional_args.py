# only positional = a, b
# either positional or keyword = c,d
# only keyword arguments = e,f

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


