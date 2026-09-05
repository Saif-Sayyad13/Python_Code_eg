'''class Student:    # className--------Student
    
    """Student Class INformation"""# this is desprition of class is called as dockstring
    name="Aman"    # classvaraible------name age total_sub
    age=22
    total_sub=5
s=Student() #        object_creatioon
print(Student.__doc__) #        only to print dicperatioon of class
help(Student) #         help(ClassName)


'''
'''print(name)


print(age)
print(total_sub)
# inside the class what everevr data we pass we cont access outside 
#if we do its should Name erroe'''
# to access class data outside we have 2 ways 
"""
How to access class varaible DAta outside 

here we have two way
1. By using ClassName
2. By using object
"""
"""
#.1,By using classname
print(' accessing data by the help of ClassName')
print(Student.name)
print(f'Student name is {Student.name}')
print(Student.age)
print(Student.total_sub)

#2.By using Object
print(' accessing data by the help of object')
print(s.name)
print(f'Student name is {s.name}')
print(s.age)
print(s.total_sub)



'''when ever we are creating class how it will in internally'''
print(Student.__dict__) # {key:value}   // {'__module__': '__main__', 'name': 'Aman', 'age': 22, 'total_sub': 5, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
print(s.__dict__) # {}
# this __dict__ is called magic methood 
'''
access modifier
a=10-----public
_a=10-----protected
__a=10-----private
__a__-------magic methods
'''
"""

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




