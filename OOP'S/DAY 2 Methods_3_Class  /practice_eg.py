#1.Create a class Person Store name and age Display details
'''class Person:
    def info(self,name,age):
        print(name ,'&', age)
c=Person()
c.info('Aman',22)'''
   
'''class Person:
    def info(self):
        print("name is Aman\n and age is 22")
c=Person()
c.info()'''
       








#4.  Create class Laptop Store: brand price RAM Print like: HP 50000 16GB
'''class laptop:
    def __init__(self,brand , price, ram):
        self.brand=brand
        self.price=price
        self.ram=ram
        print(f'{self.brand} {self.price} {self.ram}')
x=laptop('Hp ',50000,'16GB')'''

#2.Create a class Dog Store name and breed Print dog details
'''class Dog:
    def info(self,name,bread):
        self.name=name
        self.bread=bread
    
    def show(self):
        print(f'Dog name is {self.name} and its Bread is {self.bread}')
        
x=Dog()
x.info('Kutta','Indi')
x.show()'''

#3.Create a class Fan Store brand and price Display details


#4.Create a class Employee Store name and salary Increase salary by 5000 Display details
'''class Employee:
    
    def demo(self,name,sal):
        self.name=name
        self.sal=sal
        print(f'Emp name is {self.name} and sal is {self.sal}')
    
    def show(self):
        a=self.sal+5000
        print(f'updated sal is {a}')
        

x=Employee()
x.demo('Raju kirana', 4500)
x.show()'''

#5.Create a class Gameplayer Store player name and score Increase score


'''6.	BANK CLASS
Question:
WAP TO CREATE A CLASS NAME AS A BANK
Create a class Bank:
Create account (name, balance)
Deposit money
Withdraw money
Display balance
'''

'''
# creat instence method  and on econstrsction and print from cont and store value stdynt name age grade

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def show(self):
        print(f'{self.name} {self.age} {self.grade}')
       
x=Student('Aman',23,"A")
x.show()
'''

'''
method chaning  super function use in
constucrtion super function use in


'''


'''class A:
    ...
x=A()
print(A.__dict__)'''

'''class student:
  def data (self,name):
    self.name=name
s1=student()
s1.data("shubhangi")
print(s1.name)
s2=student()
s2.data("anjali")
print(s2.name)
s1.name="priya"
print(s1.name)'''

'''class B:
    c=900
    def Man(self,age):
        self.age=age
        B.c=340
    
        print(self.age)
        
x=B()
x.Man(23)
print(B.c)
x.c=500
print(x.c)'''

'''
#fun student info class name roll no marks  when every a call name and roll its should be same but marks incress by 5 

class Student:
    def info(self,name,age,marks):
        self.name=name
        self.age=age
        
        self.marks=marks
    
    def show(self):
        print(f'student name is{self.name}, student age is {self.age},student marks is{self.marks}')
        
    def update(self):
        self.marks+=5
x=Student()
x.info('Aman',23,15)

x.update()
x.show()
x.info('Bman',23,25)
x.update()
x.show()'''

'''class School:
    school_name = "ABC Public School"
    @classmethod
    def display_school(cls):
        print("School Name:", cls.school_name)

'''
'''class Student:
    def __init__(self):
        self.n = "Prabhu"

s1 = Student()
print(s1.n)
'''
'''class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anu", 20)
print(s1.name, s1.age)
'''
'''class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 20000)
m2 = Mobile("Apple", 80000)
m3=Mobile('iqoo',30000)
print(m1.brand,m3.price)
print(m1.brand, m1.price)
print(m2.brand, m2.price)
'''

'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width   # calculation inside constructor

r1 = Rectangle(5, 3)
print("Area:", r1.area)
'''
'''class Square:
    def __init__(self,area):
        self.area=area
        self.total=area*4
x=Square(5)
print(x.total)

        '''
        
'''class Student:
    def __init__(self, marks):
        self.marks = marks
        if marks >= 40:
            self.result = "Pass"
        else:
            self.result = "Fail"

s1 = Student(333)
print(s1.result)'''


'''class Student:
    college = "ABC College"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Ram")
s2 = Student("Anu")

print(s1.name, s1.college)
print(s2.name, s2.college)
'''
'''class Car1:
   def __init__(self,brand,model,price,*args):
       print(f'{brand} brand with {model} price is {price}')
       print(f'extra information are {args}')
      
c=Car1("kia","k7","Rs15lkh")
c1=Car1("kia","k7","Rs15lkh","white","2019 engine")
'''

'''class Dad:
   def spam(self):
       print("Dad's class")
class Child(Dad):
   def demo(self):
       print("Child class")
x=Child()
x.demo()
x.spam()
Child.spam(x)
Child.demo(x)'''

#2.Create a class Bank with attribute balance. Create a child class 
# SavingsAccount with methods: deposit() withdraw() 
'''class Bank:

    def __init__(self, bal):
        self.bal = bal
        
class Saving(Bank):

    def __init__(self, bal):
        super().__init__(bal)

    def deposite(self, amo):
        self.amo = amo
        self.r = self.bal + self.amo

        self.bal = self.r 
        print(f'total balance is {self.bal}')
        print(f'total amount after dep is {self.r}')
        
    def withdraw(self, amo1):
        self.amo1 = amo1
        self.bal = self.bal - self.amo1 
        print(f'withdrw amount is {self.amo1}')
        print(f'remaining balance is {self.bal}')

x1 = Saving(5000)

x1.deposite(5000)
x1.withdraw(2500)
'''

'''
class Grandpa:
   def land(self):
       print("agriculture land")
class Father(Grandpa):
   def car(self):
       print("my car")
class Child(Father):
   def loan(self):
       print("lot of loans")
c = Child()
c.loan()
c.car()
c.land()'''

'''
multilevel
class GrandParent:
    def Villa(self):
        print("GrandParent Property")
class Parent(GrandParent):
    def Villa(self):
        print("Parent Property")
        super().Villa()
class Child(Parent):
    def Villa(self):
        print("Child Property")
        super().Villa()
c=Child()
c.Villa()'''
'''

# Multiple
class Parent1:
    def __init__(self, name):
        print(f"Parent1 Constructor: Hello {name}")

    def show(self, age):
        print(f"Parent1 Show: Age is {age}")

class Parent2:
    def __init__(self, city):
        print(f"Parent2 Constructor: You live in {city}")

    def show(self, country):
        print(f"Parent2 Show: Country is {country}")

class Child(Parent1, Parent2):
    def __init__(self, name, city):
        print("Child Constructor starts")
        super().__init__(name)    # Calls Parent1 first (MRO)
        Parent2.__init__(self, city)  # Manually call second parent
        print("Child Constructor ends")

    def show(self, age, country):
        print("Child Show Method")
        super().show(age)             # Calls Parent1's show
        Parent2.show(self, country)   # Manually call Parent2's show

# Test
c = Child("Prince", "Bangalore")
c.show(25, "India")


'''



'''#example on hierarchical inheritance

# Parent class
class Person:
    def display(self):
        print("I am a person")

# Child class 1
class Student(Person):
    def study(self):
        print("I am a student and I study")

# Child class 2
class Teacher(Person):
    def teach(self):
        print("I am a teacher and I teach")
        
# Creating objects
s = Student()
t = Teacher()

# Accessing parent method from both children
s.display()
s.study()

t.display()
t.teach()
'''
'''
# hybride

class RBI:
   def money_back(self):
       print("amount will be double if u fixed for 5 Years")


class Icici(RBI):
   def FD_account(self):
       print("rate of interest is 7.5%")


class Postoffice(RBI):
   def saving_scheme(self):
       print("save money")


p = Postoffice()
p.money_back()
p.saving_scheme()
#amount will be double if u fixed for 5 Years
# save money


i = Icici()
i.money_back()
i.FD_account()
# amount will be double if u fixed for 5 Years
# rate of interest is 7.5%'''


'''

Has a realitionship
class Address:
    def __init__(self, city, state, country):
        self.city = city
        self.state = state
        self.country = country

    def show_address(self):
        return f"{self.city}, {self.state}, {self.country}"

# Person class uses Address
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address   # Composition

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address.show_address()}")

# Creating Address object separately
addr = Address("Bengaluru", "Karnataka", "India")

# Passing it into Person
p = Person("Prince", 25, addr)
p.show_details()
'''
# Class 1: Engine
'''class Engine:
    def start(self):
        print("Engine started...")

    def stop(self):
        print("Engine stopped...")

# Class 2: Car uses Engine (Composition)
class Car:
    def __init__(self, brand):
        
        self.brand = brand
        self.engine = Engine()   # Composition: Car HAS an Engine

    def drive(self):
        print(f"Driving {self.brand} car")
        self.engine.start()

    def park(self):
        print(f"Parking {self.brand} car")
        self.engine.stop()

# Using Car class
c = Car("Tesla")
c.drive()
c.park()
'''


