'''
#with object creation  calling Classmethod
class Hotel:  #class creation
    @classmethod
    def display(cls):
        print("Hotel Class")

Hotel.display()

#with object creation calling Classmethod

class Hotel:  #class creation
    @classmethod
    def display(cls):
        print("Hotel Class")

h=Hotel()  #object_creation
h.display()
Hotel.display()
'''

'''
#Note:----> in class method cls is Pointing To the
#main class
class Hii:
    @classmethod
    def spam(cls):
        print(cls )#<class '__main__.Hii'>
Hii.spam()
'''

'''
#object creation and cls Parameter
class Joy:
    @classmethod
    def show(cls):
        print(cls)  #<class '__main__.Joy'>
j=Joy()
print(j) #<__main__.Joy object at 0x000001D2E1134710>
print()
http://j.show()
'''

'''
#Class variable accessing into the class method
#by useing cls parameter.
class Car:
    name="BMW"  #class variable
    @classmethod
    def Data(cls):
        print(f'car Name is {http://cls.name}')
http://Car.Data()

##Class variable accessing into the class method
#by useing ClssName .

class Car:
    name="BMW"  #class variable
    @classmethod
    def Data(cls):
        print(f'car Name is {http://Car.name}')
http://Car.Data()
"""
Note:--->How To access Class Variable into the class method..???
we Have two ways  http://1.by useing cls Parameters
                  http://2.By useing ClassName
"""
'''

'''
#Modification In class method by useing cls Parameter
class Student:
    name="Joy"
    sub="SQL"
    @classmethod
    def Show_Data(cls):
        # print(f'Student Name is {http://cls.name}\n'
        #       f'student subject Name is {cls.sub}')
        cls.name="Abhi"
        cls.sub="Python"
        print(f'Student Name is {http://cls.name}\n'
              f'student subject Name is {cls.sub}')
Student.Show_Data()
'''

'''

#Modification In class method by useing className Parameter
class Student:
    name="Joy"
    sub="SQL"
    @classmethod
    def Show_Data(cls):
       
        # print(f'Student Name is {http://Student.name}\n'
        #        f'student subject Name is {Student.sub}')
        Student.name="Abhi"
        Student.sub="Python"
        print(f'Student Name is {http://cls.name}\n'
              f'student subject Name is {cls.sub}')
Student.Show_Data()
'''
'''
class School:
        fee=1000
        @classmethod
        def Data(cls):
                print(f'Total School Fee {cls.fee}')

        @classmethod
        def Updated_data(cls):
                School.fee=9000
                # print(f'Total School Fee {cls.fee}')
                print(f'Total School Fee {School.fee}')
x=School()
http://x.Data()
x.Updated_data()
'''

'''
class School:
        fee=1000
        @classmethod
        def Data(cls):
                print(f'Total School Fee {cls.fee}')

        @classmethod
        def Updated_data(cls,newfee):
                cls.fee=newfee
                print(f'Total School Fee {cls.fee}')
                print(f'Total School Fee {School.fee}')
x=School()
http://x.Data()
x.Updated_data(10000)

'''

'''
class Employee:
        yop="5year"
        @classmethod
        def Information(cls):
                print(f'Employee Total YOP {cls.yop}')

        @classmethod
        def data(cls,updated_yop):
                Employee.yop=updated_yop
                print(f'Total YOP is {Employee.yop}')
                print(f'Total YOP is {cls.yop}')
Employee.Information()
http://Employee.data("10year")
'''

'''
class Employee:
        yop="5year"
        @classmethod
        def Information(cls):
                print(f'Employee Total YOP {cls.yop}')
e=Employee()
'''
#class variable Modification outside
#by useing object
# e.yop=25
# print(e.yop)
'''
'''
#class variable Modification outside
#by useing ClassName
# print(e.yop)
# Employee.yop=55
# print(e.yop)
'''
e.Information() #5year
e.yop=60
e.Information() #5year
Employee.yop=100
e.Information()
'''
'''
class Amazon:
        Product="Pen"
        @classmethod
        def Show(cls):
                print(f'My product Name is {Amazon.Product}')

a=Amazon()
http://a.Show()
Amazon.Product="Marker"
http://a.Show()
'''
# print(a.Product)
# a.Product="Laptop"
# print(a.Product)
'''
'''
# print(Amazon.Product)
# Amazon.Product="Phone"
# print(Amazon.Product)

'''
class Check:
        x=1000
        @classmethod
        def spam(cls):
                print(cls.x)  #1000

        @classmethod
        def demo(cls,new):
                cls.x=new
                print(cls.x)
q=Check()
q.demo(500)
q.spam()
'''






'''
class A:
        @classmethod
        def Data(cls):
                print("Data Class")

        def spam(self):
                print("spam Class")

s=A()
http://s.Data()
http://A.Data()
s.spam()
A.spam(s)
'''



















'''

class Data:
        a=100
        @classmethod
        def show1(cls):
                print(cls.a)  #100

        @classmethod
        def demo(cls):
                x=cls()    #x=Data()
                x.a="Python"
                print(x.a)  #"Python"

        @classmethod
        def spam(cls):
                print(cls.a)   #100
d=Data()
d.show1()
d.demo()
d.spam()
'''











 


'''class Hotel:
    @classmethod
    def display(cls):
        print('Hotel Class')
Hotel.display()

# 
class Hotel:
    @classmethod
    def display(cls):
        print('Hotel Class')
a=Hotel()
a.display()
Hotel.display()
'''



"""# class varable accesiing into the class methods by usinf cls paramete
class Car():
    name="BMW"#class varaible any varaibe present in class
    @classmethod
    def Data(cls):
        print(f'car NAme is {cls.name}')
Car.Data()


# by using class method
class Car():
    name="BMW"
    @classmethod
    def Data(cls):
        print(f'car NAme is {Car.name}')
Car.Data()


'''
Note- In class method if we use class varable  How we are accesiing into class method

we have 2 ways :- 1. by using cls parameter
                  2. by using class name
'''

"""
'''
# modification in class methods 

class Student:
    name='aman'
    subject='python'
    
    @classmethod
    
    def Show_Data(cls):
        print(f'Student name is {cls.name}\n'
              f'Student subject Name is {cls.subject}')
        
        cls.name='kon'
        
Student.Show_Data()
    '''