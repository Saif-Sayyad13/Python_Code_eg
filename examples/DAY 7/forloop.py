'''a="aman"
for i in a:
    print(i,end=" "i)
    print()
    print(i)

for i in range(1,11):
    print(i,end=" ")
'''
'''
# 9.wap to perform list operations user should enter only list data type,if options 1 pop().options 2 sort() options 3 clear() invalid options,invalid data type
a=eval(input("enter a data"))
if a.isinstance(a,list):
    print("1.pop()")
    print("2.sort()")
    print("3.clear()")
    ch=int(input("enter your choice"))
    if ch==1:
        a.pop()
        print(a)
    elif ch==2:
        a.sort()
        print(a)
    elif ch==3:
        a.clear()
        print(a)
    else:
        print("invalid option")
else:
    print("invalid data type")
    
'''


# Collection Groups
'''
a="Morning"
for i in a:   #for i in "Morning":
    print(i,end=" ")
print()
b=[10,20,30,40]
for k in b:
    print(k,end=" ")

print()
c=(100,"Hii",89.45,True,4+5j)
for i in c:
    print(i,end=" ")
print()
d={1,2,3,4,5}
for i in d:
    print(i,end=" ")
print()
'''
'''
e={12:90,100:200,45:"abc"}

for i in e:
    print(i)   #i----->12  i----->100  i---->45
print()

for i in e:
    print(e[i])   #var_name[key]----->e[i]
'''
'''
e={12:90,100:200,45:"abc"}
for i in e:
    print(i)

i----->12 ----->key
i----->100----->key
i----->45------>key

How To print Value In dictionary
ans:--> By the help of keys
Here all keys will Pointing by --->i (variable)

synatx :----> var_name[key]
Here var_name means dicitionary---->e
Here startPoint_variable is ---->i

final syntax ----> var_name[key]----> e[i]

'''
'''
print()

for i in e:
    print(i,"----->",e[i])
'''

'''
#with useing Inbuilt Function How to print
#keys---> values----> both(key-->value)
e={12:90,100:200,45:"abc"}
for i in e.keys():
    print(i)
print()
for i in e.values():
    print(i)
print()
for i in e.items():
    print(i)
"""
keys()------> var_name.keys()
values()----> var_name.values()
items()-----> var_name.items()
'''






"""
d=[1,2,3,4,5,6,7,8,9,10]
for i in d:
    if i%2==0:
        print(i)

d=[1,2,3,4,5,6,7,8,9,10]
for i in d:
    if i%2==0:
        print(i)

step--->1
for 1 in [1,2,3,4,5,6,7,8,9,10]:-->True
    if 1%2==0:---->False
        Blank_space

step--->2
for 2 in [1,2,3,4,5,6,7,8,9,10]:-->True
    if 2%2==0:---->True
        print(i)----->2

step--->3
for 3 in [1,2,3,4,5,6,7,8,9,10]:-->True
    if 3%2==0:---->False
        Blank_space
step--->4
for 4 in [1,2,3,4,5,6,7,8,9,10]:-->True
    if 4%2==0:---->True
        print(i)----->4

"""

'''
s=["abc","xyz","python","java","sql"]
for i in s:
    print(i.upper())    #var_name.upper()

print()
for i in s:
    print(i,"--->",i[0],"---",i[-1])   #i------>"abc"----->i[0]-->a i[-1]-->c

print()
for i in s:
    if len(i)%2==0:
        print(i)
"""
i--->"abc"
len(i)--->3

for "abc" in s:   True
    if len(abc)%2==0: False
        print(i)  #Blankspace

for "xyz" in s:  True
    if len("xyz")%2==0:  False
        print(i)  #Blankspace

for "python" in s:  True
    if len("python")%2==0: True
        print(i)----->o/p-->python

for "java" in s: True
    if len("java")%2==0: True
        print(i)----->o/p--->Java

for "sql" in s: True
    if len("sql")%2==0: False
        print(i)---->Blankspace
"""
'''

s="PYTHON123"
for i in s:
    if i.isdigit():
        print(i)
"""
i---->"P"---->True
"P".isdigit()--->False

i--->"Y"---->True
"Y".isdigit()--->False

i-->"T"---->True
"T".isdigit()---->False

i--->"H"--->True
"H".isdigit()--->False

i-->"O"--->True
"O".isdigit()--->False

i-->"N"--->True
"N".isdigit()--->False

i--->"1"--->True
"1".isdigit()--->True
output--->'1'

i--->"2"---->True
"2".isdigit()--->True
output--->'2'

i--->"3"--->True
"3".isdigit()---->True
output--->'3'


"""


s="Good Luck"
for i in s:
    if i in "aeiouAEIOU":
        print(i)

print()

s="Good Luck"
for i in s:
    if i not in "aeiouAEIOU":
        print(i)


