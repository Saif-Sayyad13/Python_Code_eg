'''#positional arguments
def Aman(a,b,c,d):
    print(a,b,c,d)
Aman(10,20,30,40)
print()

def Aman(a,b,c,d):
    print(a,b,c,d)
Aman(10,20,30) # TypeError: Aman() missing 1 required positional argument: 'd'
print()
'''
'''# keyword argument
def Aman(a,b,c,d):
    print(a,b,c,d)
Aman(b=10,c=20,d=30,a=40)
print()

def Aman(a,b,c,d):
    print(a,b,c,d)
Aman(d=10,a=20,c=30,) #TypeError: Aman() missing 1 required positional argument: 'b'
print()

def Aman(a,b,c,d):
    print(a,b,c,d)
Aman(d=10,a=20,c=30,x=99)#TypeError: Aman() got an unexpected keyword argument 'x'
print()
'''
'''# only positional
def Aman(a,b,/,c,d):
    print(a,b,c,d)
Aman(1,2,d=99,c=12)
Aman(1,2,3,4)
Aman(a=1,b=2,3,4) #SyntaxError: positional argument follows keyword argument'''

'''#only keyword

def Aman(a,b,*,c,d):
    print(a,b,c,d)
Aman(a=1,b=2,d=99,c=12)
Aman(1,b=2,d=99,c=2)
Aman(a=1,2,d=99,c=12)#SyntaxError: positional argument follows keyword argument

def x(a,b,*,c):
    print(a,b,c)
x(1,2,3)#TypeError: x() takes 2 positional arguments but 3 were given

'''

'''def Aman(a,b,*,c,/,d,e): #SyntaxError: / must be ahead of *
    print(a,b,c,d,e)
Aman(1,2,c=3,d=11,e=3)
'''
