'''1. Print numbers from 1 to 10 using a for loop.
2. Print all even numbers from 1 to 20.
3. Find the sum of all numbers in a list.
4. Count the even numbers in a list.
5. Find the largest number in a list without using max().
6. Count the vowels in a string.
7. Reverse a string using a for loop.
8. Remove duplicates from a list while keeping the original order.
9. Find the first number greater than 100 in a list; stop once found.
10. Print a multiplication table for a number entered by the user.

Here are 10 tough for-loop coding questions. Write only the code for each—no explanation needed.
1. Find the second-largest distinct number in a list without using sort() or max().
2. Given a list of integers, create a new list containing only values that occur exactly once.
3. Check whether a string is a palindrome without using slicing ([::-1]) or reversed().
4. Find the first repeated character in a string. If none repeats, print "No repeat".
5. Count the frequency of every character in a string using a dictionary.
6. From a list of numbers, find all pairs whose sum equals a target value. Do not print duplicate pairs.
7. Flatten a nested list containing only one nesting level—for example, turn [[1, 2], [3, 4], [5]] into [1, 2, 3, 4, 5].
8. Print this pattern for n = 5:
*
**
***
****
*****
9. Print this number pattern for n = 5:
1
12
123
1234
12345
10. Given a list of words, group anagrams together—for example, group "eat", "tea", and "ate"
together—using loops and dictionaries.'''


'''#1. Print numbers from 1 to 10 using a for loop.
#2. Print all even numbers from 1 to 20.
#3. Find the sum of all numbers in a list.
a=[1,2,3,4,5,6,7,8,9,97,6,5,4,33]
print(sum(a))
#4. Count the even numbers in a list.
a=[1,2,3,4,5,6,7,8,9,97,6,5,4,33]
count=0
for i in a:
    if i%2==0:
        count=count+1
print(count)'''
'''#5. Find the largest number in a list without using max().
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 97, 6, 5, 4, 33]
large=a[0]
for i in a:
    if i>large:
        large=i
print(large)

'''
'''#6. Count the vowels in a string
s=" Count the vowels in a string"
count=0
for i in s:
    if i in"aeiouAEIOU":
        count=count+1
print(count)'''
'''#7. Reverse a string using a for loop.
a="Reverse a string using a for loop."
aa=" "
for i in a:
    aa=i+aa
print(aa)'''
'''
#8. Remove duplicates from a list while keeping the original order.
a = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []

for num in a:
    # Only add the number if it is unique so far
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)  # Output: [1, 2, 3, 4, 5]

#9. Find the first number greater than 100 in a list; stop once found.
numbers = [45, 88, 105, 23, 150, 9]

for num in numbers:
    if num > 100:
        print("Found:", num)
        break  # Stops the loop instantly so 150 is ignored

#10. Print a multiplication table for a number entered by the user.
# 1. Get input and convert it to a number
num = int(input("Enter a number: "))

# 2. Loop from 1 to 10
for i in range(1, 11):
    result = num * i
    # 3. Print the formatted row
    print(f"{num} x {i} = {result}")
'''