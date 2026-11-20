'''from abc import ABC, abstractmethod
class Hi(ABC):
    @abstractmethod
    def show(self):
        pass
h=Hi()
h.show() #raceback (most recent call last):
  #File "/Users/saifsayyad/Documents/GitHub/Python_Code/OOP'S/DAY 8/abstraction.py", line 6, in <module>h=Hi()
#TypeError: Can't instantiate abstract class Hi without an implementation for abstract method 'show''''

"""
######in method will be holding delarration part as well as 
# implement  part  is called concreat class
A method which is having declaraation & definition is called as Concreate method"""

"""
ABSTRACTION

Hiding the complexity of a features and displaying only the
The required property to the end-user is called ABSTRACTION.


Abstract Method

Sometimes we don’t Know about implementation,still we can declare a method,such types of methods are called abstract method, i.e abstract method has only declaration but not implementation

In python we can declare abstract method by using @abstractmethod decorator as follows


@abstractmethod
Def M1(self):
	Pass

@abstractmethod decorator present in abc module,hence compulsory we should import abc module,otherwise we will get error

abc – abstract base class module

Class Test:
	@abstractmethod
    Def M1(self):
		Pass

Name error abstract method not defined


From abc import *

Class Test:
	@abstractmethod
    Def M1(self):
		Pass


Abstract Class

Sometimes implementation of a class is not a complete,such type of partially implementation classes are called abstract classes Every abstract class in Python should be derived from ABC class which is Present in abc module


from abc import ABC
abc ---> module/file
ABC ---> ClassName
@abstractmethod ---> decorator



interface :
    * a class consist of pure abstract method is called as Interface
    (we don't have any concept as interface in python)
    
    

concrete method:

A method which is having declaration & definition is called
as Concrete method

def add(self)              --> declaration
   print('addition')       --> definition    
"""


#case--->01
#in the above code we can create object for Test class because it is concrete class and it does not
#contain any abstract method




#case-->02

# from abc import *
# class Test(ABC):
#     pass
#
# t=Test()

#in the above code we can create object,even it is derived from ABC class but doesn't contain any
#abstract method
#case-->03
# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def spam(self):
#         pass
#
# t=Test()
#TypeError: Can't instantiate abstract class Test with abstract method spam



#case-->04

# from abc import *
# class Test:
#     @abstractmethod
#     def spam(self):
#         print("hi")
#
# t=Test()
# t.spam()

#we can create object even class contains abstract method because we are not extending ABC class
'''
Example:--->01


class TEST(ABC):
    @abstractmethod
    def Subject1(self):
        pass

    @abstractmethod
    def Subject2(self):
        pass

    @abstractmethod
    def Subject3(self):
        pass


class Test2(TEST):

    def Subject1(self):
        print("my first subject is PYTHON")

    def Subject2(self):
        print("my second subject is SQL")

    def Subject3(self):
        print("my third subject is Selenium")

t=Test2()
t.Subject1()
t.Subject2()
t.Subject3()
'''



'''example:-->02


from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def Balance(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdrawal(self,amount):
        pass

class ATM(Bank):
    def __init__(self,cname,bal):
        self.name=cname
        self.bal=bal


    def Balance(self):
        print(f' total available balance is {self.bal}')


def deposit(self,amount):
        print(f' total available balance is {self.bal}')
        self.bal+=amount
        print(f' after depositing total amount is  {self.bal}')
def withdrawal(self,amount):
        print(f' total remains balance is {self.bal}')
        self.bal-=amount
        print(f' after withdrawal remains balance is {self.bal}')

a=ATM("Ravi",10000)
a.Balance()
print()
a.deposit(5000)
print()
a.withdrawal(4000)
print()

'''
"""
output:--->

 total available balance is 10000

 total available balance is 10000
 after depositing total amount is  15000

 total remains balance is 15000
 after withdrawal remains balance is 11000
"""
