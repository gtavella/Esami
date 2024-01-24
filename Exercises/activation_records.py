# I've written this code to train myself in writing activation records.


def p(a,b):
    return (a+b)*2

def n(x,y):
    a=3
    return f(a,y,x)

def f(b,a,t):
    return (t*2)+a+b

def x(a,b,c):
    d=2
    return f(c,b+d,a)

def q(x):
    y=f(x+2,x-1,x+1)
    return y+x

def main():
    t=5
    l=4
    y=p(t,l)
    b=n(y,t+l)
    a=x(y,b,q(b))
    print(a)

main()

# What's the value of variable a?
# 329
