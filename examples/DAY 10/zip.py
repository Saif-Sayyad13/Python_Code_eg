'''
zip()------inbuild function
it match position to position
Syntax
zip(iterable1, iterable2,.....)
if we want to a cant use 2 type means type casthing we only get output in the 
form of object address to abovide that we use typecasting and looping
the
dont use for string it will show object error
for i in zip(iterable1,iterable2.....):
    staterment 


Note directely if we use it will show object address
 
 syntax:-
zip_longest()
step 1 --- from itertools import zip_longest
(zip_longest(iterable1,iterable2.....,fillvalue=))
here we use fillvalue= to not show none in the place on non we can replace anything 




'''
'''a=[1,2,3,4]
b=[10,20,30,40]
print(zip(a,b))
print(list(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(dict(zip(a,b)))'''
'''
a=[1,2,3,4]
b=[10,20,30,40]
for i in zip(a,b):
    print(i)
    
x=[11,22,33]
y="Hi"
for i in zip(x,y):
    print(i)
    
aa=(10,20,30,40,50)
bb="sql"
cc=[1,2]
for i in zip(aa,bb,cc):
    print(i)'''
  
  
"""  
for using zip_longest we must have to import it
from itertools import zip_longest   
"""

'''from itertools import zip_longest  
a=[1,2,3]
b=[5,6,7]
for i in zip_longest(a,b):
    print(i)
print(list(zip_longest(a,b)))'''

''' hereif we dont fillvalue it will show non to avoid that we use fillvalue
from itertools import zip_longest  
s=[1,2,3,4,5]
h=[11,22]
print(list(zip_longest(s,h,fillvalue=10)))

print(list(zip_longest(s,h)))

for i in zip_longest(s,h,fillvalue='a'):
    print(i)'''
    
'''a=[10,20,30,40]
b=(1,2,3)
c='hehe'
#print(list(zip(a,b,c)))
for i in zip(a,b,c):
    print(i)'''
    
'''
a=[1,2,3,4]
b=[11,12,13,14]
print(zip(a,b))
print(list(zip(a,b)))
print(tuple(zip(a,b)))
print(set(zip(a,b)))
print(dict(zip(a,b)))
print(str(zip(a,b)))
'''
'''
a=[1,2,3,4]
b=[11,12,13,14]
for i in zip(a,b):
    print(i)
'''

'''
x=[11,12,13]
y="H"
for i in zip(x,y):
    print(i)
print()

print(list(zip(x,y)))
'''
'''
a=(1,2,3,4,5)
b="sql"
c=[1,2]
for i in zip(a,b,c):
    print(i)
'''

a=[1,2,3]
b=[5,6,7]

from itertools import zip_longest
'''
print(list(zip_longest(a,b)))
for i in zip_longest(a,b):
    print(i)
'''
'''
s=[1,2,3,4]
h=[11,12]
# print(list(zip_longest(s,h,fillvalue=10)))
for i in zip_longest(s,h,fillvalue=("Data",10)):
    print(i)
'''

'''
x=[1]
y=(1,2)
z="a"
z1={3,4,5,6}

for i in zip_longest(x,y,z,z1,fillvalue=0):
    print(i)
'''







"""
zip()

syntax :---> zip(iterble1,iterable2........)

Looping synatx:-->
for i in zip(iterble1,iterable2........):
    statement

Note:-->Directly if we use it will show object address

zip_longest()
step1--->from itertools import zip_longest

syntax :---> zip_longest(iter1,iter2........,fillvalue=value)

Looping syntax :-->
for variable in zip_longest(iter1,iter2........,fillvalue=value):
    statement

Note:-->Directly if we use it will show object address

"""











d=[10,5,89,100,34,1,0.6,99]
print(sorted(d,reverse=True))

for i in sorted(d):
    print(i,end=" ")

print()

'''
h="python"
print(sorted(h,reverse=True))
print(ord("h"))
print(ord("n"))
print(ord("o"))
print(ord("p"))
print(ord("t"))
print(ord("y"))
'''

'''

f=["Hello","pen","xyz","java","sql","a"]
for i in sorted(f):
    print(i)
print()

for i in sorted(f,key=len):
    print(i)
print()

for i in sorted(f,reverse=True):
    print(i)
'''








'''
#1.wap to print a-z character
for i in range(97,123):
    print(chr(i),chr(i-32),end=" ")

print()
#2.wap to print A-Z character
for i in range(65,91):
    print(chr(i),end=" ")
'''
'''
#2WAP to get the given o/p
s = 'hi hello good morning'
#exp o/p: 'gninrom doog olleh ih'

for i in reversed(s):
    print(i,end="")
print()

res=" "
for i in s.split():
    res=i[::-1]+" "+res
print(res)
'''

'''
# wap to create a dictionary with letter and
# its words starting with that letter pair

s="hi hello good morning welcome to python session"
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}
d={}
for i in s.split():
    print(i[0],"------->",i)
    if i[0] not in d:   #----->True
        d[i[0]]=[i]
    else:
        d[i[0]] += [i]
print(d)
''' 