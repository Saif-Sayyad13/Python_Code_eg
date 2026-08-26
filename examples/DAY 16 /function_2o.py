'''
Types of argument while calling the Functions
1.Positional argument
2.keyword arguments
3.Only Positional argument(/)
4.only keyword arguments(*)
5.variable Positional arguments (*args)
6.variable keyword arguments (**kwargs)
7.combination of only Positional arguments
    and only keyword arguments
    
8.combination of *args and **kwargs

Only Positional arguments(/)

Before the forrward slash if we 

'''

"""
Only Positional arguments(/)
"""
"""
Before the forward slash if we Pass only Positional
arguments it will work properly.
but Before the forward slash if we Pass keyword arguments
it will show syntax error but after the  forward slash
we can Pass Positional or keyword arguments it will
work.

def demo(a,b,/,c):
    print(a,b,c)
demo(1,2,3)
demo(1,2,c=3)
demo(1,2,c=3)
"""
"""
only keyword arguments (*)

Here Before the * symbole we can Pass both
Positional and keyword arguments but after the
* symbole only we can Pass keyword argumnets.

def demo(a,b,*,c):
    print(a,b,c)

demo(1,b=10,c=90)
demo(1,10,c=90)
demo(1,10,90) Typeerror
"""
"""
combination of / and *
def spam(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
spam(1,2,3,d=90,e=89)
spam(1,2,c=3,d=45,e=33)
spam(100,200,300,d=900,1000)
"""

"""
1.Positional arguments (-->)
2.keyword argumnets (--->)
3.only Positional arguments(/)
4.only keyword arguments(*)
5.combination of / and *
6.variable Positional argumnets(*args)(--->)
7.variable keyword argumnets(**kwargs) (--->)
8.combination of *args and **kwargs (--->)
"""
'''
#6.variable Positional argumnets(*args)(--->)
def spam(*args):
    # print(args)  #Packed format
    print(*args)  #unPacked format
spam()
spam(1)
spam(1,2,3,4,5)
spam("abc",[1,2,3],True,False,{567,90},{5:9})

ex-->2
def check(*python):
    print(*python)
check()
check(90,100,200)
check([1,2,3,4],{90,23},8+9j)
'''

'''
# 7.variable keyword argumnets(**kwargs) (--->)
def check(**kwargs):
    print(kwargs)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)
print()

def check(**kwargs):
    print(*kwargs)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)

print()

def check(**sql):
    print(*sql)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)
'''
'''
# 8.combination of *args and **kwargs (--->)
def Data(*args,**kwargs):
    print(*args,*kwargs)
Data()
Data(11,12)
Data(110,120,a=90,b=99)
'''

"""def don(a,b,/,c):
    print(a,b,c)
don(1,2,c=3)
don(5,7,c=234567)"""

'''
Only keywprds argument(*)


'''
'''def demo(a,b,*,c):
    print(a,b,c)
demo(1,b=10,c=90)
demo(1,10,c=90)
demo(1,b=10,c=90)'''

'''def don(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
don(23,0,c=34,d=6,e=23)
don(23,0,34,d=6,e=23)'''

"""
Variable Positional arggument 



"""
'''
def demo(*args):
    print(args)
demo()
demo(1)
demo(1,2,"hi",1)
demo(1,2,'hi',[1,2,3],{2345})
print()
def demo(*args):
    print(*args)
demo()
demo(1)
demo(1,2,"hi",1)
demo(1,2,'hi',[1,2,3],{2345})
print()
def demo(*aman):
    print(aman)
demo()
demo(1)
demo(1,2,"hi",1)
demo(1,2,'hi',[1,2,3],{2345})
'''
"""
variable keyword argument(**kwarqs)

def demo(**kwargs):
    print(kwargs)
demo()
demo(a=1)
demo(a=1,b=2,c="hi",d=1)
demo(aman=1,aa=2,d='hi',f=[1,2,3],e={2345})

print()

def demo(**kwargs):
    print(*kwargs)
demo()
demo(a=1)
demo(a=1,b=2,c="hi",d=1)
demo(aman=1,aa=2,d='hi',f=[1,2,3],e={2345})

print()

def demo(**don):
    print(don)
demo()
demo(a=1)
demo(a=1,b=2,c="hi",d=1)
demo(aman=1,aa=2,d='hi',f=[1,2,3],e={2345})

"""







'''
DEfauld parameter 

def aman(x=0,y=0,z=0):
    print(x,y,z)
aman()
aman(1)
aman(1,2)
aman(1,2,3)'''

def don(*args, **kwargs):
    print(args,kwargs)
don()
don(11,22)
don(11,122,a=90,b=0000000)
don(11,122,a=90,b=01)


