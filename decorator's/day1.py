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
#4.write a decorator function calculate the execution time of any function


#5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them 
#and perform division but the condition is you should not modify the original function

