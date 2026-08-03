'''#2. WAP to check a data is a Sequence / Iterable / Individual data type
a = eval(input("Enter data: "))

if type(a) in [str, list, tuple]:
    print("Sequence Data Type")
elif type(a) in [set, dict]:
    print("Iterable Data Type")
else:
    print("Individual Data Type")
    
#3. WAP if input is string return its length, else if input is list pop element, else if input is tuple reverse else invalid input
a = eval(input("Enter data: "))

if type(a) == str:
    print("Length:", len(a))

elif type(a) == list:
    print("Popped Element:", a.pop())
    print("List:", a)

elif type(a) == tuple:
    print("Reversed Tuple:", a[::-1])

else:
    print("Invalid Input")
    
    
#4. WAP to check age category
age = eval(input("Enter age: "))

if age >= 0 and age <= 17:
    print("Child")

elif age >= 18 and age <= 30:
    print("Adult")

elif age >= 31 and age <= 60:
    print("Men")

elif age >= 61 and age <= 100:
    print("Senior Citizen")

else:
    print("Invalid Age")
#5. WAP to calculate average of 5 subjects and display grade
s1 = eval(input("Enter Subject1 Marks: "))
s2 = eval(input("Enter Subject2 Marks: "))
s3 = eval(input("Enter Subject3 Marks: "))
s4 = eval(input("Enter Subject4 Marks: "))
s5 = eval(input("Enter Subject5 Marks: "))

avg = (s1 + s2 + s3 + s4 + s5) / 5

print("Average =", avg)

if avg >= 90 and avg <= 100:
    print("Distinction")

elif avg >= 75:
    print("First Class")

elif avg >= 60:
    print("Second Class")

elif avg >= 50:
    print("Third Class")

else:
    print("Fail")
#6. WAP to check divisibility by 3 and 5 (Fizz Buzz)
n = eval(input("Enter Number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")

elif n % 3 == 0:
    print("Fizz")

elif n % 5 == 0:
    print("Buzz")

else:
    print("Not Divisible")
#7. WAP to check number of digits
n = abs(eval(input("Enter Number: ")))

if n <= 9:
    print("One Digit")

elif n <= 99:
    print("Two Digit")

elif n <= 999:
    print("Three Digit")

else:
    print("More than Three Digits")
#8. WAP to accept number 1-5 and display word
n = eval(input("Enter Number (1-5): "))

if n == 1:
    print("One")

elif n == 2:
    print("Two")

elif n == 3:
    print("Three")

elif n == 4:
    print("Four")

elif n == 5:
    print("Five")

else:
    print("Invalid Number")
#9. WAP to check uppercase/lowercase/special character
ch = input("Enter Character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
    print("Lowercase:", ch.lower())

elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
    print("Uppercase:", ch.upper())

else:
    print("Special Character")
    print("Previous:", chr(ord(ch)-1))
    print("Given:", ch)
    print("Next:", chr(ord(ch)+1))
10. WAP to check password strength
pwd = input("Enter Password: ")

l = len(pwd)

if l < 6:
    print("Weak Password")

elif l >= 6 and l <= 8:
    print("Medium Password")

elif l >= 9 and l <= 12:
    print("Strong Password")

else:
    print("Very Strong Password")
#11. Create a Login System
uname = input("Enter Username: ")
pwd = input("Enter Password: ")

if uname == "admin":
    if pwd == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User Not Found")
#12. WAP to classify a number
n = eval(input("Enter Number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

elif n < 0:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")

else:
    print("Zero")
#13. WAP for Menu Driven Food Ordering System
print("1. Burger - ₹120")
print("2. Pizza - ₹250")
print("3. Sandwich - ₹80")
print("4. Coffee - ₹50")

n = eval(input("Enter Menu Number: "))

if n == 1:
    print("Burger - ₹120")

elif n == 2:
    print("Pizza - ₹250")

elif n == 3:
    print("Sandwich - ₹80")

elif n == 4:
    print("Coffee - ₹50")

else:
    print("Invalid Menu")
#14. WAP to check Teacher's Mood
per = eval(input("Enter Assignment Percentage: "))

if per == 100:
    print("Teacher is Very Happy")

elif per >= 75:
    print("Teacher is Happy")

elif per >= 50:
    print("Teacher is Angry")

else:
    print("Surprise Test Tomorrow!")
    
#15. WAP to suggest Weekend Plan
money = eval(input("Enter Money: "))
battery = eval(input("Enter Battery Percentage: "))

if money >= 1000 and battery >= 80:
    print("Go on a Trip 🏖️")

elif money >= 500 and battery >= 50:
    print("Watch a Movie 🍿")

elif money >= 200 and battery >= 20:
    print("Go to a Café ☕")

else:
    print("Stay Home and Study Python 🐍")'''