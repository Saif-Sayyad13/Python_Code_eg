"""'''# wap to print a-z charcter
for i in range(97,123):
    print(chr(i),end=" ")
    '''
'''# wap to print A-Z character
for i in range(65,91):
    print(chr(i),end=" ")'''
   
'''# wap to write to print a-z,A-Z, like aA,bB,cC.. 
for i in range(97,123):
    print(chr(i),chr(i-32),end=" ")'''
    
'''#wap tp get the given o/p s='hi hello good morning '
#exp o/p: 'gninrom',doog,olleh,ih
s='hi hello good morning'
print(s[::-1])
print()
for i in s[::-1]:
    print(i,end=" ")
print()
for i in reversed(s):
    print(i,end=" ")
print()

s='hi hello good morning'
res=" "
for i in s.split():
    res=i[::-1]+" "+res 
print(res)
'''

'''#wap tp create a dictionary with letter and its words starting with that letter pair
s='hi hello good morning welcome to python session'
#o/p--{'h':['hi','hello'],'g':['good'],'m':['morning']}
dict={}
for i in s.split():
#    print(i[0],"-----",i)
    if i[0] not in dict:
        dict[i[0]]=[i]
    else:
        dict[i[0]] +=[i]
print(dict)'''

'''#wap t0
s="hello python"
d={}
for i in range(len(s)):
#    print(i[0],i)
    if s[i] not in d:
        d[s[i]]=[i]
    else:
        d[s[i]] +=[i]
print(d) '''

"""
'''
    1.wap to create a dictionary word and reverse word pair
s="tomorrow is weekend and non-veg special"


o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}




2.wap to Sum of numbers
s = 'Sony12India567pvt21ltd'


3.Print all the missing numbers from 1-10 in the below list
l = [1, 2, 3, 4, 6, 7, 10]



4.WAP to remove duplicates from the list without using inbuilt function
d=[1,2,3,4,5,6,7,1,2,3,4]




5.wap to replace all the character with "-" if the characters occurs more than once in a string
s="hellohai"
o/p---->-e--o-ai




6.wap to print first and last char of each name in the list
a=["Sunil","anil","Suresh","Mahesh","Dinesh"]


7.wap to create a new list as square of each number of below list
b=[2,4,5,6,7,1]


8.wap if number is even the print its square else print its cube
c=[2,4,5,3,7,9]


9.wap to create a list with square and cube of each numbers
d=[2,4,5,1,8,9,10]
o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]


10.wap to create a new list of reversing each name from the list
names=["prince","Rekha","Madhu","Sindhu","denga","manga"]


11.wap to create a new list, of individual and collection data type from list
data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)] 
Aug 10 - 10:20 am
12.wap to create a dictionary characters and its count pair
char=["a","M","i","A","M","I","i","H","a","H"]


13.wap to group fruit name and country pair
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}


14.wap to sum of same index element from l1,l2,l3
l1=[10,20,30,40]
l2=[78,44,11,99]
l3=[1,2,3,4]


15.wap to pair values of both dictionary
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}

'''

#1. WAP to extract only file names
#l= ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
  #  'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']
#output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops'] 

""" 
#1. Word and reverse-word pair
s = "tomorrow is weekend and non-veg special"

d = {}

for i in s.split():
    d[i] = i[::-1]

print(d)

#2. Sum of numbers
s = 'Sony12India567pvt21ltd'

sum = 0

for i in s:
    if i.isdigit():
        sum += int(i)

print(sum)


s = 'Sony12India567pvt21ltd'

sum = 0
num = ""

for i in s:
    if i.isdigit():
        num += i
    else:
        if num:
            sum += int(num)
            num = ""

if num:
    sum += int(num)

print(sum)


#3. Missing numbers from 1–10
l = [1, 2, 3, 4, 6, 7, 10]

for i in range(1, 11):
    if i not in l:
        print(i)


#4. Remove duplicates without inbuilt function
d = [1,2,3,4,5,6,7,1,2,3,4]

res = []

for i in d:
    if i not in res:
        res.append(i)

print(res)


#5. Replace repeated characters with -
s = "hellohai"

res = ""

for i in s:
    if s.count(i) > 1:
        res += "-"
    else:
        res += i

print(res)


#6. First and last character of each name
a = ["Sunil", "anil", "Suresh", "Mahesh", "Dinesh"]

for i in a:
    print(i[0], i[-1])


#7. Square of each number
b = [2,4,5,6,7,1]

res = []

for i in b:
    res.append(i ** 2)

print(res)


#8. Even → square, Odd → cube
c = [2,4,5,3,7,9]

for i in c:
    if i % 2 == 0:
        print(i ** 2)
    else:
        print(i ** 3)


#9. Square and cube of each number
d = [2,4,5,1,8,9,10]

res = []

for i in d:
    res.append((i ** 2, i ** 3))

print(res)

#10. Reverse each name
names = ["prince","Rekha","Madhu","Sindhu","denga","manga"]

res = []

for i in names:
    res.append(i[::-1])

print(res)


#11. Individual and collection data types
data = [20.12, True, [10,20], "super", {1,2}, {"a":10}, 100, (8,9)]

individual = []
collection = []

for i in data:
    if isinstance(i, (list, tuple, set, dict)):
        collection.append(i)
    else:
        individual.append(i)

print("Individual:", individual)
print("Collection:", collection)


#12. Character and count pair
char = ["a","M","i","A","M","I","i","H","a","H"]

d = {}

for i in char:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)


#13. Group fruit name and country pair
d = {"apple":45, "mango":67, "cherry":90, "berry":23}

p = {"Kashmir":"India", "America":"us", "UK":"Toronto", "Africa":"Uganda"}

res = {}

for i in d:
    for j in p:
        res[i] = (d[i], p[j])
        break

print(res)



d = {"apple":45, "mango":67, "cherry":90, "berry":23}

p = {"Kashmir":"India", "America":"us", "UK":"Toronto", "Africa":"Uganda"}

res = {}

d_values = list(d.values())
p_values = list(p.values())

for i in range(len(d_values)):
    res[d_values[i]] = p_values[i]

print(res)


{45: 'India', 67: 'us', 90: 'Toronto', 23: 'Uganda'}
#14. Sum same-index elements
l1 = [10,20,30,40]
l2 = [78,44,11,99]
l3 = [1,2,3,4]

res = []

for i in range(len(l1)):
    res.append(l1[i] + l2[i] + l3[i])

print(res)


#15. Pair values of both dictionaries
d = {"apple":45, "mango":67, "cherry":90, "berry":23}

p = {"Kashmir":"india", "America":"us", "UK":"Toronto", "Africa":"Uganda"}

res = []

for i in d.values():
    for j in p.values():
        res.append((i, j))
        break
    p = dict(list(p.items())[1:])

print(res)


# another way to pair values of both dictionaries

d = {"apple":45, "mango":67, "cherry":90, "berry":23}

p = {"Kashmir":"india", "America":"us", "UK":"Toronto", "Africa":"Uganda"}

res = []

a = list(d.values())
b = list(p.values())

for i in range(len(a)):
    res.append((a[i], b[i]))

print(res)
#16. Extract only file names
l = [
    'forloop.txt',
    'http://python.py',
    'while.pdf',
    'functions.pptx',
    'lambda.png',
    'http://map.py',
    'python.pdf',
    'http://oops.py'
]

res = []

for i in l:
    if "http://" in i:
        i = i.split("/")[-1]

    i = i.split(".")[0]
    res.append(i)

print(res)




l = [
    'forloop.txt',
    'http://python.py',
    'while.pdf',
    'functions.pptx',
    'lambda.png',
    'http://map.py',
    'python.pdf',
    'http://oops.py'
]

res = []

for i in l:
    if "http://" in i:
        i = i.split("/")[-1]

    i = i.split(".")[0]

    if i not in res:
        res.append(i)

print(res)
'''"""