'''
class Grandpa:
   def land(self):
       print("agriculture land")
# print(dir(Grandpa))  #     ['land']]


class Father(Grandpa):
   def car(self):
       print("my car")
# print(dir(Father))  #     [ 'car', 'land']]


class Child(Father):
   def loan(self):
       print("lot of loans")
# print(dir(Father))  #     ['loan', 'car', 'land']]


# c = Child()
# c.loan()
# c.car()
# c.land()

#Example 02

class University:
   USN = "1PY12012023"


class Collage(University):
   def exam(self):
       print("lab exam")
   def internal(self):
       print("internal exam")


class Student(Collage):
   def assignment(self):
       print("copying assignment last moment")


# s = Student()
# print(s.USN)
# s.internal()
# s.assignment()
# s.exam()

#Example 03

class GrandParent:
    def Hello(self):
        print("Hello from GrandParent")
class Parent(GrandParent):
    def Hello_method(self):
        print("Hello from Parent")
class Child(Parent):
    def Hello_child(self):
        print("Hello from child")

c=Child()
c.Hello()
c.Hello_method()
c.Hello_child()


#Example 04

#method overriding in method------> super().method_name()
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
c.Villa()


#Example 05
class Dad:
    def __init__(self):
        print("Gold property")
class MoM(Dad):
    def __init__(self):
        print("siliver Property")
        super().__init__()

class Child(MoM):
    def __init__(self):
        print("Money----loading")
        super().__init__()

x=Child()


#Example 06

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'my name is {self.name} and mine age is {self.age}')
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.sub=subject
    def show_data(self):
        print(f'mine subject name is {self.sub}')

class Incharge(Teacher):
    def __init__(self,name,age,subject,class_name):
        super().__init__(name,age,subject)
        self.class_name=class_name

    def details(self):
        print(f'i am taking in charge of {self.class_name}')

i=Incharge("Meera",28,"Python","A11")
i.show_data()
i.details()
i.show()

print("*******************************************************")
y=Incharge("Avii",26,"PowerApps","A18")
y.show_data()
y.details()
y.show()


print("----------------------------------------------------------------------")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('my name is {self.name} and mine age is {self.age}')
class Teacher(Person):
    def __init__(self,subject):
        super().__init__(name="Meera",age=28)
        self.sub=subject
    def show_data(self):
        print(f'mine subject name is {self.sub}')

class Incharge(Teacher):
    def __init__(self,class_name):
        super().__init__(subject="Python")
        self.class_name=class_name

    def details(self):
        print(f'i am taking in charge of {self.class_name}')

i=Incharge("A11")
i.show_data()
i.details()
i.show()
print("second object------------->> Data")
x=Incharge("M32")
x.show_data()
x.details()
x.show()

#Example 07

class BankAccout:
    def __init__(self,Holder,Balance):
        self.Holder=Holder
        self.bal=Balance
    def Data(self):
        print(f'Account Holder Name : {self.Holder} '
              f'and Total balance :{self.bal}')
class Saving(BankAccout):
    def __init__(self,Holder,Balance,Interset_rate):
        super().__init__(Holder,Balance)
        self.rate=Interset_rate

    def Add_interset(self):
        self.bal+=self.bal*self.rate/100
        print(f'after applying the interset total balance is {self.bal}')

class SeniorSaving(Saving):
    def __init__(self,Holder,Balance,Interset_rate,age):
        super().__init__(Holder,Balance,Interset_rate)
        self.age=age

    def Age_benfits(self):
        if self.age>=60:
            self.bal+=self.bal*1/100
            print(f'after applying 1% interset total amount is {self.bal}')

x=SeniorSaving("Pavan",10000,5,65)
x.Data()
x.Add_interset()
x.Age_benfits()

print()
print("age is less than 60------->")

y=SeniorSaving("Pavan",10000,5,59)
y.Data()
y.Add_interset()
y.Age_benfits()'''