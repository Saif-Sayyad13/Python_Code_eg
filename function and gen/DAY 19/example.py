"""1. Greeting Function
Write a function that takes a name and prints:
Hello Amit


2. Add Two Numbers
Write a function that takes two numbers and returns their sum.
Input: 10, 20
Output: 30


3. Find Difference
Write a function that accepts two numbers and returns their difference.

4. Find Maximum
Write a function that accepts two numbers and returns the greater number.

5. Find Minimum
Write a function that accepts two numbers and returns the smaller number.

6. Check Even or Odd
Write a function that accepts a number and returns "Even" or "Odd".

7. Check Positive, Negative or Zero
Write a function that accepts a number and returns:
Positive
Negative
Zero

8. Square a Number
Write a function that accepts a number and returns its square.
Input: 5
Output: 25

9. Cube a Number
Write a function that accepts a number and returns its cube.

10. Find Last Digit
Write a function that accepts a number and returns its last digit.
Input: 12345
Output: 5

11. Find First Digit
Write a function that accepts an integer and returns its first digit.
Input: 45678
Output: 4

12. Calculate Area of Rectangle
Write a function that accepts length and breadth and returns the area.
Area = length × breadth

13. Calculate Simple Interest
Write a function that accepts:
principal
rate
time
and returns simple interest.
SI = (P × R × T) / 100


14. Find Average of Three Numbers
Write a function that accepts three numbers and returns their average.


15.Count Vowels
Write a function that accepts a string and returns the number of vowels.
Input: "education"
Output: 5


16.Count Consonants
Write a function that accepts a string and returns the number of consonants.

17. Count Digits in a String
Write a function that accepts a string and counts how many digits are present.
Input: "abc123xy5"
Output: 4


18.. Reverse a String
Write a function that accepts a string and returns the reversed string.
Input: "python"
Output: "nohtyp"

19.Return Only Positive Numbers
Write a function that accepts a list and returns a new list containing 
only positive numbers.
a = [10, -5, 20, -2, 30]




20.wap to perform addition and subtraction if "a" is greater than 
"b" return sum else return difference



21.waf to check string is palindrome or not (take user input)


22.wap to return length of variable keywords arguments


23.wap to return length of the variable positional arguments


24.waf to search for character in a given string and return corresponding index
  string="coding part is done"


25.wap to squaring of the element in the given list
l=[1,2,3,4,5]

26.wap to fetch last digit number


27.wap to read 3 numbers from the user,first two numbers should be added 
and the result of addition should be subtracted by third number


28.wap to find square,cube,square root and cube root of a number


29.wap to check the given characters is alphabets or digit or special characters


30.wap to check given iterable is a sequence,if it is a sequence reverse it,
if not add one extra element to the iterable


31.write a function to print the below output
func("TRACXN",1)
#should print RCN


32.write a function to print the below output
func("TRACXN",0)
#should print TAX


33.A function take variable number of positional arguments as input. 
how to check if the arguments are more than 5.




34.waf to return a dictionary with characters and ascii value pair


35.waf to reverse a iterable if you are passing string or list or tuple else 
print type of the data

36.wap to check if a given character is alphabet or digit or special character
(without using inbuilt function).

37.wap to return length of an iterable without using len() function

38.wap to count the number of arguments passed inside the function call
(both positional and keyword)

"""

'''#1. Greeting Function Write a function that takes a name and prints:
def greet(name):
    print("hello",name)
greet("amit")

def greet(name):
    return "hello",name
    
greet(greet("amit"))
or
w=gree

def demo():
    print('Hello Amit')
demo()'''

 
'''#2. Add Two Numbers Write a function that takes two numbers and returns their sum.

def don(a,b):
    print(a+b)
don(10,20)


'''
    
'''#12. Calculate Area of Rectangle Write a function that accepts length and breadth and returns the area.
#Area = length × breadth

def area():
    a=eval(input("enter the length"))
    b=eval(input("enter the breadth"))
    print(a*b)
area()

def area():
    a=eval(input("enter the length"))
    b=eval(input("enter the breadth"))
    return a*b
print(area())'''

'''#13. Calculate Simple Interest Write a function that accepts:
principal
rate
time
and returns simple interest.
SI = (P × R × T) / 100

def simple_interest(P,R,T):
    print (P*R*T/100)
simple_interest(10,20,30)'''

'''#14. Find Average of Three Numbers Write a function that accepts three numbers and returns their average.

def avg(a,b,c):
    return (a+b+c)/3
print(avg(10,20,30))'''

'''#15.Count Vowels Write a function that accepts a string and returns the number of vowels.
#Input: "education"
#Output: 5
def total_vowels(Input):
    count=0
    for i in Input:
        if i in 'AEIOUaeiou':
            count=count+1
    print(count)
total_vowels("education")
    '''
    
'''#16.Count Consonants Write a function that accepts a string and returns the number of consonants.

def Consonants():
    count=0
    a=eval(input("enter a string"))
    for i in a:
        if i not in 'AEIOUaeiou':
            print(i,end=" ")
            count=count+1
    print(count)
    
Consonants()'''

'''#17. Count Digits in a String Write a function that accepts a string and counts how many digits are present.
Input: "abc123xy5"
#Output: 4

def Count_Digit(Input):
    count=0
    for i in Input:
        if i.isdigit():
            count=count+1
    print(count)
Count_Digit('abc123xy5')

def Count_Digit(Input):
    count=0
    for i in Input:
        if i.isdigit():
            count=count+int(i)
    print(count)
Count_Digit('abc123xy5')
'''

'''#18.. Reverse a String Write a function that accepts a string and returns the reversed string.
Input: "python"
#Output: "nohtyp"

def Reverse(Input):
    print(Input[::-1])
Reverse("python")'''


'''#19.Return Only Positive Numbers Write a function that accepts a list and returns a new list containing  
# only positive numbers.
a = [10, -5, 20, -2, 30]

def Positive(a):
    l=[]
    for i in a:
        if i >0:
            l.append(i)
    print(l)
Positive([10, -5, 20, -2, 30])

'''

'''#20.wap to perform addition and subtraction if "a" is greater than 
# "b" return sum else return difference

def Don():
    a=eval(input("enter a number"))
    b=eval(input("enter a another  number"))
    if a>b:
        print(a+b)
    else:
        print(a-b)
Don()
'''


'''#21.waf to check string is palindrome or not (take user input)

def kon():
    a=eval(input("kuch to likho"))
    if a==a[::-1]:
        print("palindrome hai")
    else:
        print("not a palindrome")
kon()
'''

'''#22.wap to return length of variable keywords arguments
def lenght_data(**kwarges):
    return len(kwarges)
k=lenght_data(a=10,b=20,c="hello",d={1:2,3:4})
print(k)'''
    




#23.wap to return length of the variable positional arguments


#24.waf to search for character in a given string and return corresponding index


#25.wap to squaring of the element in the given list 


#26.wap to fetch last digit number


'''#28.wap to find square,cube,square root and cube root of a number

import math as M
print(M.sqrt(4))
print(M.cbrt(27))
'''