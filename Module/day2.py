
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