'''class X:
    def __init__(self):
        print("X class constructor")
x=X()

print()
class Student:
    def __init__(self):
        self.name = "Prabhu"

s1 = Student()
print(s1.name)

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 20000)
m2 = Mobile("Apple", 80000)

print(m1.brand, m1.price)
print(m2.brand, m2.price)

'''

'''class demo:
    a=10
    @classmethod
    def info(cls):
        #cls.a=20
        print("The class")
        print(cls.a)
s=demo()
demo.info()
s.info()
a=29
print(a)'''
'''
def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check factors from 2 up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a factor, so it's not prime
            
    return True  # No factors found, it is prime

# --- Example Usage ---
number = 29
if is_prime(number):
    print(f"{number} is a prime number!")
else:
    print(f"{number} is NOT a prime number.")
'''
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))

if is_prime(user_number):
    print(f"{user_number} is a prime number!")
else:
    print(f"{user_number} is NOT a prime number.")


'''
'''Reverse an array/string in plac
two-pointer pattern 
def reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
'''
'''def is_palindrome(s):
    
    #s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("level"))
'''

'''a='level'
if a==a[::-1]:
    print("Palindrome")'''
    
'''   
from typing import Counter


def first_unique(s):
    from collections import Counter
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None
print(first_unique("swiss"))  # Output: 'w'''