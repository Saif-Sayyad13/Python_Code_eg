'''
LAMBDA FUNCTION/ANONYMOUS FUNCTIONS
Anonymous function is a function that is defined without a def keyword
Anonymous function will be defined by using “lambda” keyword
It can take any number of arguments
Simple lambda function syntax
Lambda arg1,arg2,arg3…:expression/return_value
Lambda function with if-else statement
Lambda arg1 :True state Block if condition else False state block
Lambda functions with comprehensions
Lambda arg1:comprehension

Drawbacks
*we can’t write return keyword
*we can’t return multiple values,if we want return explicitly we should enclose in tuple format
*we can’t use equal(+=)/(=) operator
*we can’t use for loop (if we want to use then we should write comprehension)
'''



'''a=lambda x:x*2
print(a(5))'''
'''
words = ["python", "java", "selenium"]
result = [char for word in words for char in word]
# Output: ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 's', 'e', 'l', 'e', 'n', 'i', 'u', 'm']
matrix = [[1, 2, 3], [4, 5, 6]]
result = [(num, num**2) for sublist in matrix for num in sublist]
# Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
nums = [1, 2, 3, 4]
result = [(a, b) for a in nums for b in nums if (a + b) % 2 == 0]
# Output: [(1, 1), (1, 3), (2, 2), (2, 4), (3, 1), (3, 3), (4, 2), (4, 4)]
words_list = [["apple", "ant"], ["banana", "ball"], ["cat", "car"]]
result = [word for sublist in words_list for word in sublist if word[0] == word[-1]]
# Output: [] (None of the words in the provided lists match this criterion)
numbers = [[12, 15, 18], [21, 24, 27], [30, 33, 36]]
result = [num for sublist in numbers for num in sublist if num % 3 == 0 and num % 2 != 0]
# Output: [15, 21, 27, 33]
words = ["apple", "orange", "grapes", "kiwi"]
result = [char for word in words if len(word) % 2 == 0 for char in word]
# Output: ['o', 'r', 'a', 'n', 'g', 'e', 'g', 'r', 'a', 'p', 'e', 's', 'k', 'i', 'w', 'i']
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = [(num, row_idx) for row_idx, sublist in enumerate(matrix) for num in sublist]
# Output: [(1, 0), (2, 0), (3, 0), (4, 1), (5, 1), (6, 2), (7, 2), (8, 2), (9, 2)]
words = ["listen", "silent", "enlist", "hello"]
result = [(w1, w2) for i, w1 in enumerate(words) for w2 in words[i+1:] if sorted(w1) == sorted(w2)]
# Output: [('listen', 'silent'), ('listen', 'enlist'), ('silent', 'enlist')]
'''
'''
# The range(1, 6) includes numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

text = "Python programming is fun"
word_lengths = [len(word) for word in text.split()]
print(word_lengths)
# Output: [6, 11, 2, 3]

text = "Python programming is fun"
word_lengths = [len(word) for word in text.split()]
print(word_lengths)
# Output: [6, 11, 2, 3]

import math

numbers = [3, 4, 5, 6]
factorials = [math.factorial(num) for num in numbers]
print(factorials)
# Output: [6, 24, 120, 720]

inp = 'PYTHON IS EASY'
outp = {word: word.lower() for word in inp.split()}
print(outp)

# Output: {'PYTHON': 'python', 'IS': 'is', 'EASY': 'easy'}

d = {10: "ten", "hai": "value", (1, 2, 3): "colln", 1.2: "decimal"}

# Collection types like tuple are not individual/primitive data types
result = {}
for key, value in d.items():
    if isinstance(key, (int, float, str, bool)):
        result[key] = value
    else:
        result[key] = type(key)

print(result)
# Output: {10: 'ten', 'hai': 'value', (1, 2, 3): <class 'tuple'>, 1.2: 'decimal'}


'''