'''class Dad:
  def Property(self):
    print("dad's Property")


class Child1(Dad):
  def Bike(self):
    print("Bike Class")


class Child2(Dad):
  def Car(self):
    print("car Class")

class Child3(Dad):
  def Plane(self):
    print("Plane class")



c1=Child1()
c1.Property()
c2=Child2()
c2.Property()
c3=Child3()
c3.Property()
'''
'''class Dad:
  def Property(self):
    print("dad's Property")


class Child1(Dad):
  def Bike(self):
    print("Bike Class")


class Child2(Dad):
  def Car(self):
    print("car Class")

class Child3(Dad):
  def Plane(self):
    print("Plane class")



c1=Child1()
c1.Property()
c1.Bike()
c2=Child2()
c2.Property()
c2.Car()
c3=Child3()
c3.Property()
c3.Plane()'''


'''class Dad:
  money="1lac+villa"
  def Property(self):
    print("dad's Property")


class Child1(Dad):
  def Bike(self):
    print("Bike Class")


class Child2(Dad):
  def Car(self):
    print("car Class")

class Child3(Dad):
  def Plane(self):
    print("Plane class")



c1=Child1()
c1.Property()
c1.Bike()
c2=Child2()
c2.Property()
c2.Car()
c3=Child3()

c3.Plane()'''






'''class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
class C(A):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
class D(B,C):
    def student_data(self,name,age,sub,roll_no):
        self.sub=sub
        self.roll_no=roll_no
        B.student_data(self,name,age,sub,roll_no)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student Roll Number is {self.roll_no}')
    
d=D()
d.student_data("Aman",23,"Python","P1234")
'''



'''
class T:
    def subject(self):
        print("Python")
class U(T):
    def subject(self):
        print("Java")
    super().subject()
class V(T):
    def subject(self):
        print("C++")
class W(T):
    def subject(self):
        print("C#")
        
s=W()
s.subject()
ss=V()
ss.subject()
sss=U()
sss.subject()
ssss=T() 
ssss.subject()
# this last wala is not vaild because it is not a child class of T, so it will not be able to access the subject method of T class.

'''