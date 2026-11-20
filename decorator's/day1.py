'''
normal dctorater

def outer(func)
    def inner(*args,**kwargs):
        statement ------beforee exection
        func(*args,**kwargs):
        statement --after excetion
        
    return inner
@outer

def mainfuntion(para):
    statement
mainfunction(arguments)
    
        
'''



'''
parametries dectore

def outer_most(parameter):
    def outer(func):
        def inner(*args,**kwargs):
            startement
            func(*args,**kwargs)
        return inner
    return outer

@outer_most(argumment)

def main_function(paratemeter):
    statement
main_function(arguments)

'''

'''
import time
time.sleep(number t will be seconds)

'''

'''
execution time

start=time.time()--- current time of the system (before execution of the mainfunction)

end= time.time()------current time of the system(after execution the mainfuntion)

print(end-start)

'''

# def outer_most(x):
#     def outer(func):
#         def inner(a,b):
#             print(x)
#             func(a,b)
           
#         return inner
#     return outer
# @outer_most("Addition")
# def add(a,b):
#     print(a+b)
# add(10,20)
# @outer_most("Subtraction")
# def sub(a,b):
#     print(a-b)  
# sub(10,20)
# @outer_most("Multiplication")
# def mul(a,b):
#     print(a*b)
# mul(10,20)
# @outer_most("Division")
# def div(a,b):
#     print(a/b)
# div(10,20)


'''#1.write a decorator function that prints "HELLO EVERYONE" message before execute any function
def outer(func):
    def inner(a,b):
        print('Hello Everyone')
        func(a,b)
        print('Function executed successfully')
    return inner
@outer
def don(a,b):
    print(a+b)
don(10,20)'''

'''#2.write a decorator function to print main function name before executing any decorator function
def outside(func):
    def inside(*args,**kwargs):
        print(f'Function name is: {func.__name__}')
        func(*args,**kwargs)
    return inside
@outside
def main_function(a,b):
    print(a+b)
main_function(10,20)'''

'''#3.write a decorator which inputs 5 seconds of delay before executing any decorator function
import time
def outer(func):
    def inner(a,b):
        time.sleep(5)
        func(a,b)
    return inner
@outer
def don(a,b):
    print(a+b)
don(10,20)
'''
'''#4.write a decorator function calculate the execution time of any function
import time
def outer(func):
    def inner(a,b):
        start=time.time()
        func(a,b)
        end=time.time()
        print(f'Execution time is: {end-start}')
    return inner
@outer
def add(a,b):
    print(a+b)
add(10,20)'''

'''#5.write a decorator to check if the 1st arguments is lesser than 2nd argument if then swap them 
#and perform division but the condition is you should not modify the original function

def outer(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return inner
@outer
def div(a,b):
    print(a/b)
div(10,20)'''



'''# 6.wadf to add 2 numbers and display the message before "i am doing addition operation"
# after performing print the message "addition operation is done"
# o/p--->i am doing addition operation"value "addition operation is done
def outer(func):
    def inner(a,b):
        print(" i am doing addition operation")
        func(a,b)
        print("addition operation is done")
    return inner
@outer
def add(a,b):
    print(a+b)
add(10,20)'''

'''# 7.create a decorator to return only positive out from any subtraction
def outer(func):
    def inner(a,b):
        result=func(a,b)
        if result<0:
            result*=-1
        print(result)
    return inner
def sub(a,b):
    return a-b
sub=outer(sub)
sub(10,20)
'''
'''# 8.create a decorator which counts the number of function calls
def outer(func):
    count=0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print(f'Function called {count} times')
        func(*args,**kwargs)
    return inner
@outer
def add(a,b):
    print(a+b)
add(10,20)
add(30,40)
add(50,60)

#or
count=0
def outer(func):
    def inner(*args,**kwargs):
        global count
        count+=1
        print(f'Function called {count} times')
        func(*args,**kwargs)
    return inner
@outer
def add(a,b):
    print(a+b)
add(10,20)
add(30,40)
add(50,60)
add(70,80)
add(90,100)'''


# 9.wap to sum of the positional arguments and get the length of the keywords arguments


# 10.write a decorator function to print the type of datatype before performing the action

# 11.write a decorator operation on the given number and the condition is A>B then perform multiplication in decorator function else
#  cube it in decorator

# 12.create a decorators to which prints name of called main function and counts the function calls

# 13.create a decorators to which prints names of called functions and checks the number is even or odd

# 14.create a decorator which delays its execution as per user input

# 15.write a multilevel decorator to log some message

# 16.write a multilevel decorators to accept username and register number of employee

# 17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS ,
#  DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER

# 18 using 3 decorators show me one example
 