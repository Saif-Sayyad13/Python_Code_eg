'''
class One:
  a=900    #-------->public
  def spam(self):
    print(self.a)
    print(One.a)

s=One()
print(s.a)
s.spam()
'''
'''class One:
  a=900    #-------->public
  def spam(self):
    print(self.a)
s=One()
s.a=1000
print(s.a)
'''
'''class One:
  a=900    #-------->public
  def spam(self):
    print(self.a)
s=One()
# s.a="Python"
One.a="Java"
s.spam()'''

'''class One:
  a=900    #-------->public
  def spam(self):
    print(One.a)
s=One()
s.a="Python"
# One.a="Java"
s.spam()'''

'''class Data:
  _pin=1234

  def Pin_Information(self):
    print(f'SBI Card Pin number is {self._pin}')


  def PIN_Change(self,new_pin):
    self._pin=new_pin
    print(f'SBI Card NEW Pin number is {self._pin}')

x=Data()
print(x._pin) #1234
x.Pin_Information()
x.PIN_Change(4567)'''


'''class Data:
  _pin=1234

  def Pin_Information(self):
    print(f'SBI Card Pin number is {self._pin}')


  def PIN_Change(self,new_pin):
    self._pin=new_pin
    print(f'SBI Card NEW Pin number is {self._pin}')

x=Data()
x._pin=1001
print(x._pin) #1234'''

'''class A:
  x=90
  _name="Python"
  def data(self):
    print("A Class Data")

class B(A):
  def show(self):
    print(self.x)
    print(self._name)
    print("B Class Data")

b=B()
b.show()
b.data()'''

'''class School:
  def __init__(self,name,age,grade):
    self.name=name
    self._age=age
    self._grade=grade


  def Getter(self):
    return self.name,self._age,self._grade


  def Setter(self,new_name,new_age,new_grade):
    self.name=new_name
    self._age=new_age
    self._grade=new_grade

s=School("Rohit",23,"A")
s.Setter("virat",44,"S")
print(s.Getter())'''


'''
class School:
  def __init__(self,name,age,grade):
    self.name=name
    self._age=age
    self._grade=grade


  def Getter(self):
    return getattr(self,"name","Name is deleted"),getattr(self,"_age","age data is deleted"),getattr(self,"_grade","Grade_data_is_deleted")


  def Setter(self,name,age,grade):
    self.name=name
    self._age=age
    self._grade=grade


  def Deleter(self):
    del self.name
    del self._age
    del self._grade

s=School("Rohit",23,"A")
s.Setter("XYZ",22,"B")
s.Deleter()
print(s.Getter())

'''

'''class School:
  def __init__(self,name,age,grade):
    self.name=name
    self._age=age
    self._grade=grade


  def Getter(self):
    return getattr(self,"name","Name is deleted"),getattr(self,"_age","age data is deleted"),getattr(self,"_grade","Grade_data_is_deleted")


  def Setter(self,name,age,grade):
    self.name=name
    self._age=age
    self._grade=grade


  def Deleter(self):
    del self.name
    del self._age
    del self._grade

s=School("Rohit",23,"A")
s.Setter("XYZ",22,"B")
s.Deleter()
print(s.Getter())'''

'''class Check:
  __x=1000

  def show(self):
    print(self.__x)

c=Check()
c.show()
'''
'''class Check:
  x=1000

  def show(self):
    print(self.x)

c=Check()
c.show()
print()
print(Check.__dict__)'''

'''class Check:
  _x=1000

  def show(self):
    print(self._x)

c=Check()
c.show()
print()
print(Check.__dict__)'''

'''class Check:
  __x=1000

  def show(self):
    print(self.__x)

c=Check()
c.show()
print()
print(Check.__dict__)'''


'''class Check:
  __x=1000

  def show(self):
    print(self.__x)

c=Check()
print(c._Check__x)
print(Check._Check__x)
'''


'''class Check:
  __x=1000
  def show(self):
    print(self.__x)

class Think(Check):
  def Data(self):
    # print(self.__x)       #Through object it will show Error
    print(Check._Check__x)  #Through_Class Directly

t=Think()
t.Data()
print(Think.__dict__)'''


'''class Bank:
  def __init__(self,name,acc_num,bal):
    self.name=name
    self._acc_num=acc_num
    self.__bal=bal


  def Getter(self):
    print(getattr(self,"name","Name is deleted "),
          getattr(self,"_acc_num","account Number is Deleted "),
          getattr(self,"_Bank__bal","Balance is Deleted "))


  def Setter(self,name,acc_num,bal):
    self.name=name
    self._acc_num=acc_num
    self.__bal=bal


  def Deleter(self):
    del self.__bal

b=Bank("Manu",123453245,90000)
b.Setter("Kiran",897654236,50000)
b.Deleter()
b.Getter()'''


'''class Employee:
  def __init__(self,age):
    self.age=age

  @property
  def data(self):
    return getattr(self,"age","deleted")

  @data.setter
  def data(self,age):
    self.age=age

  @data.deleter
  def data(self):
    del self.age


e=Employee(23)
e.data=34
del e.data
print(e.data)'''


'''class Employee:
  def __init__(self,age,name,sal):
    self.age=age
    self.name=name
    self.sal=sal

  @property
  def data(self):
    return getattr(self,"age","deleted"),getattr(self,"name","name is deleted"),getattr(self,"sal","deleted")

  @data.setter
  def data(self,a):  #in modification Part we can use only one Parameter if we use multiple unable to unpack the data
      self.age,self.name,self.sal=a


  @data.deleter
  def data(self):
    del self.age
    del self.name


e=Employee(23,"ABC",5000)
e.data=(35,"xyz",10000)
del e.data
print(e.data)'''

"""
class Employee:
  def __init__(self,age,name,sal):
    self.age=age
    self.name=name
    self.sal=sal

  @property
  def data(self):
    return getattr(self,"age","deleted"),getattr(self,"name","name is deleted"),getattr(self,"sal","deleted")

  @data.setter
  def data(self,a):  #in modification Part we can use only one Parameter if we use multiple unable to unpack the data
      self.age,self.name,self.sal=a

      '''
      self.age=a[0]
      self.name=a[1]
      self.sal=a[2]
      '''

  @data.deleter
  def data(self):
    del self.age
    del self.name


e=Employee(23,"ABC",5000)
e.data=(35,"xyz",10000)
print(e.data)

"""
'''class Bank:
    def __init__(self,name, account_No, balance):
        self.name=name
        self._account_No=account_No
        self.__balance=balance
        
    def Getter(self):
        print(getattr(self,'name',"Name is deleted 😂\n"),
              getattr(self,"_account_No","Account Number is deleted 😭\n"),
              getattr(self,'__balance',"Balace is deleted 😭😭😭😭"))
        
    def Setter(self,name,acc_no,bal):
        self.name=name
        self._account_No=acc_no
        self.__balance=bal
        
        
    def Deleter(self):
        del self.__balance
        
b=Bank("Aman","1234567890",'987654321234567898765432')
b.Setter('Raju\n','45\n','908')
b.Deleter()
b.Getter()
       

""" This all getter setter and deleter are all java concept  """
        '''
   
   
        
"""
        
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @property
    def data(self):
        return getattr(self,'name','deleted name'), getattr(self,'age','deleted age')
    
    @data.setter
    def data(self,new_name,new_age):
        self.name=new_name
        self.name=new_age
        
    @data.deleter
    def data(self):
        del self.name
        del self.age
        
e=Employee('xyz',23)
print(e.data)
e.data=('abc',24)
del e.data
print(e.data)

'''.  in @ property we only can able to persorm 1 parameter if we
have to do you has be assign one parameter in to steert methods  '''

"""