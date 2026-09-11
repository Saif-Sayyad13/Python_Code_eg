'''
class Dad:
    cash=100000
    def villa(self):
        print("Dad's villa")

class Child(Dad):
    bike_name="Bmw"
    def Home(self):
        self.cash=900
        print(self.cash)
        print("Dad's Gift")

'''

'''
print(dir(Dad))
print()
print(dir(Child))
'''
'''

d=Child()
print(d.cash)
d.villa()
d.Home()
'''

'''
class Dad:
    def spam(self):
        print("spam method")

class Child(Dad):
    def spam(self):
        # Dad.spam(self)
        super().spam()
        print("child method")
c=Child()
c.spam()
'''

'''

class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,sub,usn):
        self.sub=sub
        self.usn=usn
        # super().student_data("XYZ",24)
        A.student_data(self,"ABC",17)
        print(f'subject Name is {self.sub}\n'
              f'student USN number is {self.usn}')

b=B()
b.student_data("Python","P1234")
'''

'''

class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,name,age,sub,usn):
        self.sub=sub
        self.usn=usn
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student USN number is {self.usn}')

b=B()
b.student_data("AB",24,"Excel","P1234")
'''
'''
class Test:
    def __init__(self):
        print("C1")

class Data(Test):
    def __init__(self):
        super().__init__()
        Test.__init__(self)
        print("C2")
d=Data()
'''


'''
class Company:
    def __init__(self,name,sal,yop):
        self.name=name
        self.sal=sal
        self.yop=yop

    def Data(self):
        print(f'employee name is {self.name}\n'
              f'total salary is {self.sal}\n'
              f'yop is {self.yop}')

class Information(Company):
    def __init__(self,eid,role,add):
        self.eid=eid
        self.role=role
        self.add=add
        super().__init__("Rahul",45000,5)

    def Data(self):
        super().Data()
        print(f'employee id is {self.eid}\n'
              f'Role is {self.role}\n'
              f'current address is {self.add}')

i=Information("R13","Analysis","Pune")
i.Data()

'''




"""class Dad:
    cash=10000
    def villa(self):
        print("Dad's villa")
class Child(Dad):
    bike_name="BMW"
    def Home(self):
        print("Dad's Gift")
        
print(dir(Dad))
print(dir(Child))
'''d=Child()
d.villa()
d.Home()
print(d.cash)'''
"""
'''
class Dad:
    def spam(self):
        print('spam method')
   
class Child(Dad):
    def spam(self):
        #Dad.spam(self)
        super().spam()
        print('child method')
c=Child()
c.spam()
     
     
# parent class all  data if we wan tot access into child we take done by supper function
# method overloading using same functioon name in two class but it will excuate latest one because python is dynamic launaguage'''