'''
#
def mul(x,y):
    return x*y
a=[10,20,30]
b=[1,2,3]
res=map(mul,a,b)
print(list(res))'''

'''def mul(n):
    return n*2
a=[5]
aa=map(mul,a)
print(set(aa))

a=lambda x:x*2
print(a(5))'''
'''
# range(1, 6) includes numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

text = "Learn Python step by step"
word_lengths = [len(word) for word in text.split()]
print(word_lengths)
# Output: [5, 6, 4, 2, 4]

inp = 'GOOD MORNING'
outp = {word: len(word) for word in inp.split()}
print(outp)
# Output: {'GOOD': 4, 'MORNING': 7}

import math

numbers = [3, 4, 5, 6]
factorials = [math.factorial(num) for num in numbers]
print(factorials)
# Output: [6, 24, 120, 720]

inp = 'PYTHON IS EASY'
outp = {word: word.lower() for word in inp.split()}
print(outp)
# Output: {'PYTHON': 'python', 'IS': 'is', 'EASY': 'easy'}

d = {10: "ten", "hai": "value", (1, 2, 3): "colln", 1.2: "decimal"}

result = {}
for key, value in d.items():
    # Individual/primitive types are generally scalar types like int, float, str, bool
    if isinstance(key, (int, float, str, bool)):
        result[key] = value
    else:
        result[key] = type(key)

print(result)
# Output: {10: 'ten', 'hai': 'value', (1, 2, 3): <class 'tuple'>, 1.2: 'decimal'}

names = ["manu", "lohit", "jivago", "wank", "yaseen"]
first_chars = [name[0] for name in names if name]
print(first_chars)
# Output: ['m', 'l', 'j', 'w', 'y']

names1 = ["laptop", "mouse", "board", "house", "week"]
pairs = [(name, len(name)) for name in names1]
print(pairs)
# Output: [('laptop', 6), ('mouse', 5), ('board', 5), ('house', 5), ('week', 4)]

l1 = [2, 3, 4, 5, 6]
l2 = [3, 4, 5, 8, 9]

sums = [x + y for x, y in zip(l1, l2)]
print(sums)
# Output: [5, 7, 9, 13, 15]
names = ["a", "b", "c", "d"]
age = [20, 35, 21, 56]

# Using zip to pair them into a dictionary
pairs_dict = dict(zip(names, age))
print(pairs_dict)
# Output: {'a': 20, 'b': 35, 'c': 21, 'd': 56}
'''




#1-->WAP TO FIND SQUARE OF ALL THE VALUES PRESENT BETWEEN THE RANGE(1 TO 5).



#2-->WAP TO FIND LENGTH OF EACH AND EVERY WORD PRESENT INSIDE THE GIVEN STRING.

#3-->WAP TO GET THE FOLLOWING O/P:
I/P='GOOD MORNING'
O/P={'GOOD':4,'MORNING':7}

#4-->WAP TO FIND FACTORIAL OF ALL THE NUMBERS PRESENT INSIDE THE GIVEN HOMOGENOUS LIST COLLECTION.

#5-->WAP TO GET THE FOLLOWING O/P
I/P='PYTHON IS EASY'
O/P={'PYTHON':'python', 'IS':'is', 'EASY':'easy'}

#6-->wap to return if the key is individual returns its value else return its type
d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

#7-->wap to create a list of 1st characters from each name
names=["manu","lohit","jivago","wank","yaseen"]


#8-->wap to return list of name and length pair
names1=["laptop","mouse","board","house","week"]


#9-->wap to print sum of indices from both list
l1=[2,3,4,5,6]
l2=[3,4,5,8,9]



#10-->wap to make a pair of names and age
names=["a","b","c","d"]
age=[20,35,21,56]
