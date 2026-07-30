# whenevere we are using we can pass unlimited char
a="HELLO"
if a.isupper():
    print("uppercase data")
    
# or withoutusing induild function
# inord we only have to pass 1 char
x="H"
if ord('A')<=ord(x)<=ord("Z"):
    print('upper case data')
    
# or

b ="hello"
if b.islower():
    print("lowercase data ")
    
#or
bb="h"
if ord('a')<=ord(bb)<=ord('z'):
    print('lower csse data')
    
c='12345678'
if c.isdigit():
    print('is a digit')
    
#or
cc='7'
if ord('0')<=ord(cc)<=ord('9'):
    print('number is a digit')
    
#or
ccc='8'
if "0"<=ccc<="9":
    print('good')

# print() means next line 

#wap to check to given char is upper case then convert to lowe case
k='HELLO'
if k.isupper():
    k=k.lower()
print(k)

#wap to check to given char is lower case then convert to upper case
d="good morning"
if d.islower():
    d=d.upper()
print(d)

# convert upper to lowe case without using inbuild function
e="H"
if ord("A")<=ord(e)<=ord("Z"):
    print(chr(ord(e)+32))
    
k="a"
if ord('a')<=ord(k)<=ord('z'):
    print(chr(ord(k)-32))
# here we use 32 becuase the difference bewteen uppper case rro lower case A to a is 32
# A to a use +32 to convert upper case to lower
# a to A use -32 to convert lower to upper case
