"""
Generator :






"""

'''
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a
    return b
    return c
q=check(10,20)
print(q)

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(q)

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(q)
print(list(q))

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(q)
print(list(q))

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(next(q))
print(next(q))
print(next(q))

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a,b,c
q=check(10,20)
print(next(q))

print()
def check(x,y):
    yield x+y
    yield x-y
    yield x*y
q=check(10,20)
print(next(q))
print(next(q))
print(next(q))

print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(next(q))
q.close() #                                 if we want to stope next iteration 
print(next(q))





import sys
sys.getsizeof(q) #          this we get the size of this in byte

'''


'''x=[1,2,3,4,5,6]
def square(x):
    for i in x:
        print(i**2)
square([1,2,3,4,5,6])
'''

'''def square(x):
    for i in x:
        yield i**2
z=square([1,2,3,4,5,6])
print(next(z))
print(next(z))
print(next(z))
z.close()
print(next(z))
'''

# Syntax of next ====== next(object)
'''
x=[1,2,3,4,5,6]
def square(x):
    l=[]
    for i in x:
        l.append(i**2)
    return l
q=square([1,2,3,4,5,6])
print(q)

print()

x=[1,2,3,4,5,6]
def square(x):
    l=[]
    for i in x:
        l.append(i**2)
    yield l
q=square([1,2,3,4,5,6])
print(next(q))'''

'''x=["wallmart",'vistra','vstar','blind','thank you','pro max','panther']
def odd(x):
    y=[]
    for i in x:
        if len(i)%2==1:
            y.append(i)
    print(i)
odd(["wallmart",'vistra','vstar','blind','thank you','pro max','panther'])

x=["wallmart",'vistra','vstar','blind','thank you','pro max','panther']
def odd(x):
    y=[]
    for i in x:
        if len(i)%2==1:
            y.append(i)
    yield i
z= odd(x)
print(next(z))

'''
