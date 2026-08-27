"""Scope :- the  place of the vasriable
types of variable (3)
1) Local variable 
2) Global variable
3) Nonlocal variable

1) Local variable :- 
Any variable present inside the function then we can access it as a local varaible
Local variable we can not access outside directely if we access it will show Name error
How to access local variable  outside by the help of return keywords

Local Variable
def spam():
    a=100
    print(a)
spam()

def spam():
    a=100
    return a
x=spam()
print(x)

def spam():
    a=100
    a+=50
    return a
x=spam()
print(x)

2) Global varaible
  #Global variable

# Any variable is Present outside the function then we can call it as a
#global variable.


#Global variable we can access any where into the function means inside the
#function or outside the function it will work.


#global variable we can do modification outside without useing any keyword
#but if we done any modification inside the function without keyword it will
#show unboundedlocal error


#How to do Modification for global variable inside---->???

#By useing global keyword.



 Any varaible is present outside the function then we can call it as a global varaiable 
 gobal varaible we can access any where intothe function means  we can access inside the function or outside the function it will works 
 global varable we can do modification without using any keywords but 
 if we done any modification inside the function without keyword sit will show unboundedlocal error
 
 How to do modicafication for gloabl varable inside 
 by using global keywords 
 
 eg:- 
 a=100             # global variable
def display():
    b=10          # local variable
    print(f' the given varaible is local variable. {b}')
    print(f' the given varaible is global variable. {a}')
display()
print(a)
print("modification for global variable (outside)")
a=a+400
print(a)
print()

a=100             # global variable
def display():
    global a
    b=10          # local variable
    print(f' the given varaible is local variable. {b}')
    a=a+400
    print(f' the given varaible is global variable. {a}')
    
display()
print(a)
print("modification for global variable (outside)")
a=a+400
print(a)

3) Nonlocal variable
Any variable is present in between 2 function that type of variable is called as non local variable
nither local nor gloable in between two function  what varibale we are mention. that we can called as non local variable 







x=10
def outer():
    y=20
    print(x)
    print(y)
    def inner():
        z=30
        print(x)
        print(y)
        print(z)
    inner()
    print(x)
    print(y)
    
outer()
print(x)





x=10
def outer():
    global x
    y=20
    
    def inner():
        nonlocal y
        z=30
        print("Modifica of non local varaible:")
    y=y+180
    x=x+180
    print(y)
    print(x)
    
outer()


outer()


x=10
def outer():
    global x
    y=20
    y=y+80
    x+=90
    #print(x) #100
    #print(y) #100
    def inner():
        global y
        y=y+300
        print(y)
        #nonlocal y
        #global x
        #x=x+100   #100=100+100
        #print(x)#200
        z=30
        print("Modification for Nonlocal variable")
        y=y+180
        #print(y)
        #print(x)
        #print(y)
        #print(z)
    inner()
    #print(x)
    #print(y)
outer()
#print(x)
#print(z)

"""






























