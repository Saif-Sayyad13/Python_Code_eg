'''# 39. WAP TO PRINT PYTHON FOR 5 TIMES.
print("--- Question 39 ---")
for _ in range(5):
    print("python")

# 40. WAP TO PRINT N NATURAL NUMBERS.
print("\n--- Question 40 ---")
n = int(input("Enter n for natural numbers: "))
for i in range(1, n + 1):
    print(i, end=" ")
print()

# 41. WAP TO PRINT MULTIPLICATION TABLE FOR N.
print("\n--- Question 41 ---")
n = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 42. WAP TO FIND THE SUM OF N NATURAL NUMBERS.
print("\n--- Question 42 ---")
n = int(input("Enter n to find sum of natural numbers: "))
total_sum = sum(range(1, n + 1))
print("Sum:", total_sum)

# 43. WAP TO FIND THE PRODUCT OF N NATURAL NUMBERS OR FACTORIAL OF A NUMBER.
print("\n--- Question 43 ---")
n = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial/Product:", factorial)

# 44. WAP TO PRINT ALL THE CHARACTERS OF A STRING.
print("\n--- Question 44 ---")
s = input("Enter a string to print its characters: ")
for char in s:
    print(char)

# 45. WAP TO PRINT ALL THE CHARACTERS PRESENT AT EVEN INDEX OF A STRING.
print("\n--- Question 45 ---")
s = input("Enter a string for even indices: ")
for i in range(0, len(s), 2):
    print(f"Index {i}: {s[i]}")

# 46. WAP TO EXTRACT ALL THE LOWERCASE CHARACTERS PRESENT IN A STRING.
print("\n--- Question 46 ---")
s = input("Enter a string to extract lowercase letters: ")
lowercase_chars = [char for char in s if char.islower()]
print("Lowercase characters:", "".join(lowercase_chars))

# 47. WAP TO EXTRACT ALL THE VOWELS PRESENT IN A STRING.
print("\n--- Question 47 ---")
s = input("Enter a string to extract vowels: ")
vowels = "aeiouAEIOU"
extracted_vowels = [char for char in s if char in vowels]
print("Vowels found:", "".join(extracted_vowels))

# 48. WAP TO PRINT FACTORS OF A INTEGER NUMBER.
print("\n--- Question 48 ---")
n = int(input("Enter an integer to find its factors: "))
print(f"Factors of {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 49. WAP TO TOGGLE A STRING.
print("\n--- Question 49 ---")
s = input("Enter a string to toggle case: ")
print("Toggled string:", s.swapcase())

# 50. WAP TO REVERSE THE GIVEN NUMBER.
print("\n--- Question 50 ---")
n = int(input("Enter a number to reverse: "))
reversed_num = int(str(abs(n))[::-1])
if n < 0:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)

# 51. WAP TO FIND THE SUM OF INDIVIDUAL DIGITS OF A NUMBER.
print("\n--- Question 51 ---")
n = int(input("Enter a number to find digit sum: "))
digit_sum = sum(int(digit) for digit in str(abs(n)))
print("Sum of digits:", digit_sum)

# 52. WAP TO CHECK WHETHER THE NUMBER IS PERFECT OR NOT.
print("\n--- Question 52 ---")
n = int(input("Enter a number to check if it's Perfect: "))
divisors_sum = sum(i for i in range(1, n) if n % i == 0)
if divisors_sum == n and n > 0:
    print(f"{n} is a Perfect Number.")
else:
    print(f"{n} is NOT a Perfect Number.")

# 53. WAP TO LOGIN TO PHONEPE BY ENTERING CORRECT OTP.
print("\n--- Question 53 ---")
correct_otp = "1234"
attempts = 3
while attempts > 0:
    user_otp = input("Enter 4-digit PhonePe OTP: ")
    if user_otp == correct_otp:
        print("Login Successful to PhonePe!")
        break
    else:
        attempts -= 1
        print(f"Incorrect OTP. Remaining attempts: {attempts}")
else:
    print("Account locked due to too many failed attempts.")

# 54. WAP TO RUN INFINITE LOOP UNTIL USER ENTERS THE CORRECT PASSWORD.
print("\n--- Question 54 ---")
correct_password = "secure_pass123"
while True:
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Access Granted!")
        break
    print("Wrong password! Try again.")

# 55. WAP TO EXTRACT ALL THE EVEN INTEGERS PRESENT IN A TUPLE AT ODD INDEX.
print("\n--- Question 55 ---")
tup = (10, 22, 33, 44, 55, 60, 77, 88)
result = []
for i in range(1, len(tup), 2):
    if tup[i] % 2 == 0:
        result.append(tup[i])
print("Even integers at odd indices:", result)

# 56. WAP TO REMOVE DUPLICATES FROM A LIST WITHOUT CONVERTING INTO SET.
print("\n--- Question 56 ---")
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)

# 57. WAP TO FIND THE SUM OF ALL THE ODD NUMBERS BETWEEN THE GIVEN RANGE.
print("\n--- Question 57 ---")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
odd_sum = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        odd_sum += num
print(f"Sum of odd numbers between {start} and {end}: {odd_sum}")

# 58. WAP TO FIND THE GREATEST NUMBER IN A GIVEN LIST OF INTEGERS.
print("\n--- Question 58 ---")
numbers = [3, 7, 2, 9, 5]
greatest = numbers[0]
for num in numbers:
    if num > greatest:
        greatest = num
print("The greatest number is:", greatest)

# 59. WAP TO FIND THE SUM OF CUBE OF A NUMBER IN A STRING.
print("\n--- Question 59 ---")
s = input("Enter a string with digits: ")
cube_sum = 0
for char in s:
    if char.isdigit():
        cube_sum += int(char) ** 3
print("Sum of cubes of numbers in the string:", cube_sum)

# 60. WAP TO CHECK WHETHER THE NUMBER IS ARMSTRONG OR NOT.
print("\n--- Question 60 ---")
n = int(input("Enter a number to check if it's Armstrong: "))
num_str = str(n)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
if armstrong_sum == n:
    print(f"{n} is an Armstrong Number.")
else:
    print(f"{n} is NOT an Armstrong Number.")
'''
