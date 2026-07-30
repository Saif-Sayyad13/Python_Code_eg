
# Conditional Statement:
'''
- Control the flow of program execution based on the condition.
- Types of conditional statements:
  1. simple if / if condition
     - If the given condition is working/satisfied it will execute the true state block.
     - If the given condition is not working/satisfied it will show blank space.

            start
              |
              |
          condition
              |
              |
         _______________
     true|             |false           
         |             |
  it will execute    it will skip the code
  true state block    and show the blank space

    - syntax:
        if condition:
            statement
    - Here 'if' is keyword and statement is true state block
    - space before statement is tab space if we miss the the tab space it will show indentation error
    - if we miss colon(:) it will show syntax error --> code is started
    - condition ---> expression : True/False
''' 

# 1. write a program to check the given number is +ve (by using user-input)
'''
num = eval(input("Enter the number: "))
if num > 0:
    print(f"The given number {num} is positive.")
'''
# 2. write a program to check the given number is -ve
'''
num = eval(input("Enter the number: "))
if num < 0:
    print(f"The given number {num} is negative.")
'''
# 3. write a program to check that given number is even (using % )
'''
num = eval(input("Enter the number: "))
if num % 2 == 0:
    print(f"The given number {num} is even number.")
'''
# 4. write a program to check that given number is even (without using % )
'''
num = eval(input("Enter the number: "))
if (num // 2)*2 == num:
    print(f"The given number {num} is even number.")
'''
# 5. wap to check the given number is even without using % and // symbol
'''
num = eval(input("Enter the number: "))
if num & 1 == 0:
    print(f"The g1 number {num} is even number.")
'''
# 6. wap to check the given number is odd without using % and // symbol
'''
num = eval(input("Enter the number: "))
if num & 1 == 1:
    print(f"The g1 number {num} is odd number.")
'''
# 7. wap to check the given string is even length
'''
a = (input("Enter the string: "))
if len(a) % 2 == 0:
    print(f"The g1 string {a} is even length.")
'''
# 8. wap to check the given number is even then conver the number into complex
'''
num = eval(input("Enter the number: "))
if num % 2 == 0:
    print(complex(num))
'''
# 9. wap to check the given number is even store into the list
'''
y = 4
k = []
if y % 2 == 0:
    k.append(y)
    print(k)
'''
# 10. wap to check the given number is even store into the list (without using inbuilt method)
'''
s = 40
k = []
if s % 2 == 0:
    k = k+[s]
    print(k)
'''
# 11. wap to check the given data type is a string
'''
a = eval(input("Enter the data:"))
if type(a) == str:
    print("String Data type")
'''
'''
a = eval(input("Enter the data: "))
if isinstance(a, str):
    print("String Data Type")
'''
# 12. wap to check the given data type is sequence data type
'''
a = eval(input("Enter the data: "))
if isinstance(a, (str, list, tuple)):
    print("Valid Data type")

Syntax of isinstance:--> isinstance(var, (datatype1, DT2, DT3,...))
'''
'''
a = eval(input("Enter the Data: "))
if type(a) in (str, list, tuple):
    print("Valid Data Type")
'''
# 13. wap to check the given word is palindrome (string)
'''
a = eval(input("Enter the data: "))
if a == a[::-1]:
    print("Palindrome!")
'''
# 14. wap to check the given word is palindrome (int)
'''
a = eval(input("Enter the data: "))
if str(a) == a[::-1]:
    print("Palindrome!")
'''
'''
x = int(input("Enter the data: "))
if (x // 100) == x % 10:
    print("Number is Palindrome")
'''
# 15. wap to check the given number is divisible by 2 and 6
'''
num = int(input("Enter the number: "))
if num % 2 == 0 and num % 6 == 0:
    print("The number is divisible by both 2 and 6")
'''
# 16. wap to check the given key is is part of group
'''
x = [11, 12, 13, 14]
key = 12
if key in x:
    print("Part of group")
'''
# 17 wap to check in the given string last character ends with k and starts with g
'''
y = "good luck"
if y.endswith('k'):
    print("Ends with K")

if y.startswith('g'):
    print("Starts with g")
'''


#1. Check Positive Number
'''
num = int(input("Enter the number: "))
if num > 0:
    print(f"{num} is positive number.")
else:
    print(f"{num} is negative number.")
'''
#2. Check Negative Number
'''
num = int(input("Enter the number: "))
if num < 0:
    print(f"{num} is negative number.")
else:
    print(f"{num} is positive number.")
'''
#3. Check Zero
'''
num = int(input("Enter the number: "))
if num == 0:
    print("Number is zero")
else:
    print("Not zero")
'''
#4. Eligible to Vote
'''
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
'''
#5. Driving License
'''
age = int(input("Enter age: "))
if age >= 18:
    print("Driving License allowed")
else:
    print("Not allowed")
'''
#6. Pass Student
'''
marks = int(input("Enter the marks: "))
if marks >= 35:
    print("Student is passed")
else:
    print("Student is fail")
'''
#7. Salary Eligible
'''
sal = int(input("Enter salary: "))
if sal > 10000:
    print("Eligible for Loan")
else:
    print("Not eligible for loan")
'''
#8. Adult Person
'''
age = int(input("Enter Age: "))
if age >= 18:
    print("Adult Person")
else:
    print("Not an Adult")
'''
#9. Temperature Check
'''
temp = eval(input("Enter temperature: "))
if temp > 36:
    print("Hot weather")
else:
    print("Cold weather")
'''
#10. ATM Balance
'''
bal = int(input("Enter the balance: "))
if bal > 0:
    print(f"You have {bal} balance in Account")
else:
    print("Negative bank balance")
'''
#11. Even Number
'''
num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"The number {num} is Even number")
else:
    print(f"The number {num} is not even number")
'''
'''
num = int(input("Enter the number: "))
if (num // 2)*2 == num:
    print(f"The given number {num} is Even number")
else:
    print(f"The number {num} is not even number")
'''
'''
num = int(input("Enter the number: "))
if num & 1 == 0:
    print(f"The g1 number {num} is Even number")
else:
    print(f"The number {num} is not even number")
'''
#12. Odd Number
'''
num = int(input("Enter the number: "))
if num % 2 == 1:
    print(f"The number {num} is Odd number")
else:
    print(f"The number {num} is not odd number")
'''
'''
num = int(input("Enter the number: "))
if num % 2 != 0:
    print(f"The given number {num} is Odd number")
else:
    print(f"The number {num} is not odd number")
'''
#13. Divisible by 5
'''
num = int(input("Enter the number: "))
if num % 5 == 0:
    print(f"The number {num} is divisible by 5")
'''
#14. Divisible by 10
'''
num = int(input("Enter the number: "))
if num % 10 == 0:
    print(f"The given number {num} is divisible by 10")
else:
    print(f"The given number {num} is not divisible by 10")
'''
#15. Divisible by 3
'''
num = int(input("Enter the number: "))
if num % 3 == 0:
    print(f"The number {num} is divisible by 3")
else:
    print("Not divisible by 3")
'''
#16. Multiple of 7
'''
num = int(input("Enter the number: "))
if num % 7 == 0:
    print(f"The given number {num} is multiple of 7")
else:
    print("Not multiple of 7")
'''
#17. Check Leap Year
'''
year = int(input("Enter the year: "))
if year % 4 == 0:
    print(f"The Year is Leap year")
else:
    print("Not leap year")
'''
#18. Square Greater Than 100
'''
num = int(input("Enter the number: "))
if num**2 > 100:
    print(f"{num} square is grater than 100")
else:
    print("no")
'''
#19. Cube Greater Than 500
'''
num = int(input("Enter the number: "))
if num**3 > 500:
    print(f"{num} cube is greater than 500")
else:
    print("nope")
'''
#20. Number Ends with Zero
'''
num = int(input("Enter the number: "))
if num % 10 == 0:
    print(f"The number {num} ends with zero")
else:
    print("Not ends with zero")
'''
#21. Empty String
'''
a = input("Enter the string: ")
if a == str():
    print("String is Empty")
else:
    print("Not emoty string")
'''
#22. Name Starts with A
'''
name = input("Enter Name: ")
if name.startswith("A"):
    print("Name starts with 'A'")
else:
    print("nahhh")
'''
#23. Name Ends with n
'''
name = input("Enter Name: ")
if name.endswith("n"):
    print("Name ends with 'n'")
else:
    print("NOOOO")
'''
#24. Length Greater than 5
'''
a = eval(input("Enter data: "))
if len(a) > 5:
    print(f"Length of {a} is greater than 5")
else:
    print("Not greater than 5")
'''
#25. Check Uppercase
'''
a = input("Enter string: ")
if a.isupper():
    print(f"The string {a} is in Uppercase")
else:
    print("not in uppercase")
'''
#26. Check Lowercase
'''
a = input("Enter string: ")
if a.islower():
    print(f"The string {a} is in Lowercase")
else:
    print("not in lowercase")
'''
#27. Alphabet Only
'''
a = input("Enter data: ")
if a.isalpha():
    print("Alphabet only")
else:
    print("Invalid")
'''
#28. Digits Only
'''
a = input("Enter data: ")
if a.isdigit():
    print("Digits only")
else:
    print("Invalid")
'''
#29. Alphanumeric
'''
a = input("Enter data: ")
if a.isalnum():
    print("Alphanumeric string")
else:
    print("Invalid")
'''
#30. Check Space
'''
a = input("Enter data:")
if " " in a:
    print("Space")
else:
    print("Invalid")
'''
#31. Check List Empty
'''
a = eval(input("Enter data: "))
if a == list():
    print("Empty List")
else:
    print("Not empty list")
'''
#32. List Length Greater Than 5
'''
a = eval(input("Enter data: "))
if len(a) > 5:
    print("List length is greater than 5")
else:
    print("Not greater than 5")
'''
#33.Number Exists in List
'''
a = int(input("Enter number: "))
b = eval(input("Enter list: "))
if a in b:
    print("Number exists in list")
else:
    print("Number not exist")
'''
#34.Largest Element Greater Than 100
'''
a = eval(input("Enter data: "))
if max(a) > 100:
    print(f"Largest number greater than 100 is {max(a)}")
else:
    print("uhhh")
'''
#35.Smallest Element Less Than 0 Program x = [11, -5, 35, 507]
'''
a = eval(input("Enter data: "))
if min(a) < 0:
    print(f"Smallest Element less than 0 is {min(a)}")
else:
    print("trash")
'''
#36.Sum Greater Than 500. x = [100, 200, 150, 90]
'''
a = eval(input("Enter Data: "))
if sum(a) > 500:
    print(f"Sum {sum(a)} is Greater than 500")
else:
    print("Not greater than 500")
'''
#37.List Sorted (Ascending Order) x = [10, 20, 30, 40, 50]
'''
a = eval(input("Enter data: "))
if a == sorted(a):
    print("List Sorted in Ascending Order")
else:
    print("Not sorted")
'''
#38.wap to check age>18 and salary is greater than 30000 age = 25   salary = 40000
'''
age = int(input("Enter the Age: "))
sal = int(input("Enter the Salary: "))
if age > 18 and sal > 30000:
    print("Valid")
else:
    print("Invalid")
'''
#39.wap to match Username and Password Match(user input)
'''
userName = input("Enter the Username: ")
password = input("Enter the Password: ")
if userName == 'Admin' and password == 'ankita':
    print("Condition satisfied")
'''
#40.wap to check Marks > 35 and Attendance > 75(take user input)
'''
marks = int(input("Enter the marks: "))
attendance = int(input("Enter Attendance: "))
if marks > 35 and attendance > 75:
    print("Condition satisfied")
else:
    print("Invalid")
'''
#41.wap to check the given number even and Positive
'''
num = int(input("Enter the number: "))
if num % 2 == 0 and num > 0:
    print(f"The number {num} is even and positive")
else:
    print("no")
'''
#42.wap to check given Number Between 1 and 100
'''
num = int(input("Enter the number: "))
if 1 < num < 100:
    print(f"The number {num} is between 1 and 100")
else:
    print("Not between 1 n 100")
'''
#43.wap to check the given number Divisible by 3 and 5
'''
num = int(input("Enter the number :"))
if num % 3 == 0 and num % 5 == 0:
    print(f"The number {num} is divisible by 3 and 5")
else:
    print("not")
'''
#44.wap to check the given number Divisible by 2 or 7
'''
num = int(input("Enter the number: "))
if num % 2 == 0 and num % 7 == 0:
    print(f"The number {num} is divisible by 2 and 7")
else:
    print("Not divisible ")
'''
#45.wap to check Name Starts with 'A' and Ends with 'a' name="Anita"
'''
name = input("Enter the name: ")
if name.startswith('A') and name.endswith('a'):
    print("Condition satisfied")
else:
    print("Invalid")
'''
#46.wap to check Salary > 50000 or Experience > 5
'''
sal = int(input("Enter the Salary: "))
exp = int(input("Enter the year of experience: "))
if sal > 50000 or exp > 5:
    print("Condition True")
else:
    print("False")
'''
#47.wap to check Temperature > 35 and Humidity > 80
'''
temp = int(input("Temperature: "))
humidity = int(input("Humidity: "))
if temp > 35 and humidity > 80:
    print("True")
else:
    print("False")
'''
#48.wap to check if the student has scored 70% print "good luck "(take user input)
'''
marks = int(input("Enter scored percentage: "))
if marks > 70:
    print("good luck")
else:
    print("Need to study!!!")
'''
#49.wap to check which number is greater using if condition a=98 b=67
'''
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
'''
#50.wap to check if the given string has even length of character s="hey guys you all are Osam"
'''
s= input("Enter the string: ")
if len(s) % 2 == 0:
    print("string has even length")
else:
    print("string has odd length")
'''
#51.wap to check if the given number is divisible by 5 (take user input)
'''
num = int(input("Number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")
'''
#52.wap to check if the given programming is present in the list. p=["java","python","c","c++","RUBy","golang"]
'''
lang = input("Language: ")
p = eval(input("Enter the list: "))
if lang in p:
    print("Present")
else:
    print("Not present")
'''
#53.wap to check eligible to vote take user input as a age
'''
age = int(input("Age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
'''
#54.wap to check if the given number is positive take user input
'''
num = int(input("Number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")
'''
#55.wap to check if the given string is palindrome (take user input)
'''
s = input("String: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
#56.wap to check if the first letter in the given string is consonant. s="Lahari is a good student"
'''
s = input("String: ")
if s[0] not in "aeiouAEIOU":
    print("First letter is consonant")
else:
    print("Enter letter is vowel")
'''
#57.wap to check the given string is uppercase or not (take user input)
'''
s = input("String: ")
if s.isupper():
    print("string is in uppercase")
else:
    print("string is not in uppercase")
'''
#58.wap to check the given value is string (take user input)
'''
s = eval(input("Enter data: "))
if type(s) == str:
    print("It is a string")
else:
    print("It's not a string")
'''
'''
s = eval(input("Enter data: "))
if isinstance(s, str):
    print("It's a string")
else:
    print("It's not a string")
'''
#59.wap to display "Python Coding" if the number is greater than 1 and less than 5 (take user input)
'''
num = int(input("Number: "))
if 1 < num < 5:
    print("Python Coding")
else:
    print("Uffff")
'''
#60.wap to check whether given number is negative and print "its negative guys"
'''
num = int(input("Enter number: "))
if num < 0:
    print("It's Negative guys")
else:
    print("Dam!!")
'''
#61.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)
'''
num = int(input("Number: "))
if num % 2 == 0 and num % 6 == 0:
    print(complex(num))
else:
    print("Invalid")
'''
#62.wap to check whether the given number is even or not, if even store the value inside the list (take user input)
'''
num = int(input("Enter the number: "))
l = list()
if num % 2 == 0:
    l.append(num)
    print(l)
else:
    print("Not even")
'''
#63.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)
'''
num = int(input("Enter Number: "))
if num % 5 == 0 and num % 7 == 0:
    print(num**2)
else:
    print("False condition")
'''
#64.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,
#if satisfied, display the ascii characters (take user input)
'''
num  = int(input("Number: "))
if 45 < num < 200 and num % 4 == 0 and num % 5 == 0:
    print(chr(num))
else:
    print("No")
'''
#65.wap to checking if a string contains a substring. string="hello world" substring="world"
'''
string = input("String: ")
substring = input("Substring: ")
if substring in string:
    print("Yahhhh")
else:
    print("uhhh")
'''
#WAP to check whether a character is an alphabet or not. If it is an alphabet,
#store the value inside a dictionary (key as the character and value as its ASCII value).
'''
a = input("Enter a character: ")
d = {}
if a.isalpha():
    d[a] = ord(a)
    print(d)
else:
    print("dammm")
'''
#67.wap to check whether a character is in uppercase or not, if uppercase,
#convert to lowercase and store the value inside the dictionary (character as key and ascii as value) take user input
'''
a = input("Enter a character: ")
d = {}
if a.isupper():
    ch = a.lower()
    d[ch] = ord(ch)
    print(d)
'''
#68.Write a program to check if a string ends with a period ('.').
'''
a = input("Enter a string: ")
if a.endswith("."):
    print("The string ends with '.'")
else:
    print("False")
'''
#69.  Write a program to check if 'a' is present in the string s = 'apple'.
'''
s = "apple"
if "a" in s:
    print("'a' is present")
else:
    print("'a' is not present")
'''
#70.  Write a program to check if the first and last characters of a string are the same (e.g., x = 'level').
'''
x = input("Enter string: ")
if x[0] == x[-1]:
    print("First and last characters are the same")
else:
    print("Not same")
'''
#71.  Write a program to check if a character is a vowel. (e.g., a = 'I')
'''
c = input("Enter characeter: ")
if c in "aeiouAEIOU":
    print("Yes, it's vowel")
else:
    print("No, it's not")
'''
#72.  Write a program to check if a character is uppercase. (e.g., b = 'P')
'''
c = input("Enter character: ")
if c.isupper():
    print("Yes, it's uppercase")
else:
    print("No, it's not")
'''
#73.  Write a program to check if a character is lowercase. (e.g., c = 'k')
'''
c = input("Enter character: ")
if c.islower():
    print("Yes, it's lowercase")
else:
    print("No, it's not")
'''
#74.  Write a program to check if a character is a digit. (e.g., ch = '5')
'''
ch = input("Enter the character: ")
if ch.isdigit():
    print("It's digit")
else:
    print("It's not digit")
'''
#75.  Write a program to check if the ASCII value of a character is greater than 100. (e.g., z = 'd')
'''
z = input("Enter value of z: ")
if ord(z) > 100:
    print("Yepp")
else:
    print("Nope")
'''
#76.  Write a program to check if 5 exists in a list. (e.g., lst = [2, 4, 5])
'''
num = int(input("Enter number: "))
lst = eval(input("Enter list elements: "))
if num in lst:
    print("Exists")
else:
    print("Dead")
'''
#77.  Write a program to check if the last element in a list is even. (e.g., l = [1, 2, 4])
'''
l = eval(input("Enter elements: "))
if l[-1] % 2 == 0:
    print("element is even")
else:
    print("element is not even")
'''
#78.Allow withdrawal only if the balance is sufficient. balance = 10000 withdraw = 3000
'''
balance = int(input("Balance: "))
withdraw = int(input("Withdraw amount: "))
if balance > withdraw:
    print("Allow")
else:
    print("Gareeb!!!")
'''
#79.Login only if the username and password are correct. username = "admin" password = "1234"
'''
username = input("Username: ")
pwd = input("Password: ")
if username == "admin" and pwd == '1234':
    print("Correct")
else:
    print("Wrong")
'''
#80.Verify the entered OTP. otp = 4567 entered = 4567
'''
otp = int(input("Enter OTP: "))
if otp == 4567:
    print("Same as entered OTP.")
else:
    print("Wrong OTP")
'''
#81.Book a ticket only if seats are available. seats=15
'''
seat = int(input("Enter seats: "))
if seat > 0:
    print("Seats are available")
else:
    print("Seats are not available")
'''
#82.Allow an A-rated movie only for adults. age=20
'''
age = int(input("Enter the age: "))
if age >= 18:
    print("Allow an A-rated movie")
else:
    print("not allow")
'''
#83.show a message if there is money in the account. balance = 5000
'''
bal = int(input("Enter Balance: "))
if bal > 0:
    print("Hellooooo")
else:
    print("Unsuffient Balance")
'''
#84.Eligible only if salary is above ₹30,000. salary = 45000
'''
sal = int(input("Enter Salary: "))
if sal > 30000:
    print("Eligible")
else:
    print("Not Eligible")
'''
#85.Students with 75% or more attendance can write the exam. attendance = 82
'''
a = int(input("Enter Attendance: "))
if a > 75:
    print("Can Write the exam")
else:
    print("Can not write the exam")
'''
#86.Employees with more than 5 years of experience receive a bonus experience=6
'''
exp = int(input("Enter Experience: "))
if exp > 5:
    print("Receive a bonus")
else:
    print("No bonus")
'''
#87.Customers receive a discount if they spend ₹5,000 or more. bill=6500
'''
bill = int(input("Enter Bill Amount: "))
if bill >= 5000:
    print("Discount Applied")
else:
    print("No discount")
'''
#88. Write a program to check if a credit card number is 16 digits and contains only digits. (e.g., cc = '1234567812345678')
'''
cc = input("Enter Credit Card Number: ")
if len(cc) == 16 and cc.isdigit():
    print("Correct credit card number")
else:
    print("Wrong credit card number")
'''
#89.Write a program to check if a number is divisible by both 3 and 7. (e.g., num = 42)
'''
num = int(input("Enter number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Lalalala")
else:
    print("nooo")
'''
#90.Write a program to check if the given string is a palindrome. (Take user input)
'''
a = input("Enter string: ")
if a == a[::-1]:
    print("Palindrome!!!")
else:
    print("Not Palindrome")
'''   