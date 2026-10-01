'''
Function:- Set of code or block of code it will execute when we calling the function 
without calling function if we execute it will show blank space
we we want to avoid reperation
use same code / code reusse
Type of Function;
1) Predefine function/inbuild function
eg:- len(), print(), input(), type(), id(),chr(),abs(),isinstance()

2) user define function
user define  syntax 2 types:
i) without using return keyword
ii) with using return keyword


i)
def function_name(parameter):                        ---this complete box is called function declaration
    statement                                     this all statement is called 
    statement                                      as block of code or set of code
function_name(argument)                              --- this box is called function calling





paramete. is always pointing to argument
'''

"""def Greet():
    print("Good afternoon")
Greet()
Greet()
Greet()
Greet()"""

"""def Greet():
    print("Good afternoon")
print(Greet()) # none
Greet      # Normal Name
print(Greet) #<function Greet at 0x104b46480>
"""


'''def Student(name,age):
    print(f'My name is {name}\n'
        f'and My age is {age}')
Student(name="Aman ", age=23)
Student(name="Rohit",age= 25)'''

'''
Type of argument while calling the Function
1. Position argument 
2. Keyword argument
3. Only Positional Argument 
4. Only keyword argument  
5. variable Positional argument. (*args) 
6. variable keyword argument. (**kw args)
7. combination of only positional arguments
   and only keyword argument
8. combination of * args and **kwargs 


among 8 the imp is 1,2,5,6 


'''
'''
#WAP to check palindrome word
s="level"
if s==s[::-1]:
    print("its pal")
else:
    print("its not pal")
    
def Palindrome(s):
    if s==s[::-1]:
         print("its pal")
    else:
         print("its not pal")
Palindrome("level")
    
def Palindrome_Or_Not():
    a=eval(input("Enter a  word"))
    if a==a[::-1]:
         print("its pal")
    else:
         print("its not pal")
Palindrome_Or_Not()'''
"""
#WAP to check even or odd
a=eval(input("Enter a number"))
if a%2==0:
    print(f"The number{a} is even")
else:
    print(f'The number{a} is odd')
  
print()

def even_odd():
    a=eval(input("Enter a number"))
    if a%2==0:
        print(f"The number{a} is even")
    else:
        print(f'The number{a} is odd')
even_odd()

    """

'''d=["Hii","walmart","xyz","good","onoff"]
for i in d:
    if len(i)%2==0:
        print(i)
    else:
        print(i[::-1])
      
print()
  
def don(d):
    d=["Hii","walmart","xyz","good","onoff"]
    for i in d:
        if len(i)%2==0:
            print(i)
        else:
            print(i[::-1])
don(["Hii","walmart","xyz","good","onoff"])'''

'''s="Hello"
def Data(s):
    k={}
    for i in s:
        k[i]=ord(i)
    print(k)
Data('Hello')
Data('Python')'''

'''d=[1,45,28,True,False,999]
for i in d:
    if isinstance(i,bool):
        print(i)
        
print()

for i in d:
    if type(i)==bool:
        print(i)
  
print()      
def Boolean(d):
    for i in d:
        if isinstance(i,bool):
            print(i)
Boolean([1,45,28,True,False,999])
    
'''



'''e=[90,True,3.5,9+4,"abc",[1,2,3],{677,90}]
single=[]
double=[]
for i in e:
    if isinstance(i,(bool,int,complex,float)):
        single.append(i)
    else:
        double.append(i)
print(single)
print(double)
'''

'''
def Greet():
    print("Good afternoon")
Greet()
Greet()
Greet()
'''
'''
def Greet():
    print("Good afternoon")
print(Greet())   #None  and output
Greet   #Normal name
print(Greet) #<function Greet at 0x000002A7A7F64AE0>
'''
'''
def Student(name,age):
    print(f'My name is {name}\n'
          f'and My age is {age}')
Student("Ravi",25)
Student("Rohit",40)
'''
'''
def Student(name,age):
    print(f'My name is {name}\n'
          f'and My age is {age}')
Student("Ravi",25)
Student("Ravi",40)
Student("Mahiii",35)
'''

"""
Types of argument while calling the Functions
1.Positional argument
2.keyword arguments
3.Only Positional argument
4.only keyword arguments
5.variable Positional arguments (*args)
6.variable keyword arguments (**kwargs)
7.combination of only Positional arguments
    and only keyword arguments
8.combination of *args and **kwargs

"""
'''
def demo(x,y,z):
    print(x,y,z)
demo(x=1,2,z=3)#SyntaxError: positional argument follows keyword argument
'''
'''
#wap to check the given number is even
a=10
if a%2==0:
    print(f'The given number {a} is even')
else:
    print(f'The given number {a} is odd')

def even(a):
    if a % 2 == 1:
        print(f'The given number {a} is even')
    else:
        print(f'The given number {a} is odd')
even(10)
even(11)
'''




'''
def even_odd():
    num=int(input("enter the Number"))
    if num % 2 == 0:
        print(f'The given number {num} is even')
    else:
        print(f'The given number {num} is odd')
even_odd()
'''

#wap to check the given word is Palindrome
s="level"
if s==s[::-1]:
    print("its a pal")
else:
    print("its Not")

'''
def Palindrome(s):
    if s == s[::-1]:
        print("its a pal")
    else:
        print("its Not")
Palindrome("level")
Palindrome("mom")
Palindrome("Python")
'''

'''
s=[1,2,3,4,5,6,10]
for i in s:
    if i%2==0:
        print(i)
def even_data(s):
    for i in s:
        if i % 2 == 0:
            print(i,end=" ")
even_data([1,2,3,4,5,6,10])
'''
'''
d=["Hii","walmart","xyz","good","onoff"]
for i in d:
    if len(i)%2==0:
        print(i)
    else:
        print(i[::-1])
def Check(d):
    for i in d:
        if len(i) % 2 == 0:
            print(i)
        else:
            print(i[::-1])
Check(["Hii","walmart","xyz","good","onoff"])
'''
'''
s="Hello"
def Data(s):
    k={}
    for i in s:
        k[i]=ord(i)
    print(k)
Data("Hello")
Data("Python")
'''
'''
d=[1,45,78,True,False,999]
for i in d:
    if isinstance(i,bool):
        print(i)
print()
for i in d:
    if type(i)==bool:
        print(i)
print()
def demo(d):
    for i in d:
        if isinstance(i, bool):
            print(i)
demo([1,45,78,True,False,999])
'''

'''
e=[90,True,3.5,9+4j,"abc",[1,2,3],{67,90}]
s=[]
c=[]
for i in e:
    if isinstance(i,(int,float,complex,bool)):
        s.append(i)
    else:
        c.append(i)
print(s) #[90, True, 3.5, (9+4j)]
print(c) #['abc', [1, 2, 3], {90, 67}]
'''

'''
def check(e):
    s1=[]
    c1=[]
    for i in e:
        if isinstance(i, (int, float, complex, bool)):
            s1.append(i)
        else:
            c1.append(i)
    print(s1)
    print(c1)
check([90,True,3.5,9+4j,"abc",[1,2,3],{67,90}])
'''



