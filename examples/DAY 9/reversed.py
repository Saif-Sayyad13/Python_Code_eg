"""'''
.reversed()
inbuild function 
object address --- 1 way typecasting   2 way looping
in reversed if we done operation directely it will show object address
In reversed to avoid object address data we have two ways 
!. Type casting 
2. Looping

Typecasting syntax:
list(reversed(iterable))
tuple(reversed(iterable))
dict(reversed(iterable))
set(reversed(iterable))


Looping syntax

for variable in reversed(iterable):
    statement 

'''
s="Python"
print(reversed)
print()
print(list(reversed(s)))
#['n', 'o', 'h', 't', 'y', 'P']
print()
print(tuple(reversed(s)))
#('n', 'o', 'h', 't', 'y', 'P')
print()
'''print(dict(reversed(s))) because dict want two data key as well as value
'''
print(set(reversed(s)))
#'h', 't', 'P', 'y', 'o', 'n'}
print()

"""
'''
s="Python"
for i in reversed(s):  # reversed inbuild functin
    print(i,end=" ")
print()

for i in s[::-1]:   # slicing
    print(i,end=" ")
print()

for i in range(-1,-len(s)-1,-1): # range()
    print(s[i],end=" ")
print()

res=" "  
for i in s:  # without using inbuild function
    res=i+res
print(res)
'''
'''d=[1,2,3,4,5]
l=[]
for i in d:
    l=[i]+l
print(l)
    '''
   
'''
#wap to check how many wordss are present in given sentance
a="hello world sentence"
b=a.split()
print(b)
total=0
for i in b:
    total=total+1
print(total)
    
#26.wap to check how many words are present
# in the given sentence
a="hello world sentence"
b=a.split()
print(b) #['hello', 'world', 'sentence']
total=0
for i in b:
    total=total+1
print(total)
'''






'''
# 27.wap to create a dictionary and print the characters
# and its Ascii value pair
s="hello world"
# output:--> {"h":ascii value,"e":ascii value........}
d={}
for i in s:
    d.update({i:ord(i)})
print(d)

d={}
for i in s:
    d[i]=ord(i)
print(d)
'''
'''
# 28.wap to create a dictionary and
# traverse into it and if the length is
# even print as it else reverse it
names=["apple","google","yahoo","microsoft","gmail","walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
d={}
for i in names:
    if len(i)%2==0:
        d[i]=i
    else:
        d[i]=i[::-1]
print(d)

# 29.wap to print series of factorial(take user input)
num=eval(input("enter the Number"))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
    print(i)
print(fact)

fact=1
i=1
fact=fact*i----> fact=1*1----=1
i=2
fact=fact*i----> fact=1*2----=2

i=3
fact=fact*i----->fact=2*3----=6

i=4
fact=fact*i---> fact=6*4----=24

i=5
fact=fact*i---> fact=24*5---=120





'''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
