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