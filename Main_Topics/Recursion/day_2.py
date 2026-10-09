'''Recursion is when a function calls itself.

Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of meaning that you can 
loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into 
writing a function which never terminates, or one that uses excess amounts of memory or 
processor power. However, when written correctly recursion can be a very efficient and 
mathematically-elegant approach to programming.
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
Base Case and Recursive Case
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error.

Example
Identifying base case and recursive case:

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
'''
'''def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)'''

'''#Find the 7th number in the Fibonacci sequence:

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))'''

'''#Calculate the sum of all elements in a list: recursion in list

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))'''

'''#Find the maximum value in a list:

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))



'''
"""

kuch bhi likh hai i also dont know
def even(n,i=0,out=''):
    if i>=len(n):
        return out
    if n[i]%2==0:
        out+=str(n[i])+' '
    return even(n,i+1,out)  
def odd(n,i=0,out=''):
    if i>=len(n):
        return out
    if n[i]%2!=0:
        out+=str(n[i])+' '
    return odd(n,i+1,out)

def main(s,i=0,out=''):
    b=s.split()
    if i>=len(b):
        return out
    if len(b[i])%2==0:
        out+=b[i]+' '
    return main(s,i+1,out)
print(main('HaI hEllo NaNDii'))
"""

#11. WAP to get the following output.
#In = ['hai', [34+j, True, 78, 9+2j], 'sample', (3, 7j+9), {19+20j, 34, 89},
 #     {'a':10}, 'data', [2+4j, 3.8,7.9]]
#Out = ['iah', [3+4j, 9+2j], 'elpmas', (7+9j), {19+20j}, 'atad', [2+4j]]
# Input data list
In = ['hai', [34+1j, True, 78, 9+2j], 'sample', (3, 7j+9), {19+20j, 34, 89}, {'a':10}, 'data', [2+4j, 3.8, 7.9]]

Out = []

for i in In:

    if isinstance(i, str):
        Out.append(i[::-1])

    elif isinstance(i, list):
        Out.append([x for x in i if isinstance(x, complex)])

    elif isinstance(i, tuple):
        complex_nums = [x for x in i if isinstance(x, complex)]

        if len(complex_nums) == 1:
            Out.append(complex_nums[0])
        else:
            Out.append(tuple(complex_nums))

    elif isinstance(i, set):
        Out.append({x for x in i if isinstance(x, complex)})

print("Out =", Out)
