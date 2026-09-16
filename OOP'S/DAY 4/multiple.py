'''##Example 01
class Father:
    def quality(self):
        print("Father is hardworking ")

class Mother:
    def skill(self):
        print("Mother is intelligent ")

class Child(Father, Mother):
    def own_talent(self):
        print("Child is creative ")

# Create Child object
c = Child()
c.quality()       # from Father
c.skill()         # from Mother
c.own_talent()    # from Child


#Example 02

class A:
    def display(self):
        print("Display from A")
        super().display()   # goes to B next

class B:
    def display(self):
        print("Display from B")

class C(A, B):
    def display(self):
        print("Display from C")
        super().display()   # goes to A

obj = C()
obj.display()

#Example 03
class X:
    def action(self):
        print("Action from X")
        super().action()

class Y:
    def action(self):
        print("Action from Y")

class Z(X, Y):
    def action(self):
        print("Action from Z")
        super().action()

z = Z()
z.action()


#Example 04

class Parent1:
    def __init__(self):
        print("Parent1 Constructor")

class Parent2:
    def __init__(self):
        print("Parent2 Constructor")

class Child(Parent1, Parent2):
    def __init__(self):
        print("Child Constructor")
        super().__init__()   # follows MRO

c = Child()


#Example 05
 #Constructor & Method Overriding with Parameters (Using super())

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


#Example 06

class Person:
    def __init__(self, name, age):
        print(f"Person Constructor: Name={name}, Age={age}")

    def details(self, city):
        print(f"Person Method: City = {city}")

class Company:
    def __init__(self, company_name, salary):
        print(f"Company Constructor: Company={company_name}, Salary={salary}")

    def details(self, dept):
        print(f"Company Method: Department = {dept}")

class Employee(Person, Company):
    def __init__(self, name, age, company_name, salary):
        print("Employee Constructor Start")
        super().__init__(name, age)               # Goes to Person first
        Company.__init__(self, company_name, salary)  # Manually call Company
        print("Employee Constructor End")

    def details(self, city, dept):
        print("Employee Method Start")
        super().details(city)          # Calls Person's details
        Company.details(self, dept)    # Calls Company details
        print("Employee Method End")

e = Employee("John", 30, "TechCorp", 75000)
e.details("Bangalore", "IT")
'''