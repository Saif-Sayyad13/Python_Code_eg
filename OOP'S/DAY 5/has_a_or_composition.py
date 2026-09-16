'''class Hi:
  def demo(self):
    print("demo class")

class Hello:
  def spam(self):
    x=Hi()
    x.demo()
    print("spam class")


h=Hello()
h.spam()'''

'''
class Hi:
  y=9000
  def demo(self):
    print("demo class")

class Hello:
  def spam(self):
    x=Hi()
    x.demo()
    print(x.y)
    print("spam class")


h=Hello()
h.spam()


'''
'''
class Employee:
  def data(self,sal,eid,age):
    self.sal=sal
    self.id=eid
    self.age=age
    print(f'total sal is {self.sal}')
    print(f'employee id is {self.id}')
    print(f'Current age is {self.age}')

class Information:
  def employee_data(self,role,name,yoe):
    self.role=role
    self.name=name
    self.yoe=yoe
    y=Employee()
    # y.data(450000,"R15",35)   #By useing object
    Employee.data(y,50000,"R45",33) #by useing className
    print(f'employee Role is {self.role}')
    print(f'employee Name is {self.name}')
    print(f'Total experience is {self.yoe}')


i=Information()
i.employee_data("DataScience","Rolex",10)
'''

'''

class Test:
  def __init__(self):
    print("First class")

class Two:
  def __init__(self):
    self.x=Test()        #---------->x=Test()
    print("second Class")

t=Two()


'''

'''
class Test:
  sub="Python"
  def __init__(self):
    print("First class")

class Two:
  def __init__(self):
    self.x=Test()        #---------->x=Test()
    print(self.x.sub)
    print("second Class")

t=Two()
'''

'''
class School:
  def __init__(self,sub1,sub2,sub3,total):
    self.sub1=sub1
    self.sub2=sub2
    self.sub3=sub3
    self.total=total

  def data(self):
    print(f'First subject name is {self.sub1}')
    print(f'second subject name is {self.sub2}')
    print(f'Third subject name is {self.sub3}')
    print(f'total all subject score is {self.total}')

class Trainer:
  def __init__(self,sname,Grade,result):
    self.sname=sname
    self.grade=Grade
    self.result=result
    self.Q=School("Python","Excel","PowerBI",250)
    self.Q.data()
  def student_result_information(self):
    print(f'student name is {self.sname}')
    print(f'student Grade is {self.grade}')
    print(f'final Result is {self.result}')

t=Trainer("Rahul","F","Fail")
t.student_result_information()

'''
'''
class School:
  def __init__(self,sub1,sub2,sub3,total):
    self.sub1=sub1
    self.sub2=sub2
    self.sub3=sub3
    self.total=total

  def data(self):
    print(f'First subject name is {self.sub1}')
    print(f'second subject name is {self.sub2}')
    print(f'Third subject name is {self.sub3}')
    print(f'total all subject score is {self.total}')

class Trainer:
  Q=School("Python","Excel","PowerBI",250)
  Q.data()
  def __init__(self,sname,Grade,result):
    self.sname=sname
    self.grade=Grade
    self.result=result

  def student_result_information(self):
    print(f'student name is {self.sname}')
    print(f'student Grade is {self.grade}')
    print(f'final Result is {self.result}')


t=Trainer("Rahul","F","Fail")
t.student_result_information()

'''
