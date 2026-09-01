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