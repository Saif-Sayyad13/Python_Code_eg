"""
How To create empty Class---->???

How To create object------>????

"""
"""
#How To create empty Class---->???
class ClassName:
    pass

class-----> keyword
ClassName---> Name of the class
pass----->keyword (no operations)
Pasal---->FirstwordFirst latter uppercase and second word first letter uppercase
"""
"""

How To create object------>????

new_var=ClassName()

Reference_variable------>> Any variable Refere to the
object then we can call it as a 
Reference_variable
"""










'''
class Morning:
    x=900   #class variable

m=Morning()
print(m) #<__main__.Morning object at 0x000001D091851670>

m1=Morning
print(m1) #<class '__main__.Morning'>
'''





class Morning:
    x=900   #class variable
    y=200  #class Variable
m=Morning()

'''
#How to access Inside class Data outside
print(x)  #NameError
print(y)  #NameError

'''
'''
#By useing Class Name
print(Morning.x)
print(Morning.y)

#By useing Object
print(m.x)
print(m.y)
'''


"""
when we create the Class inside the class if we
store any data  we can access outside by useing
Two ways------->http://1.By useing Class Name
                http://2.By useing object
"""
'''
print(Morning.__dict__)
print()
print(m.__dict__) #{}
'''

'''
class Pen:
    a=10   #class Variable
    b=20   #class variable

p=Pen()    #object1
p1=Pen()  #object2

"""
Point--->1
If we done anymodification in Main Class it will
effected for Both object
syntax :---> ClassName.var_Name=value
"""
print("Before Modification")
print(Pen.a)
print(p.a)
print(p1.a)
print("After Modification")
Pen.a=100
print(Pen.a)
print(p.a)
print(p1.a)
print("Before Object Modification")
print(Pen.a)
print(p.a)
print(p1.a)
print("After Object Modification")
p.a=900
print(Pen.a)
print(p.a)
print(p1.a)

print("Again Modification In Main Class")
Pen.a=1000
print(Pen.a)   #1000
print(p.a)     #900
print(p1.a)   #1000


"""
Point--->3
again we done modification In main class it will
effected for Main class and other object but it will
won't effected for Previous Modification object
because when we done separate Modification internally
it will create separated memorylocation
(connection loss)

'''



"""
























'''
#Address of the Class and object and class Variable
print(id(Pen)) #2221280202544
print(id(p))  #1974956286960
print(id(p1)) #2118822421872
print(id(p.a))#140716491930328
print(id(p.b)) #140716491930648
'''
"""










class Employee:
    '''Employeeee Informations'''
    ename="Avii"
    eid="A12"
    yop=5
    sal=10000
e=Employee()
# print(Employee.__doc__)
help(Employee)







'''
class Demo:
    def spam(self):
        print("welcome To All")

d=Demo()
d.spam()   #d.spam(d)
Demo.spam(d)
'''


'''
class Joy:
    def spam(self):
        print(self)
j=Joy()
print(j)
j.spam()
'''
print()

'''
class Joy:
    def spam(x):
        print(x)
j=Joy()
print(j)
j.spam()
'''

'''
class School:
    name="Pyspiders"  #class variable
    def Data(self):
        print("working")
        print("Accessing Class variable by useing Class name")
        print(http://School.name)
        print("Accessing Class variable by useing object")
        print(http://self.name)
        # print(name) #NameError:
s=School()
http://s.Data()
'''





'''
#way----->01
class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {self.sub}')
s=Student()

#Modification by useing Class Name
# Student.sub="Python"

#Modification by useing Object
s.sub="Python_and_Sql"
s.subject_name()
'''

'''
#way--->02

class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {Student.sub}')
s=Student()

#Modification by useing Class Name
Student.sub="Python"

#Modification by useing Object
# s.sub="Python_and_Sql"
s.subject_name()
'''

"""
Note :--->
if we access class variable by useing self object
if we done Modification by useing class_Name and
object it will effected

if we access class variable by useing ClassName
if we done Modification by useing class_name it 
will effected but if we done Modification by useing
object it will won't effected.

"""






'''class don:
    c=100
    def kon(self):
        print(don.c)    # her we are accessing 
s=don()
print(s.c)
'''


'''

class student:
    def info(self):
        self.name="aman"
        self.age=23
        self.rollno=122
        self.data()
    
    def data(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
        #self.info()
s=student()
s.info()

print()

s.data()
print()
s.age=232
s.data()
print()

s.data()'''
