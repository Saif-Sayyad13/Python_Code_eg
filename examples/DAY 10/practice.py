'''# wap to print a-z charcter
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



#1. WAP to extract only file names
l= ['forloop.txt', 'http://python.py', 'while.pdf', 'functions.pptx',
    'lambda.png', 'http://map.py', 'python.pdf', 'http://oops.py']
#output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops'] 
Aug 10 - 10:21 am
    """