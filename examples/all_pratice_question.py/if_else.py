'''  IF-ELSE PROGRAMS
1.wap to check the given number is even or odd (take user input)
2.wap to check whether the male and female are eligible for wedding (take user input)
3.wap to return uppercase if the char is lower,else return same char (by taking user input)
4.wap to return lower case if the upper ,else return same char (by taking user input)
5.wap to find greater value among the two number
n1=34
n2=54
6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)
7.wap to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalize it
s="python"
8.wap to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)
9.wap to check number should be divisible by 3 and 7 (take user input)
10.wap if the length of string is even then reverse else convert into upper case (take user input)
11.wap to check a number is +ve/-ve number (take user input)
12.wap to check a data is individual or collection data type or not (take user input)
13.wap to check whether the specified character is present in the given string
s="Python"
14.wap to check the length of dictionary and length of dictionary is even or Not if even
print as it is or else add a item and make it even
D={"a":"apple","b":"ball","c":"cat"}
15.wap to check the given number is greater than 5,if it is greater convert that number into negative number
else print the same number
16.wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it
else print the number as it is
17.wap to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)
18.wap to check if the given character is alphabet or Not ,if it is alphabet, create a replica of it 2 times. (take user input)
'''

'''

#54
a= "pass123"
while True:
    user = input("Enter your password: ")
    if user == a:
        print("Ho giya ")
        break
    print("Wrong password try again")
    
    
a = "pass123"

while input("Enter your password: ") != a:
    print("Wrong password try again")

print("Ho giya")

#55
a = (10, 22, 33, 44, 55, 60, 77, 88)
l = []
for i in range(1, len(a), 2):
    if a[i] % 2 == 0:
        l.append(a[i])
pprint("List after removing duplicates:", l2)

hello_guys="don don don"
if hello_guys=="don don dn":
    print('accha hai')
else:
    print("kon hai ye")rint("Even integers at odd indices:", l)

#56
l1 = [1, 2, 2, 3, 4, 4, 5]
l2 = []
for item in l1:
    if item not in l2:
        l2.append(item)
'''
'''
# wap to display the message as per signal red-stop,green -go,yello-stay
a=eval(input('enter a signal red,yelloor green in:'))
if a=="red":
     print("its red stop")
elif a=="yellow":
     print('its yello stay')
elif a=="green":
     print('its green go')
else:
     print('invaild signal')'''
     
'''
#wap to creat a simple calculator to perform basic operation lik +,-,*,/
a=eval(input('enter a number'))
b=eval(input('enter a another  number'))
print("please select the operation you want to do ")
add=print("1.ADD")
sub=print("2.SUB")
multi=print("3.MULTI")
div=print("4.DIV")

c=eval(input(" 1,2,3,4"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print('invalid selection')'''

'''# wap to findlaargest of 3 per specific number using ternitery operation
a=1
b=2
c=3
if a>b and a>c:
    print('a bada hai')
elif b>a and b>c:
    print('b bada hai')
else:
    print('c bada hai')'''
    
a=eval(input('enter a no'))
l=0
for i in a:
    if i>0:
        l=l+i
    else:
        i==0:print()
print(l)


'''
idia sore under 
signup FTC 100
sevirity high 


'''
