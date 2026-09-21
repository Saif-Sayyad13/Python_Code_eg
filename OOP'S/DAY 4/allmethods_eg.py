"""# By using Multi level inheritence

class School:
    def __init__(self,name,smarks,sage):
        self.name=name
        self.smarks=smarks
        self.sage=sage
        print(f'Student name is {self.name}.\n Student School marks are{self.smarks}.\n Student School age is {self.sage} ')
        
class Twelth(School):
    def __init__(self,tmarks,tage):
        self.tmarks=tmarks
        self.tage=tage
        super().__init__('Aman','500',18)
        print(f'Student 12 marks are {self.tmarks}.\n Student age at 12 class is {self.tage}')
        
class Degree(Twelth):
    def data(self,dmarks,dage):
        self.dmarks=dmarks
        self.dage=dage
       # super().__init__(600,20)
        print(f'Degree marks are {self.dmarks}.\n Age when in degree{self.dage}')
        
x=Degree(600,20)
x.data(1000,23)

'''if we write multiple super na the line no 21 ka answer will Beeew

Student name is Aman.
 Student School marks are500.
 Student School age is 18 
Student 12 marks are 1000.
 Student age at 12 class is 23
Student name is Aman.
 Student School marks are500.
 Student School age is 18 
Student 12 marks are 600.
 Student age at 12 class is 20
Degree marks are 1000.
 Age when in degree23'''
"""

# bank saving current and on saving intrest incress by 0.1 %
'''
1. Single Level Inheritance
Create a class Vehicle with a method start. Override this method in the child class Bike.
Demonstrate single-level inheritance.
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Bike(Vehicle):
    def start(self):
        print("Bike start")
x = Bike()
x.start()
'''
'''

2. Multilevel Inheritance
Create a Python program using multilevel inheritance:
BankAccount → store holder name and balance.
SavingAccount → add interest rate and calculate interest.
SeniorSavingAccount → add age and give 1% extra interest if age ≥ 60.
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Saving(Bank):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def cal_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        print(f"Interest total is {interest}")

class S_SAccount(Saving):
    def __init__(self, name, balance, interest_rate, age):
        super().__init__(name, balance, interest_rate)
        self.age = age
        if self.age >= 60:
            self.interest_rate += 1 


x = S_SAccount("Aman", 10000, 4, 65)
print(f"Account is own by  {x.name}, Rate: {x.interest_rate}%")
x.cal_interest()
'''

'''
3. Multiple Inheritance Create a Python program using multiple inheritance. Create a Person class with name, age, and a
details) method. Create a Company class with company name, salary, and a details method. Create Employee(Person, Company) that inherits from both classes. Display employee and
company details using the Employee object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Person Name is {self.name} and   Age is {self.age}")

class Company:
    def __init__(self, cname, salary):
        self.company_name = cname
        self.salary = salary

    def details(self):
        print(f"Company Details: Company is {self.company_name}, Salary is {self.salary}")

class Employee(Person, Company):
    def __init__(self, name, age, cname, salary):
        Person.__init__(self, name, age)
        Company.__init__(self, cname, salary)

    def display(self):
        Person.details(self)
        Company.details(self)

x = Employee("Aman", 23, "free", 50000)
x.display()
'''
'''
4. Hierarchical Inheritance Create a Company class with company name. Create Employee and Manager classes that inherit from Company. Employee should store employee name and ID. Manager should store manager
name and department. Display the details of both objects.
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

class Employee(Company):
    def __init__(self, company_name, emp_name, emp_id):
        super().__init__(company_name)
        self.emp_name = emp_name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee: {self.emp_name}, ID: {self.emp_id}, Company: {self.company_name}")

class Manager(Company):
    def __init__(self, company_name, mgr_name, dept):
        super().__init__(company_name)
        self.mgr_name = mgr_name
        self.dept = dept

    def display(self):
        print(f"Manager: {self.mgr_name}, Dept: {self.dept}, Company: {self.company_name}")

# Demonstration
emp_obj = Employee("Tech ", "Kishor", "E101")
mgr_obj = Manager("Tech ", "Aman", "IT")

emp_obj.display()
mgr_obj.display()
'''
'''
class Book:

    def __init__(self, book_title, book_author,):
        self.title = book_title
        self.author = book_author
        self.available = True  

    def get_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Is Available?:", self.available)


    def mark_unavailable(self):
        self.available = False 

    def mark_available(self):
        self.available = True 
class BorrowedBook(Book):
    def __init__(self, book_title, book_author, ):
        Book.__init__(self, book_title, book_author,)
        self.borrower_name = ""
        self.due_date = ""

    def borrow(self, name, date):
        if self.available == True:
            self.mark_unavailable()
            self.borrower_name = name
            self.due_date = date
            print(" Book is  given to:", name)
        else:
            print("This book  is taken by someone else.")

    def return_book(self):
        if self.available == False:
            self.mark_available()
            print( self.borrower_name, "has returned the book.")
            self.borrower_name = ""
            self.due_date = ""
        else:
            print("Error: This book is already in the library.")


b = BorrowedBook("Wings of Fire", "APJ Abdul Kalam")
b.get_details()
b.borrow("Kishor", "30 Sep")
b.borrow("Priya", "2 oct")
b.return_book()
'''