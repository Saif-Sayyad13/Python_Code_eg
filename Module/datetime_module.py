
# 2 Build in Modules

# datetime module
'''
import datetime
print(datetime.datetime.now())
'''


'''import datetime as d
s=d.datetime.now()
print(s)'''
'''
import datetime as d
s=d.datetime.now()
# x= s.strftime("%Y-%m-%d %H:%M:%S")
# x=s.strftime('%Y')
# x=s.strftime('%y')
# x=s.strftime('%d')
# x=s.strftime('%m')
# x=s.strftime('%H')
# x=s.strftime('%I')
# x=s.strftime('%M')
# x=s.strftime('%S')
# x=s.strftime('%s')
# x=s.strftime('%p')
# x=s.strftime('%A')
# x=s.strftime('%a')
# x=s.strftime('%B')
# x=s.strftime('%b')
# x=s.strftime('%j')

# print(x)'''


'''import datetime as d
s=d.datetime.now()
print(s.year)
print(s.month)
print(s.day)
print(s.hour)
print(s.minute)
print(s.second) 
print(s.microsecond)
'''

'''print(s.tzinfo)
print(s.weekday())
print(s.isoweekday())
print(s.isocalendar())
print(s.isoformat())
print(s.ctime())
'''
"""

1.now()
2.%d------>Day
3.%m------>month number
4.%Y----->four-digit year
5.%y----->Two-digit year
6.%H------>24 hour format
7.%I------>12-hour format
8.%M------>Minutes
9.%s------>Seconds
10.%p----->AM/PM
11.%A------>Full weekday
12.%a------>short weekday
13.%B------>Full month
14.%b----->short month
15.%J----->Day of year
""" 
'''import datetime as d
w=d.date(2030,1,13)
print(w)'''


# collections module in detiel we will learn i dsa currentely deque
'''from collections import deque
q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)  # Output: deque([0, 1, 2, 3, 4])
q.pop()
q.popleft()
print(q)  # Output: deque([1, 2, 3])
q.extend('abc')
print(q)  # Output: deque([1, 2, 3, 'a', 'b', 'c'])
q.extendleft('xyz')
print(q)  # Output: deque(['z', 'y', 'x', 1, 2, 3, 'a', 'b', 'c'])'''

'''# math module
import math
print(math.sqrt(16))  # Output: 4.0 
print(math.pi)  # Output: 3.141592653589793
print(math.factorial(5))  # Output: 120
print(math.gcd(12, 15))  # Output: 3'''

'''import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Output: Random choice from the list
print(random.random())  # Output: Random float between 0.0 and 1.0
print(random.shuffle([1, 2, 3, 4, 5]))  # Output: Shuffles the list in place
'''

'''import random as r
print(r.randint(1, 10))  # Output: Random integer between 1 and 10
print(r.random()) # Output: Random float between 0.0 and 1.0
print(r.randrange(1, 10, 2)) # Output: Random odd integer between 1 and 9
print(r.randrange(11)) 
print(r.choice([12,67,13,'Hi',4+5j])) # Output: Random choice from the list
print(r.choice('Hello')) # Output: Random character from the string
print(r.sample([1, 2, 3, 4, 5], 3)) # Output: Random sample of 3 elements from the list
print(r.sample('abcdef', 2)) # Output: Random sample of 2 characters from the string
print(r.sample(range(10), k=5)) # Output: Random sample of 5 elements from the range
# k is the number of elements to sample
print(r.shuffle([1, 2, 3, 4, 5])) # Output: Shuffles the list in place none whe have to do it like next wala
# s=[1,2,3,4,'hi,29']
# r.shuffle(s)
# print(s) # Output: Shuffles the list in place
print(r.uniform(1, 10)) # Output: Random float between 1.0 and 10.0
'''

'''import random as r
print(r.randint(10000,99999)) # Output: Random integer between 10000 and 99999
'''

"""
# generate random OTP
from random import *
def OTP():
    otp=' ' # this is for concatenation of string
    for i in range(4):
        otp=otp+str(randint(0,9))
    print(otp)
OTP()

"""

"""
# generate random 2 alpha 2 numeric 2 and 2 lower case char
from random import *
def OTP():
    otp=' ' 
    for i in range(2):
        otp=otp+str(randint(0,9))
    
    for j in range(2):
        otp=otp+chr(randint(65,90))
    
    for k in range(2):
        otp=otp+chr(randint(97,122))
    print(otp)
OTP()



# from random import *
# def OTP():
#     otp=[] 
#     for i in range(2):
#         otp.append(str(randint(0,9)))
    
#     for j in range(2):
#         otp.append(chr(randint(65,90)))
    
#     for k in range(2):
#         otp.append(chr(randint(97,122)))
#     shuffle(otp)
#     result=''.join(otp)
#     print(result)
    
# OTP()
"""

'''
# gtenerate random password or opt
import random as r
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(r.choice(characters) for _ in range(length))
    return password

print(generate_password(12))
# VvFqy=+C5HG; kuch bi aa sakta random
# u&M-dV@>54y>'''