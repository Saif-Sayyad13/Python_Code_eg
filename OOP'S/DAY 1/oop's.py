
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
Pascal Case ---->FirstwordFirst latter uppercase and second word first letter uppercase
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
Two ways------->1.By useing Class Name
                2.By useing object
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










"""class Employee:
    '''Employeeee Informations'''
    ename="Avii"
    eid="A12"
    yop=5
    sal=10000
e=Employee()
# print(Employee.__doc__)
help(Employee)

"""




 



'''class Don:
    a=99
    b=999
t=Don()
t1=Don()

print("Before Modification")
print(Don.a)
print(t.a)
print(t1.a)
print()
Don.a=100
print("After Modification")
print(Don.a)
print(t.a)
print(t1.a)

print()

print("Before  Modification in Object ")
print(Don.a)
print(t.a)
print(t1.a)
print()

t.a=500
print("After   Modification in Object ")
print(Don.a)
print(t.a)
print(t1.a)
print()


Don.a=20
print("Again   Modification in Class ")
print(Don.a)
print(t.a)
print(t1.a)
print()
'''

