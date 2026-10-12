'''
Comprehension Day 1
it is a simple way to write a collection or multiple lines of code in a single line
Comprehension is a concise way to create lists, dictionaries, or sets in Python. 
It allows you to generate these collections using a single line of code, making it 
more readable and efficient.
1. List Comprehension:
it is a elegant way to create or define a list based on existing lists or iterables. It consists of an expression followed by a for loop, and optionally, an if condition.
it will take string or tuple as a value and works on it like a list Data Type
to reduce / modify the resultant list we can use if condition statements in the list comprehension
we cant use any transfer statements like break, continue, or return in list comprehension
we cant usw while loop inside list comprehension because it is not allowed in list comprehension
only use for loop in list comprehension

Syntax:
1. [expression for item in iterable] /// [expression for i in collection]
2. [expression for item in iterable if condition] // 
3. [expression for item in iterable if condition1 if condition2]/// expression if condition1 else expression2 for item in iterable
'''
'''
normal way to find even numbers in a list
a=[1,2,3,4,5,6,7,8,9]
out=[]
for i in a:
    if i%2==0:
        out.append(i)
print(out)'''
'''
a=[1,2,3,4,5,6,7,8,9]
var=[i for i in a if i%2==0]
print(var)

print([i for i in eval(input("Enter a list of numbers: ")) if i%2==0])'''
'''
g=[1,2,3,4,5,6,7,8,9]
var=[i**2 if i%2==0 else i**3 for i in g]
print(var)

print([i**2 if i%2==0 else i**3 for i in eval(input("Enter a list of numbers: "))])

'''
'''print([i for i in range(1,21) if i%2==0])
print([i*2 for i in range(1,11) ])
print([i*3 for i in range(1,11) ])'''
#addition of two list using list comprehension

'''a=[10,20,40]
b=[40,50,60]
print([i+j for i,j in zip(a,b)])
print([a[i]+b[i] for i in range(len(a))])
'''

'''a=('hi','hello','bye')
print([i.upper() for i in a])
print([(i, a[i]) for i in range(len(a))])'''

