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

'''
class A:
  ...
class B(A):
  ...
class C(A):
  ...
class D(B,C):
#class D(A,C):#TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C
  ...
  
d=D()
print(D.__mro__)'''
'''
class School:
  def demo(self,name):
    self.name=name
    print(f'School name is {self.name}')

class Teacher(School):
  def display(self,sub):
    self.sub=sub
    print(f'subject name is {self.sub}')
  
class Student(School):
  def Grade(self,marks):
    self.marks=marks
    print(f'Total marls is {self.marks}')
class Sports(Teacher,Student):
  def Play(self,game_name):
    self.game_name=game_name
    print(f'game namw is {game_name}')
    
s=Sports()
s.demo('ABC')
s.display('python')
s.Grade('A+')
s.Play('lala')'''
'''
class School:
    def __init__(self, name):
        self.name = name
  
    def show(self):
        print(f'School name is {self.name}')
    
class Teacher(School):
    def __init__(self, name, sub):
        School.__init__(self, name)  # Call parent directly
        self.sub = sub
    
    def display(self):
        print(f'Subject name is {self.sub}')
    
class Student(School):
    def __init__(self, name, marks):
        School.__init__(self, name)  # Call parent directly
        self.marks = marks
    
    def Grade(self):
        print(f'Student marks are {self.marks}')
    
class Sports(Teacher, Student):
    # This takes exactly 5 parameters (self + 4 strings)
    def __init__(self, school_name, sub, marks, game):
        # Explicitly pass the correct parameters to each parent constructor
        Teacher.__init__(self, school_name, sub)    # Wants: self, name, sub
        Student.__init__(self, school_name, marks)  # Wants: self, name, marks
        self.game = game
    
    def finalshow(self):
        print(f'Game name is {self.game}')

# Passing exactly 4 values (Python adds 'self' automatically to make 5)
s = Sports('ABC School', 'Python', 'A+', 'Cricket')

s.show()       # School name is ABC School
s.display()    # Subject name is Python
s.Grade()      # Student marks are A+
s.finalshow()  # Game name is Cricket
'''
'''
class Inst:
  def show(self,name):
    self.name=name
    print(f'Insta name is {self.name}')
class Student(Inst):
  def display(self,sname):
    self.sname=sname
    print(f'Student name is {self.sname}')
class Result(Student):
  def don(self,marks):
    self.marks=marks
    print(f'Total marks are {self.marks}')
class Teacher(Result,Student):
  def lala(self,sub):
    self.sub=sub
    print(f'sub name is {self.sub}')
    
c=Teacher()
c.lala("python")
c.don(99)
c.display('don')
c.show('Qspider')
  '''
  
class Insta:
  def __init__(self,name):
    self.name=name
    
  def show(self):
    print(f'Insta name is {self.name}')
class Student(Insta):
  def __init__(self, name,sname):
    super().__init__(name)
    self.sname=sname
  def display(self):
    print(f'Student name is {self.sname}')

class Result(Student):
  def __init__(self, name, sname, marks):
    super().__init__(name, sname)
    self.marks=marks
  
  def show1(self):
    print(f'Total marks are {self.marks}')
    
class Teacher(Insta,Student):
  def __init__(self, name,sub):
    super().__init__(name)
    self.sub=sub
  def show2(self):
    print(f'Subject name is {self.sub}')

x=Teacher("Qspider",'Python')
    