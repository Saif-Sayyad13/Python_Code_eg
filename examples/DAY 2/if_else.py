# if the given condition is true it will execute in true statr is true it will excuacte in true state block
#but if the condition become false it wont show blank space it will exci=ute in false stae block
# False state block is also called as else block
# True state block is also called as True state block

'''# Synta:- 
if condition:
    statement(True state block)
else:
    statement(False state block)
'''

'''
# wap a check the given number is even print question and reminder else make it as a square
s=20
if s%2==0:
    print("Q------->",s//2,)
    print("Reminder",s%2)
else:
    print(s**2)
    
s=21
if s%2==0:
    print("Q------->",s//2,)
    print("Reminder",s%2)
else:
    print(s**2)
    
# if the given dic len is even print as it is and if the len is odd add a keypair

s={1:2,4:5,8:9}
if len(s)%2==0:
    print(s)
else:
    s[100]="hi" # var_name[key]=value (without using inbuild)
    print(s)
#or
s={1:2,4:5,8:9}
if len(s)%2==0:
    print(s)
else:
    s.update({"Python":"SQl"}) # var_name.update({key:value})
    print(s)
    
# wap to check the no is odd if the given no is odd print as it is if even convert to -ve
a=eval(input("Enter a number"))
if a%2==1:
    print(a)
else:
    print(-a) # we we can also use abs it convert +ve to -ve
    '''
'''#WAP to check whether a number is positive or negative. If Positive print positive
#message or else print Negative Number.
a=eval(input("Enter a number"))
if a>0:
    print("positive number")
else:
    print("number is negative")
    '''

'''#WAP to check whether a number is even or odd. If even, print message an even
#or else print message as odd.
a=eval(input("Enter a number"))
if a%2==0:
    print(f"Number {a} is even ")
else:
    print(f"Number {a} is odd")'''
    
'''#Write a program to check whether a given number is greater than 10 or not. if it
#is greater than 10 print message as greater or else print that number with not a greater than.
a=eval(input("Enter a number"))
if a>10:
    print(f"{a} is grater than 10")
elif a==10:
    print(f"{a} is equal to {10}")
else:
    print(f"{a} is less than 10")'''
    
'''#WAP to check whether the given two input numbers are divisible by 3 and 5. If it
#is divisible, print “Good Morning”, if it is not divisible print “Good Evening”.
a=eval(input('Enter the first  number' ))
a=eval(input('Enter the second number' ))
if a%3==0 and a%5==0:
    print("Good Morning")
else:
    print("Good Evening")'''

'''#WAP to accept two integers and check whether those two values are equal or not.
#If equal, multiply to value or else to display the quotation value.
a=eval(input('Enter a number'))
b=eval(input('enter another number'))
if a==b:
    print(a*b)
else:
    print(a/b)
'''

'''#WAP to find the largest of two numbers.
a=eval(input('enter a number'))
b=eval(input('enter other no'))
if a>b:
    print(f'{a} is greater than{b}')
else:
    print(f'{b} is greater than {a}')
    '''
    
'''#WAP to find the smallest of two numbers.
a=eval(input('enter a number'))
b=eval(input('enter other no'))
if a<b:
    print(f'{a} is smaller than{b}')
else:
    print(f'{b} is smaller than {a}')'''
    
#WAP to check whether the input number is greater than 10 or not if it is greater
#than 10 print messages as greater with number. if it is not a greater than 10 print that number.

'''#WAP to the given number integer, if n is greater than 21,print the absolute
#difference between n and 21 otherwise print twice the absolute difference
a=eval(input('enter a number'))
diff = abs(a - 21)
if a > 21:
    print(diff)
else:
    print(2 * diff)
    
'''
'''
#WAP to check whether a given value is less than 125 and in between 47 to 125 or
#not. if condition is True, to perform store the given value as key and value as a
#character into the dict or else to append the value in list and display it.
# Initialize an empty dictionary and an empty list
dict = {}
list = []
a = eval(input("Enter a number: "))
if a < 125 and 47 <= a <= 125:
    char_val = chr(a)
    dict[a] = char_val
    print("Condition True! Stored in dictionary:")
    print(dict)
else:
    list.append(a)
    print("Condition False! Appended to list:")
    print(list)
'''
'''
#WAP to check whether the given string of the first character is a special symbol
#or not. If a special symbol, to extract and display the middle character or else to
#reverse the string and display the half of the string
#text = input("Enter a string: ")

a= text[0]
if not (a.isalpha() or a.isdigit()):
    mid_index = len(text) // 2
    mid_char = text[mid_index]
    print("Starts with a special symbol. Middle character is:")
    print(mid_char)
else:
    reversed_text = text[::-1]
    half_length = len(reversed_text) // 2
    half_text = reversed_text[:half_length]
    
    print("Does not start with a special symbol. Half of reversed string:")
    print(half_text)
'''





#WAP to check whether the given number is even or odd. If it is even then make
#it as an add number, if it is an odd number then make it as even number.


#Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
#If the pen is available in the shop, he will buy the pen. If it is not there he will
#come out of the shop.


'''

#WAP to perform addition and subtraction operation by using list collection if the
#first and middle data items number are even performing addition operation, or
#else performing subtraction
a=[10,20,30,40,50,60,70]
low=a[0] # first index
high=len(a)-1 # len is 7 len-1 =6 its index start from 0
first_element=a[0]
print(first_element)
mid_element=(low+high)//2
print(mid_element)
print(a[mid_element])

'''


'''#WAP to check whether the first item of these two lists is either integer or not.
#If it is an integer, concatenate these two lists or else print the memory
#address of these two lists.
# Define your two sample lists
a = [5,10,15,20,25]
b = [10, 20,30,40,50]
if type(a[0]) == int and type(b[0]) == int:
    result = a +b
    print("Both start with integers. Combined list:")
    print(result)
else:
    print("They do not both start with integers. Memory addresses:")
    print(f"List 1 Address: {id(a)}")
    print(f"List 2 Address: {id(b)}")

''''''
#WAP to check whether the input character is a vowel or not. If it is vowel print
#‘VOWEL’ along with that character, if it is not just print ‘CONSONANT
char = input("Enter a character: ")
vowels = "aeiouAEIOU"
if char in vowels:
    print(f"VOWEL: {char}")
else:
    print("CONSONANT")
'''
'''#WAP to check whether a given character is a vowel or consonant. if vowel, to
#print the next character of a given character or else print previous characters.

char = input("Enter a character: ")
vowels = "aeiouAEIOU"
if char in vowels:
    next_char = chr(ord(char) + 1)
    print(f"It is a vowel. Next character: {next_char}")
else:
    prev_char = chr(ord(char) - 1)
    print(f"It is a consonant. Previous character: {prev_char}")

'''
''''''''


'''
#WAP to check whether a given string is less than 3 characters, to print the entire
#string otherwise to print after third positions to the remaining string.

a = input("Enter a string: ")

if len(a) < 3:
    print("Length is less than 3. Entire string:")
    print(a)
else:
    remaining_text = a[3:]
    print("Length is 3 or more. Remaining string after 3rd position:")
    print(remaining_text)
'''
'''
#WAP to check whether a given length of the string is even or not. if even, to
#append the new string called "bye" or else print the first and last characters.

a = input("Enter a string: ")
if len(a) % 2 == 0:
    new_text = a + "bye"
    print("Length is even. Appended 'bye':")
    print(new_text)
else:
    first_char = a[0]
    last_char = a[-1]
    
    print("Length is odd. First and last characters:")
    print(first_char, last_char)
'''
'''#WAP to check whether a given length of the string is odd or not. if odd, to append
#the new string("Haii") from the starting of the given string, or else to avoid the
#starting character and ending character of the given
#string and to display the remaining characters.

a = input("Enter a string: ")
if len(a) % 2 != 0:
    new_text = "Haii" + a
    print("Length is odd. Added 'Haii' to the front:")
    print(new_text)
else:
    remaining_text = a[1:-1]
    print("Length is even. Showing remaining characters:")
    print(remaining_text)
'''
'''
#WAP to check whether the last of the given string is a special character or not, if
#the special character prints reverse the string except the last character or else to
#check if the length of the string is odd or not, if odd to extract the middle
#character to the end of the string.

a = input("Enter a string: ")
last_char = text[-1]
if not (last_char.isalpha() or last_char.isdigit()):
    main_part = a[:-1]
    reversed_part = main_part[::-1]
    
    print("Ends with a special character. Reversed except last:")
    print(reversed_part)
    
else:
    if len(a) % 2 != 0:
        middle_index = len(a) // 2
        middle_to_end = text[middle_index:]
        
        print("Length is odd. Slicing from middle to end:")
        print(middle_to_end)
    else:
        print("Ends with normal character and length is even. Nothing to do.")
        
        
        ###var_name
'''


'''
WAP to check whether a given year is a leap year or not. if leap year, print leap
year or else not a leap year.
WAP to find out the greatest of two numbers and display the greatest number. if
the greatest number, display the greatest message with value.
WAP to check whether the given value is present inside the given collection or
not.if value is present, display the value is available or else the value is not
present.
WAP whether a given string, if string length is more than 2, then it displays a new
string with the first and last characters switched, otherwise the display the 3
copies of given string.
WAP to check whether a given value is a list and first and last values should be
integer if condition is satisfied first value is True division by 3 and perform the
bitwise not for last value and those result values are stored in same positions in
given list or else, to perform length of the collection power by 2 and display
value.
WAP to check whether a given value is a string or not and length of the value
should be more than 7, if condition is satisfied to append the new string in the
middle of the given string or else to perform the replications with 3 and display
the result.
WAP to check if the given string of first and second character should be sequence
or not. if the sequence prints the first, second and last two characters, or else the
first half string is reversed and the remaining half string should be normal and
display it.
WAP to check whether a given value is present inside the collection or not. If
present, print the value or else print value is not found.
WAP to check whether a given key is present in the dict or not. if key is present:
display the value or else add key and new value inside the dict.
WAP to check whether a given collection is set or not. if set, append the new
value, or else eliminate the duplicate values in collection. final results should be
set type.
WAP to read the age of a candidate and determine whether it is eligible for
his/her own vote or not.it eligible print age and eligible messages or else print
not eligible.
WAP to check whether a given value is even and in between 47 to 58 and not in
0 or odd. if condition is True, to perform display the ascii character or else to
perform floor division with 5 and display it.
WAP to check whether the given string is palindrome or not if it is a palindrome
string palindrome along with the string if it is not a palindrome print not
palindrome
WAP to check whether a given number is palindrome or not. If palindrome,
display the given value as a palindrome or else not a palindrome.
WAP to check length of both string collections are equal or not. if both are equal
print the concat the two strings and display, or else if any one of the collection
not equal print both the collections with lengths
WAP to check whether both given values point to the same memory location or
not. if it is true print the middle item of the second collection, or else if it is false
print the first item and last item of the first collection along with the memory
address.
WAP to check whether a given string collection is more than ten, and the first +
last character of the ascii values should be divisible by 5, if condition is satisfied
print first, middle, last characters ASCII values or else print the string three
times.
WAP to check whether the middle of the item present in the list is string data type
or not if it is string print that list or else if it is not string then print that middle
item.
WAP Given a string, return a new string where the first and last characters have
been exchanged.
Write a program to find out such numbers which are divisible by 7 but are not a
multiple of 5. Both the conditional is satisfied and print actual value. if one
condition is not satisfied actual number is multiply by 4 and print result
WAP to check whether two values are pointing to the same memory address or
not. If the same memory displays the address or else displays the two values
addresses.
WAP to check whether a given input character is a special symbol or not if it is a
special symbol then print that character three times and tell print that character
5 times.
WAP to check length of both string collections equal or not if it is equal print the
connection of any one of the collections if it is not equal print both the collection.
WAP To check whether both input variables point to the same memory location
or not if it is true print the last item of the second collection, if it is false print the
first item of the first collection along with the memory address.
WAP to print the string collection five times when the length of the string
collection should be more than 3 and the middle character of the string should
be vowel and the first character ASCII value should be even, to print the previous
character of middle character, or else if ASCII value is odd then print the string
three times as print that string.
'''
