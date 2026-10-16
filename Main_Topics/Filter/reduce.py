'''
Reduce function is used to apply a particular function passed in its argument to
all of the list elements mentioned in the sequence passed along. This function is
defined in "functools" module.
reduce(function, sequence[, initial]) -> value
*function: a function of two arguments.
*sequence: a sequence like a list, tuple, or string.
*initial: [optional] value that is provided as the initial value to the function.
If not provided, the first item of the sequence is used as the initial value.

'''



'''# using reduce in want answer addition of complte list with a single value
from functools import reduce
c=[10,20,30]
res=reduce(lambda x, y: x + y, c)
print(res)'''


'''
from functools import reduce
def sum(a,b):
    return a+b
a=[1,4,9,16]
res=reduce(sum,a)
print(res)
'''

'''from functools import reduce
def greatest(a,b):
    if a>b:
        return a
    else:
        return b
a=[10,45,77,92,101,40]
res=reduce(greatest,a)
print(res)'''

'''from functools import reduce
a=[10,45,77,92,101,40]
res=reduce(lambda x,y:x if x>y else y,a)
print(res)'''
'''
from functools import reduce
def sum(a,b):
    return a+b
a=[1,4,9,16]
res=reduce(sum,a,100) # here 100 is initializer is optional
print(res)
'''