
"""
reverse
'''a=[1,2,3,3,4,5,3,23,23,412,43,5,4,5]
a.reverse()
print(a)
print(a[::-1])
'''

for i in reversed(a):
    print(i,end=" ")"""

"""
remove duplicate
a=[1,2,3,1,2,3,4,5]
'''s=set(a)
print(s)   '''

s=[]
for i in a:
    if i not in s:
        s.append(i)
print(s)"""
'''
palindrome
a=eval(input('enter a data'))
if a==a[::-1]:
    print(f'{a} is a pal hai')
else:
    print(f'{a} is not a pal')'''
    



'''
# count volwels
a=eval(input('enter a number '))
s=0
for i in a:
    if i in "aeiouAEIOU":
        s=s+1
print(s)'''


"""
# find largest /smallest no
a=[1,2,3,4,4,5,6,7,9]
print(min(a))
print(max(a))
"""


'''a=[9,42,21,335,44,23,2]
a.sort()
print(a[5])

s=eval(input('enter a number'))
s.sort()
print(s[len(s)-2])
    
'''
'''# fibonacci
# Get user input
u = int(input("Enter how many numbers you want: "))

# Simple loop to generate the sequence
a, b = 0, 1
sequence = []

for _ in range(u):
    sequence.append(a)
    a, b = b, a + b  # Update the numbers simply

print("Fibonacci sequence:", sequence)
'''

'''# anagram
# Get user inputs
u1 = input("Enter first word: ")
u2 = input("Enter second word: ")

# Sort both words alphabetically
if sorted(u1.lower()) == sorted(u2.lower()):
    print("Yes, they are anagrams!")
else:
    print("No, they are not anagrams.")
'''

'''
#factorial
def calculate_factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# User Input Execution
try:
    u = int(input("Enter a non-negative integer to find its factorial: "))
    print(f"Factorial ({u}!): {calculate_factorial(u)}")
except ValueError:
    print("Please enter a valid integer calculation value.")
'''

'''import math

# Get user input
u = int(input("Enter a number: "))

# Use math.factorial for an instant answer
result = math.factorial(u)

print(f"The factorial of {u} is:", result)
'''

'''def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))  # Output: 120
'''

'''
# fibonacci
u=eval(input('enter a number'))
a,b=0,1
l=[]
for i in range(u):
    l.append(a)
    a,b=b,a+b
print(l)'''


'''#anagram
u1=input('enter a word')    
u2=input('enter a word')
if sorted(u1)==sorted(u2):
    print('yes they are anagrams')
else:
    print('no they are not anagrams')'''
    
    
'''#factorial
a=eval(input('enter a number'))
s=1
for i in range(1,a+1):
    s=s*i
print(s)'''

'''
list of prime numbers
u = int(input('enter a number: '))
l = []

for num in range(2, u + 1):
    # If num is not divisible by any number before it, it's prime
    if all(num % i != 0 for i in range(2, num)):
        l.append(num)

print(l)
'''

'''a = int(input('enter a number: '))

# A prime number must be greater than 1
if a <= 1:
    print("not prime")
else:
    # Check if any number from 2 up to (a-1) divides it perfectly
    if any(a % i == 0 for i in range(2, a)):
        print("not prime")
    else:
        print("prime")'''


'''
a = int(input('enter a number: '))

# 1. Convert to string to easily count digits and loop through them
num_str = str(a)
power = len(num_str)

# 2. Calculate the sum of digits raised to the power
total_sum = sum(int(digit) ** power for digit in num_str)

# 3. Check and print the result
if total_sum == a:
    print("Armstrong number")
else:
    print("not Armstrong number")'''
