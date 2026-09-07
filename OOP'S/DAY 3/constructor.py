'''class Data:
    def __init__(self):
        print("first Class")
d=Data()# by using object we can call the constructor
Data.__init__(d)# by using class name we can call the constructor
'''


'''class Aman:
    def __init__(self):
        print("Good Afternoon")
        
    def __init__(self):
        print("Good Evening") # constuctor overloading
a=Aman()'''

'''class Student:
    def __init__(self):
        print('Student class')
        
    def show(self):
        print('Student class show method')
        
s=Student()
s.show()'''


'''# 4. calling instance method into the constructor
class Student:
    def __init__(self):
        print('Student class')
        self.show()
        
    def show(self):
        print('Student class show method')
        
s=Student()
'''

# 5. 
'''
class Car:
    def __intit__(self):
        #instance varable
        self.name='BMW'
        self.model='X5'
        self.price=1000000
        self.color='Black'
        
        print(f'Car name is {self.name}\n'
              f'Car model is {self.model}\n'
              f'Car price is {self.price}\n'
              f'Car color is {self.color}\n')
              
x=Car()

#6. constructor plus instance method without parameter

class Car:
    def __init__(self):
        #instance varable
        self.name='BMW'
        self.model='X5'
        self.price=1000000
        self.color='Black'
        
        def show(self):
            print(f'Car name is {self.name}\n'
              f'Car model is {self.model}\n'
              f'Car price is {self.price}\n'
              f'Car color is {self.color}\n')
        
              
x=Car()
'''
'''class Car: 
    def __init__(self): 
        # instance variables
        self.name = 'BMW' 
        self.model = 'X5' 
        self.price = 1000000 
        self.color = 'Black' 
        
        # This runs automatically upon object creation
        print(f'Car name is {self.name}\n' 
              f'Car model is {self.model}\n' 
              f'Car price is {self.price}\n' 
              f'Car color is {self.color}\n')

# Creating the object triggers the print statements immediately
x = Car()
'''
'''
class Car: 
    def __init__(self): 
        # instance variables
        self.name = 'BMW' 
        self.model = 'X5' 
        self.price = 1000000 
        self.color = 'Black' 
        self.show()  # Call the instance method from the constructor
        
        
    def show(self): 
        # This only runs when the method is called
        print(f'Car name is {self.name}\n' 
              f'Car model is {self.model}\n' 
              f'Car price is {self.price}\n' 
              f'Car color is {self.color}\n')

# 1. Create the object (stores the data, but prints nothing)
x = Car()

# 2. Call the method to display the output
x.show()

'''

'''
class RoomNo3:
    def __init__(self,total_student,total_girls,total_boys,subject):
        self.total_student = total_student
        self.total_girls = total_girls
        self.total_boys = total_boys
        self.subject = subject
        
        print(f'Total student in the class is {self.total_student}\n'
              f'Total girls in the class is {self.total_girls}\n'
              f'Total boys in the class is {self.total_boys}\n'
              f'Current Subject  name is {self.subject}\n')
r=RoomNo3(45,20,25,'Python')

print('-------------------------------------')
r1=RoomNo3(50,30,20,'SQL')
print('-------------------------------------')
r2=RoomNo3(100,50,50,'C++')
'''


'''
class RoomNo3:
    def __init__(self,total_student,total_girls,total_boys,subject):
        self.total_student = total_student
        self.total_girls = total_girls
        self.total_boys = total_boys
        self.subject = subject
        
    def class_information(self):
        print(f'Total student in the class is {self.total_student}\n'
              f'Total girls in the class is {self.total_girls}\n'
              f'Total boys in the class is {self.total_boys}\n'
              f'Current Subject  name is {self.subject}\n')

e=RoomNo3(45,20,25,'Python')
e.class_information()

print('-------------------------------------')
e1=RoomNo3(90,80,10,'SQL')
e1.class_information()
print('-------------------------------------')
e2=RoomNo3(100,50,50,'C++')
e2.class_information()'''


'''
# *args
class RoomNo3:
    def __init__(self,total_student,total_girls,total_boys,subject,*args):
        self.total_student = total_student
        self.total_girls = total_girls
        self.total_boys = total_boys
        self.subject = subject
        self.args=args
        
    def class_information(self):
        print(f'Total student in the class is {self.total_student}\n'
              f'Total girls in the class is {self.total_girls}\n'
              f'Total boys in the class is {self.total_boys}\n'
              f'Current Subject  name is {self.subject}\n'
              f'extra data is {self.args}\n')

e=RoomNo3(45,20,25,'Python','Aman','Ravi','Ramesh')
e.class_information()'''


'''
# **kwargs
class RoomNo3:
    def __init__(self,total_student,total_girls,total_boys,subject,**kwargs):
        self.total_student = total_student
        self.total_girls = total_girls
        self.total_boys = total_boys
        self.subject = subject
        self.kwargs=kwargs
        
    def class_information(self):
        print(f'Total student in the class is {self.total_student}\n'
              f'Total girls in the class is {self.total_girls}\n'
              f'Total boys in the class is {self.total_boys}\n'
              f'Current Subject  name is {self.subject}\n'
              f'extra data is {self.kwargs}\n')

e=RoomNo3(45,20,25,'Python',student_names=['Aman','Ravi','Ramesh'],teacher_name='Don',class_room='Room 3')
e.class_information()'''

'''
class Bank:
    def __init__(self):
        self.blance=0.00
        
    def deposit(self,amount):
        
        print(f'Before Deposit Blance is {self.blance}')
        self.blance+=amount
        #self.balance=self.blance+amount
        print(f'After Deposit total balance is {self.blance}')
        
    def withdraw(self,amount):
        #self.blance-=amount
        self.blance=self.blance-amount
        print(f'After Withdraw total balance is {self.blance}')
b=Bank()
#b.balance=1000
Bank.blance=10000
print(b.blance) #0.0
b.deposit(5000) # 5000.0
b.withdraw(2500) # 2500.0

# here if we done modification in main class it will not effect for object because we done modification in main class not in object
'''