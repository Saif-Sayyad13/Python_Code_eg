
#default except block
a=[1,2,3]
try:
    print(a.upper())
except:
    print('error')
    
a=[1,2,3]
try:
    print(a.upper())
except AttributeError:
    print('error')
    
# multiple except block
a=[1,2,3]
try:
    print(a.upper())
except (AttributeError,ZeroDivisionError,NameError,TypeError):
    print('error')
# also can be writtenn it like
a=[1,2,3]
try:
    print(a.upper())
except AttributeError:
    print('error')
except ZeroDivisionError:
    print('error')
except NameError:
    print('error')
except TypeError:
    print('error')
    
# gereric except block
a=[1,2,3]
try:
    print(a.upper())
except Exception as e:
    print('error',e)

a="abc"
try:
    print(a.upper())
except Exception as e:
    print('error',e)


# multiple except block with else and finally
try:
    print(a.upper())
except:
    print('error')
else:
    print('no error')

a=[1,2,3]
try:
    print(a.append(4))
except:
    print('error')
else:
    print('no error')
    
a=[1,2,3]
try:
    print(a.upper())
except:
    print('error')
finally:
    print('this is finally block')

a=[1,2,3]
try:
    print(a.append(4))
except:
    print('error')
else:
    print('no error')
finally:
    print('this is finally block')
'''
Exception handling

In any programming Language there are 2 types of error are possible

1.syntax Errors

2.Runtime Errors


1.syntax Errors

The  errors which occur because of invalid syntax are called syntax errors


2.Runtime errors

While executing the program if something goes wrong because of end user input or programming logic or memory Problem etc then will get Runtime Error



Exception:-


An unwanted and unexpected event that disturbs normal flow of program is called Exception
               OR


an event which triggers/occurs suddenly/abruptly during execution of the program is called an exception.




*handling this kind of event during program execution is called exception handling.


*We can handle the exception by using the "try" and "except" block.


*an event which will stop/terminate the program execution.
*types of except block
=====================
1.default except block
2.specific except block
3.generic except block
4.multiple except block


try block:-
-----------
which line/block of code will get exception/error should present in "try" block


except block:-
--------------
*except block will execute only when exception occurs.


*here will handle the exception.


*when ever we are writing try block it is mandatory to write except block
"""


exception on exception occurs without handling
a = 10
b = 0
print(a/b)
print("in python exception handling")


"""
print(a/b)
ZeroDivisionError: division by zero
"""
#1.default except block:
# ======================
"""
*we will go default except block when we don't know what kind of exception occurs.
syntax:
-------
try:
   statement
except:
   statement
"""


example on handling exception
a = 10
b = 0
try:
   print(a/b)
except:
   print("exception handled")


print("in python exception handling")


example on no exception Occured
a = 10
b = 2
try:
   print(a/b)
except:
   print("exception handled")


print("in python exception handling")


example on name error
a = 10
b = 2
try:
   print(a * c)
except:
   print("we are handling name error")
print("end of program")


example on zero division and name error
a = 10
b = 0
try:
   print(a * c)         #name error
   print(a / b)        #zero division error
except:
   print("we are handling name error")


print("end of program")


# 2.specific except block
"""
*in specific except block, except block will get executed only when the specified exception is mentioned in except block.
syntax:
-------
try:
   statement
except exception_name:
   statement
"""


a = 10
b = 0
try:
   print(a / b)        #zero division error
except ZeroDivisionError:
   print("we are handling name error")


print("end of program")




a = 10
b = 0
try:
   print(a / c)        #Name error
except ZeroDivisionError:
   print("we are handling name error")
print("end of program")


"""
NameError: name 'c' is not defined
"""


a = 10
b = 0
try:
   print(a / c)        #Name error
except NameError:
   print("we are handling name error")


print("end of program")




a = 10
b = 0
try:
   print(a / c)        #Name error
   print(a / b)
except NameError:
   print("we are handling name error")


print("end of program")
"""
note:
-----
*as per above example 1st we will get "nameerror" and it will handled in except block, but in 2nd line of try block
will get "zerodivisionerror" it will not execute at all.




*because once when we get error,it will stop the execution there itself and it will handle in "except" block, again
it will not come and continue the execution in the "try" block.
*so it is better to write single line/which line will get exception in "try" block
"""


a = 10
b = 0
try:
   print(a / b)        
   print(a / c)
except NameError:
   print("we are handling name error")


print("end of program")


"""
ZeroDivisionError: division by zero
"""








#3.multiple except block
"""
*For a single "try" block we will write multiple "except" blocks.


*Once the exception is handled then the remaining "except" block will get ignored.
syntax:
-------
try:
  statement
except exception1:
  statement
except exception2:
  statement
except exception3:
  statement


note:
----
we can optimize by writing multiple exception in single "except" block, instead of writing multiple "except" block
syntax:
------
try:
 statement
except (exception1, exception2,...):
 statement


"""


a = 10
b = 0


try:
   print(a / b)


except NameError:
   print("handling name error")
except ZeroDivisionError:
   print("handling division error")


"""
handling division error
"""
l = [10, 20]
try:
   print(l.upper())        #AttributeError


except NameError:
   print("handling name error")
except ZeroDivisionError:
   print("handling division error")
except AttributeError:
   print("handling AttributeError")


handling AttributeError
l = [10, 20]
try:
   print(l.upper())        #AttributeError


except NameError:
   print("handling name error")
except ZeroDivisionError:
   print("handling division error")
except TypeError:
   print("handling type error")


"""
AttributeError: 'list' object has no attribute 'upper'
"""


l = [10, 20]
try:
   print(l.upper())        #AttributeError


except AttributeError:
   print("handling name error")
except AttributeError:
   print("handling division error")
except AttributeError:
   print("handling type error")


handling name error




l = [10, 20]
try:
   print(l.upper())        #AttributeError


except (NameError,ZeroDivisionError,AttributeError):
   print("handling exception")








#4.generic except block
"""
"handles all types of exceptions in a single except block.
syntax:
-------
try:
 statement
except BaseException/Exception as msg:
 statement


"""


a = 10
b = 0
try:
   print(a/b)
except Exception:
   print("exception handling")


a = 10
b = 0
try:
   print(a/b)
except BaseException:
   print("exception handling")


"""
"as" keyword
------------
*used to give an alias name for the exception name written in the except block.
syntax:
-------
except <exception-name> as alias-name


->exception-name : can be any exception name
->alias-name : it can be any name
"""


a = 10
b = 0
try:
   print(a/b)


except BaseException as x:
   print("exception handling")
   print(x)




#nested try-except block
"""
try:
  try:
    stmt
except:
    stmt
except:
  stmt
"""


b = 2
try:
   print(10/b)
   try:
       print(c)
   except NameError:
       print("handling name error")


except ZeroDivisionError:
   print("handling ZeroDivisionError")






"""
user defined exception:-
========================
when we want to develop/create user defined exception we follow below syntax
syntax:
-------
class user defined-exception-name(BaseException/Exception)
   ...


raise Exception-name("message")
"""


# class NegativeError(BaseException):
#     ...
#
#  raise NegativeError("passing negative number")






class NegativeNumberError(BaseException):
   ...


def check(no):
   if no < 0:
       raise NegativeNumberError
   else:
       print("no is positive")


check(3)
check(-2)


class Passwordlengthlessthan6(BaseException):
   ...


class EnterValidPassword(BaseException):
 ...


def password(pwd):
   if len(pwd) > 6:
 if pwd.isalnum():
           print("valid password")
       else:
           raise EnterValidPassword
   else:
       raise Passwordlengthlessthan6
password("abc2456#@$")

'''


