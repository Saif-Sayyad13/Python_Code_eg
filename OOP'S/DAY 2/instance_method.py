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