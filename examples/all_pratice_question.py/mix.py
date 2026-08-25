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

'''#1. Find the second-largest distinct number in a list without using sort() or max().
a =eval(input('likho')) #[12, 2, 3, 4, 4, 5, 65, 3]
big=0
big2=0
for i in a:
    if i>big:
        big2=big
        big=i
print(big2)
'''

'''#2. Given a list of integers, create a new list containing only values that occur exactly once.
a=[12, 2, 3, 4, 4, 5, 65, 3]
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)'''
'''#3. Check whether a string is a palindrome without using slicing ([::-1]) or reversed().
text = "racecar"

# Assume it is a palindrome until proven otherwise
is_palindrome = True  
length = len(text)

# Loop through the first half of the string
for i in range(length // 2):
    # Compare character from front with character from back
    if text[i] != text[length - 1 - i]:
        is_palindrome = False
        break  # Stop immediately if letters don't match

print(is_palindrome)  # Output: True
'''

"""#4. Find the first repeated character in a string. If none repeats, print "No repeat".
text = "abcdefd"
seen = []  # List to track characters we already looked at
result = "No repeat"

for char in text:
    if char in seen:
        result = char
        break  # Stop immediately at the first repeat
    seen.append(char)

print(result)  # Output: d

#5. Count the frequency of every character in a string using a dictionary.
text = "apple"
freq = {}  # Empty dictionary to store counts

for char in text:
    if char in freq:
        freq[char] += 1  # If already in dict, add 1
    else:
        freq[char] = 1   # If new, start at 1

print(freq)  # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

#6. From a list of numbers, find all pairs whose sum equals a target value. Do not print duplicate pairs.
nums = [2, 4, 3, 5, 7, 8, 9]
target = 7
seen_pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            # Create a small pair and always keep it sorted to easily avoid duplicates
            pair = sorted([nums[i], nums[j]])
            if pair not in seen_pairs:
                seen_pairs.append(pair)
                print(pair)  # Output:, [3, 4]

#7. Flatten a nested list containing only one nesting level—for example, turn [[1, 2], [3, 4], [5]] into [1, 2, 3, 4, 5].
nested = [[1, 2], [3, 4], [5]]
flat = []

# Loop through the outer list, then loop through each inner list
for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)  # Output: [1, 2, 3, 4, 5]

#8. Print this pattern for n = 5:
n = 5

for i in range(1, n + 1):
    print("*" * i)  # Multiplies the string "*" by the line number

'''*
**
***
****
*****'''
#9. Print this number pattern for n = 5:
n = 5

for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j)  # Add numbers side-by-side as text
    print(row)

'''1
12
123
1234
12345'''

#10. Given a list of words, group anagrams together—for example, group "eat", "tea", and "ate"
#together—using loops and dictionaries
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for w in words:
    # Sorting a word alphabetically (e.g., "eat" -> "aet") gives it a unique key
    key = "".join(sorted(w))
    
    if key in groups:
        groups[key].append(w)
    else:
        groups[key] = [w]

# Print just the grouped lists
print(list(groups.values())) 
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

a="Jidnyasha"
aa=" "
for i in a:
    aa=i+aa
print(aa)


a="Jidnyasha"
print(a[::-1])

y="Hello"
for i in range(len(y)):
    print(i+100,y[i])
    
a=[100,121,134,170]
for i in a:
    if i ==121:
        print(i)

    
a="Hello"
for i in a.replace("l","-"):
    print(i,end=" ")

a=[[1,2,3],[4,5,"hi"]]
a[1][2]





#a="welcome to the club"
#output 'w':[welcome],'t':[To]
a = 'welcome to the club'
d={}
for i in a.split():
    d.update({i[0]:(i)}) 
print(d)

a="India"
for i in a:
    if i in "AEIOaeuiou":
        print(i,ord(a),ord(z)-32)
        
    

