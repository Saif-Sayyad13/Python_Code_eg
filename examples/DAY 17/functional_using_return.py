# def demo():
#     x=900
#     return x
# k=demo()
# print(k)
# # or
# print(demo())


def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    print(a,b,c)
Operations(10,5)
print()

def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a
    return b
    return c
w=Operations(10,5)
print(w)

print()

def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a,b,c
w=Operations(10,5)
print(w)
print()

def Operations(x,y):
    return x+y,x-y,x*y,x/y,x//y
w=Operations(10,5)
print(w) 