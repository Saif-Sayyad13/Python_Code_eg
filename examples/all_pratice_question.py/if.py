''' IF CONDITION PROGRAMS
1.wap to check the number is odd (take user input)
2.wap to check the number is even (take user input)
3.wap to check if the student has scored 70% print "good luck "(take user input)
4.wap to check which number is greater using if condition
a=98
b=67
5.wap to check if the given string has even length of character
s="hey guys you all are Osam"
6.wap to check if the given number is divisible by 5 (take user input)
7.wap to check if the given programming is present in the list
p=["java","python","c","c++","RUBy","golang"]
8.wap to check eligible to vote take user input as a age
9.wap to check if the given number is positive take user input
10.wap to check if the given string is palindrome (take user input)
11.wap to check if the first letter in the given string is consonant
s="Lahari is a good student"
12.wap to check the given string is uppercase or not (take user input)
13.wap to check the given value is string (take user input)
14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
15.wap to check whether given number is negative and print "its negative guys"
16.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
17.wap to check whether the given number is even or not,if even store the value inside the list (take user input)
19.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
20.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take user input)
21.wap to checking if a string contains a substring
string="hello world"
sub_string="world"
22.wap to check whether a character is in the alphabet or not,if it is alphabet,store the value inside  a dict(key as a character and value as a ascii value)
     23.wap to check whether a character is in uppercase or not,if uppercase,convert to lowercase and store the value inside the dictionary (character as key and ascii as value) take user input
'''
'''#1.wap to check the number is odd (take user input)
a=eval(input("Enter a number"))
if a%2==0:
     print("number is even",a)
#2.wap to check the number is even (take user input)
b=eval(input('enter a number'))
if b%2==0:
     print("number is odd",b)
     
#3.wap to check if the student has scored 70% print "good luck "(take user input)
c=eval(input('Enter your score'))
if c>70:
     print("Good luck")     
#4.wap to check which number is greater using if condition
a=98
b=67
if a>b:
     print("a bada hai")
#5.wap to check if the given string has even length of character
s="hey guys you all are Osam"
if len(s)%2==0:
     print("even length")'''
     

'''#6.wap to check if the given number is divisible by 5 (take user input)
a=eval(input('enter a number'))
if a%5==0:
     print('number is divisible by 5')'''
     
     
'''#7.wap to check if the given programming is present in the list
p=["java","python","c","c++","RUBy","golang"]
a=eval(input('Enter a progra launguage'))
if a in p :
     print("pressent hai")
     '''
     
'''#8.wap to check eligible to vote take user input as a age
a=eval(input('enter your age'))
if a>=18:
     print('good to vote')'''
     
'''#9.wap to check if the given number is positive take user input
a=eval(input('enter a no'))
if a>0:
     print('+ve')'''
     
'''#10.wap to check if the given string is palindrome (take user input)
a=eval(input('enter a string'))
if a==a[::-1]:
     print('palinfrome hai')'''

'''
#11.wap to check if the first letter in the given string is consonant
s="Lahari is a good student"
a='aeiouAEIOU'
if a not in s[0]:
    print("first chr consonant hai")'''
    
'''#12.wap to check the given string is uppercase or not (take user input)
a=eval(input('kuch to likho'))
if a== a.upper() :
     print('upper hai')'''
'''#13.wap to check the given value is string (take user input)
a=eval(input('enter kuch to'))
if isinstance(a,str):
     print('string hai')'''
     
'''#14.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
a=eval(input('enter a no'))
if a>1  and a<5:
     print('python coding')'''
'''#15.wap to check whether given number is negative and print "its negative guys"
a=eval(input('enter a no'))
if a<0:
     print("-ve hai")'''
'''#16.wap to check whether given input is divisible by 2 and 6 if condition is True
# ,convert the given number to complex number.(take user input)
a=eval(input('enter a no'))
if a%2==0 and a%6==0:
     aa=complex(a)
     print(aa)'''
'''#17.wap to check whether the given number is even or not,if even store the
# value inside the list (take user input)
a=eval(input('enter a no'))
aa=[]
if a%2==1:
     aa.append(a)
print(aa)'''

'''#19.wap to check whether a given value is divisible by 5 and 7,if
# the value is divisible then display the square of the values (take user input)
a=eval(input('enter a no'))
if a%7==0 and a%7==0:
     
     print(a**2)'''
'''#20.wap to check whether a given value is present in between 45 and 200 and the number 
# should be divisible by 4 and 5 ,if satisfied,display the ascii characters (take user input)
a=eval(input('enter a no'))
if 45 <= a <= 200 and a % 4 == 0 and a % 5 == 0:
    print(chr(a))'''
     
'''#21.wap to checking if a string contains a substring
string="hello world"
sub_string="world"
if sub_string in string:
     print("hai")'''
'''#22.wap to check whether a character is in the alphabet or not,if it is alphabet,
# store the value inside  a dict(key as a character and value as a ascii value)
d = {}
user = input("Enter a character: ")

if len(user) == 1 and user.isalpha():
    d[user] = ord(user)
    print("Updated dictionary:", d)
'''
'''
 #    23.wap to check whether a character is in uppercase or not,if uppercase,convert to lowercase
 # and store the value inside the dictionary (character as key and ascii as value) take user input
d={}
a=eval(input('enter kuch to:'))
if len(a) == 1 and a.isupper():
    lower_char = a.lower()
    d[lower_char] = ord(lower_char)
    print("Updated dictionary:", d)
 '''
 
 



class 