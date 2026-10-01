'''
# 1. Greeting Function
# Write a function that takes a name and prints:
# Hello Amit

def Greet(name):
    print("Hello",name)
Greet("Amit")

#      OR

def Greet(name):
    return name
print(Greet("Amit"))
#    OR
w=Greet("Amit")
print(w)
'''

'''
# 2. Add Two Numbers
# Write a function that takes two numbers and returns their sum.
# Input: 10, 20
# Output: 30
def ADD(a,b):
    return a+b
e=ADD(10,20)
print(e)


def ADD(a,b):
    print(a+b)
ADD(10,20)



def ADD():
    a=int(input("enter the Number"))
    b=int(input("enter the Number"))
    print(a+b)
ADD()

def ADD(a,b):
    print(a+b)
ADD(a=int(input("ent")),b=int(input("ent")))
'''
'''
# 3. Find Difference
# Write a function that accepts two
# numbers and returns their difference.
def ADD(a,b):
    return a-b
e=ADD(10,20)
print(e)
'''
'''
# 4. Find Maximum
# Write a function that accepts two numbers and returns the greater number.

def Maximum_num(a,b):
    if a>b:
        print(f'The given number {a} is greater')
    else:
        print(f'The given number {b} is greater')
Maximum_num(10,20)

def Maximum_num(a,b):
    if a>b:
        return True,a
    else:
        return True,b
print(Maximum_num(10,20))
print(Maximum_num(100,20))
'''



# 5. Find Minimum
# Write a function that accepts two
# numbers and returns the smaller number.

# 6. Check Even or Odd
# Write a function that accepts a number
# and returns "Even" or "Odd".

'''
# 7. Check Positive, Negative or Zero
# Write a function that accepts a number and returns:
# Positive
# Negative
# Zero

def Check(num):
    if num>0:
        return "+Ve"
    elif num<0:
        return "-ve"
    else:
        return "Zero"
k=Check(0)
print(k)


def Check(num):
    if num>0:
        return "+Ve"
    elif num==0:
        return "Zero"
    else:
        return "-ve"
k=Check(0)
print(k)
'''


'''
# 8. Square a Number
# Write a function that accepts a number
# and returns its square.
# Input: 5
# Output: 25

def Square(num):
    return num**2
print(Square(5))

def Square(num):
    print(num**2) 5x5
Square(10)
'''




'''
# 9. Cube a Number
# Write a function that accepts a number
# and returns its cube.

def Cube(num):
    return num**3   #5x5x5
print(Cube(5))

'''
'''
# 10. Find Last Digit
# Write a function that accepts a number and returns its last digit.
Input: 12345
# Output: 5
def Last_data(Input):
    return Input%10
print(Last_data(12345))
'''

'''
# 11. Find First Digit
# Write a function that accepts an integer and returns its first digit.
# Input: 45678
# Output: 4

def First_Num(num):
    return num//10000
print(First_Num(45678))
'''
'''
# 12. Calculate Area of Rectangle
# Write a function that accepts length and 
# breadth and returns the area.
# Area = length × breadth
def Area():
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    print(l*b)
Area()
def Area():
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    return l*b
print(Area())
'''

'''
# 13. Calculate Simple Interest
# Write a function that accepts:
# principal
# rate
# time
# and returns simple interest.
# SI = (P × R × T) / 100
def SimpleInterest(P,R,T):
    return P*R*T/100
print(SimpleInterest(1000,2,3))
'''





'''
# 14. Find Average of Three Numbers
# Write a function that accepts three numbers
# and returns their average.

def Average_data(a,b,c):
    return (a+b+c)/3   #(a+b+c)/3
print(Average_data(10,20,30))
'''
'''
# 15.Count Vowels
# Write a function that accepts a string
# and returns the number of vowels.
Input: "education"
# Output: 5

def Total_vowels(Input):
    count=0  #local variable
    for i in Input:
        if i in "AEIOUaeiou":
            count=count+1
    print(count)
Total_vowels("education")
 #         OR
print()
count=0   #Global variable
def Total_vowels(Input):
    global count
    for i in Input:
        if i in "AEIOUaeiou":
            count=count+1
    print(count)
Total_vowels("education")
'''
'''
# 16.Count Consonants
# Write a function that accepts a
# string and returns the number of consonants.
Input: "education"
def Consonants(Input):
    count=0
    for i in Input:
        if i not in "AEIOUaeiou":
            print(i)
            count+=1
    print(count)
Consonants("education")
'''



'''
# 17. Count Digits in a String
# Write a function that accepts a string
# and counts how many digits are present.
Input: "abc123xy5"
# Output: 4
def Digit(Input):
    count=0
    for i in Input:
        if i.isdigit():
            count=count+1
    print(count)
Digit("abc123xy5")

print()



Input: "abc123xy5"
# Output: 4
def Digit(Input):
    count=0
    for i in Input:
        if i.isdigit():  #'1'----->int('1')---->1
            count=count+int(i)
    print(count)
Digit("abc123xy5")

'''
'''
# 18.Reverse a String
# Write a function that accepts a string and returns the reversed string.
Input: "python"
# Output: "nohtyp"
def Reverse(Input):
    return Input[::-1]
print(Reverse("python"))

print()

def Reverse(Input):
    print(Input[::-1])
Reverse("python")

print()

def Reverse(Input):
    for i in reversed(Input):
        print(i,end="")
Reverse("Python")

print()


def Reverse(Input):
    for i in range(-1,-len(Input)-1,-1):
        print(Input[i],end="")

Reverse("Python")

print()

def Reverse(Input):
    res=''
    for i in Input:
        res=i+res
    print(res)
Reverse("Python")
'''
'''
# 19.Return Only Positive Numbers
# Write a function that accepts a list
# and returns a new list containing only
# positive numbers.
a = [10, -5, 20, -2, 30]
def Positive_number(a):
    b=[]
    for i in a:
        if i>0:
            b.append(i)
    print(b)
Positive_number([10, -5, 20, -2, 30])
#output----->>>[10, 20, 30]
'''
'''
# 20.wap to perform addition and subtraction
# if "a" is greater than "b" return sum else
# return difference
def Operations(a,b):
    if a>b:
        return a+b
    else:
        return a-b
print(Operations(10,5)) #15
print(Operations(100,500))#-400
'''
'''
# 21.waf to check string is palindrome or
# not (take user input)
def Palindrome(a):
    if a==a[::-1]:
        return True,a
    else:
        return False,a
print(Palindrome("MoM"))
print(Palindrome("java"))

print()


def Palindrome():
    a=eval(input("enter the string"))
    if a==a[::-1]:
        return True,a
    else:
        return False,a
print(Palindrome())
print(Palindrome())
'''

'''
# 22.wap to return length of variable
# keywords arguments

def length_Data(**kwargs):
    return len(kwargs)
k=length_Data(a=10,b=90,c="Hello",e={1:2,3:4})
print(k)
print()
def length_Data(**kwargs):
    print(len(kwargs))
length_Data(a=10,b=90,c="Hello",e={1:2,3:4})

print()
def length_Data(**kwargs):
    length=0  #local variable
    for i in kwargs:
        print(i)
        length+=1
    print(length)
length_Data(a=10,b=90,c=100,d="hello",e=[1,2,3,4])
print()
length = 0  # Global variable
def length_Data(**kwargs):
    global length
    for i in kwargs:#{a:10,b:90,c:100.....}
        print(i)
        length+=1
    print(length)
length_Data(a=10,b=90,c=100,d="hello",e=[1,2,3,4])

'''
# 23.wap to return length of the
# variable positional arguments


'''
# 24.waf to search for character in
# a given string and return corresponding index
string="coding part is done"
def check(string,sub):
    return string.index(sub)
e=check("coding part is done","ing")
print(e)
'''
'''
def Data(string):
    sub=eval(input("enter the substring"))
    for i in range(len(string)):
        if string[i]==sub:
            return sub,i
    return "substring not found"
a=Data("coding part is done")
print(a)
'''

# 25.wap to squaring of the element
# in the given list
# l=[1,2,3,4,5]



# 27.wap to read 3 numbers from the
# user,first two numbers should be added
# and the result of addition should be
# subtracted by third number

'''
# 28.wap to find square,cube,square root
# and cube root of a number

def Data(num):
    return num**2,num**3,num**(1/2),num**(1/3)
print(Data(27))

print()
import math
def Data(num):
    return num**2,num**3,math.sqrt(num),math.cbrt(num)
print(Data(27))

'''



# 29.wap to check the given characters is
# alphabets or digit or special characters


# 30.wap to check given iterable is a sequence,
# if it is a sequence reverse it,if 
# not add one extra element to the iterable


# 31.write a function to print the below output
# func("TRACXN",1)
#should print RCN

#
# 32.write a function to print the below output
# func("TRACXN",0)
#should print TAX


# 33.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.




# 34.waf to return a dictionary with characters and ascii value pair


# 35.waf to reverse a iterable if you are passing string or list or tuple else print type of the data

# 36.wap to check if a given character is alphabet or digit or special character (without using inbuilt function).
#


# 37.wap to return length of an iterable without using len() function

# 38.wap to count the number of arguments passed inside the function call(both positional and keyword)

