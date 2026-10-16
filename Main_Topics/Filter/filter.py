'''
 FILTER
*filter is an inbuilt class which is used to filter default values.
*it will accept only 2 arguments that are "function and iterable".
*if the function is returned o/p as default value then it will filter that input.
*if the function is not returning any default value then it will keep the input.
*the output of the filter will be object format.
syntax:
-------
filter(function_name, iterable)
note:
-----
*no need of specifying map() class when we use filter, because filter itself only passes the input to function.
""
 
'''
'''a=[11,20,31,40]
res=filter(lambda x:x%2==0,a)
print(list(res))'''

'''d=('King','queen','Monkey','Donkey','patanahi')
res=filter(lambda x:x[0].isupper(),d)
print(list(res))'''

'''
l = [4, 3, 5, 6, 7, 8, 10]

# Using a list comprehension
even_list = [num for num in l if num % 2 == 0]
print(even_list)
# Output: [4, 6, 8, 10]
l = ["sun flowers", "banana tree", "lily flowers", "lotus flower", "marigold flowers"]

# Filtering elements that contain the word "flower"
flower_list = [item for item in l if "flower" in item]
print(flower_list)
# Output: ['sun flowers', 'lily flowers', 'lotus flower', 'marigold flowers']
l = ["hello", "guys", "please", "respond", "to", "insta", "computer"]
vowels = "aeiouAEIOU"

# Filtering elements whose first letter is not a vowel
consonant_list = [word for word in l if word and word[0] not in vowels]
print(consonant_list)
# Output: ['hello', 'guys', 'please', 'respond', 'to', 'computer']
k = ["apple", "google", "walmart", "fb", "insta", "act", "zomato"]

# Using filter() with a lambda function
even_length_strings = list(filter(lambda x: len(x) % 2 == 0, k))
print(even_length_strings)
# Output: ['google', 'walmart', 'fb', 'zomato']
m = [-5, -6, 9, -34, 90, -28, 78, 100, 89, 45, -65]

# Using filter() with a lambda function to get values greater than 0
positive_values = list(filter(lambda x: x > 0, m))
print(positive_values)
# Output: [9, 90, 78, 100, 89, 45]
# 1. Generate the range from 1 to 100 (101 is exclusive)
numbers = range(1, 101)

# 2. Use filter with a lambda function to check for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 3. Print the result
print(even_numbers)


'''
