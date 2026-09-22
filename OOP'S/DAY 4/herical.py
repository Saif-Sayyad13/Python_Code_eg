"""
'''
4.hierarchical inheritance:
***************************
*A multiple child class inheriting property from a single parent class is called hierarchical inheritance.
diagram:'''



class Parent:
   def home(self):
       print("Parent Home")


class Child1(Parent):
   age = 18
# print(dir(Child1))      ['age', 'home']
# c = Child1()
# print(c.age)
# c.home()


# 18
# Parent Home


class Child2(Parent):
   def job(self):
       print("searching for job")
# print(dir(Child2))      ['job', 'home']
# c1 = Child2()
# c1.job()
# c1.home()
# searching for job
# Parent Home


#Example 02

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


#Example 03  With __init__() Constructor

class Company:
    def __init__(self, name):
        self.company_name = name

    def show_company(self):
        print(f"Company Name: {self.company_name}")

class Employee(Company):
    def __init__(self, name, emp_name, emp_id):
        super().__init__(name)
        self.emp_name = emp_name
        self.emp_id = emp_id

    def show_employee(self):
        print(f"Employee: {self.emp_name}, ID: {self.emp_id}")

class Manager(Company):
    def __init__(self, name, mgr_name, dept):
        super().__init__(name)
        self.mgr_name = mgr_name
        self.dept = dept

    def show_manager(self):
        print(f"Manager: {self.mgr_name}, Department: {self.dept}")

# Creating objects
e = Employee("TechCorp", "Alice", 101)
m = Manager("TechCorp", "Bob", "HR")

e.show_company()
e.show_employee()

m.show_company()
m.show_manager()


#Example 04
#Hierarchical with Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):  # overriding parent method
        print("Car is starting with key ignition")

class Bike(Vehicle):
    def start(self):  # overriding parent method
        print("Bike is starting with self-start button")

c = Car()
b = Bike()

c.start()  # overridden in Car
b.start()  # overridden in Bike
"""

