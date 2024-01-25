def f(x,a):
    return (a-x)*2


def y(a,b):
    c=b+a
    return c*a


def b(y,x):
    return x+f(x,y)

def m(a,x):
    c=a
    d=x+a
    return f(d,c)


def p(x,a):
    c=b(a,x)+m(a,f(x,y(a,x)))
    d=f(c,b(x,a))
    print(d)

p(1,2)
