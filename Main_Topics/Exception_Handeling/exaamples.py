'''#1.Write a program that accepts two numbers and performs division.
# Handle ZeroDivisionError if the second number is 0. 
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print(f"Result of division: {result}")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")



#2.Ask the user to enter an integer. Handle ValueError if the user
# enters text instead of a number. 
try:
    user_num = int(input("Please enter an integer: "))
    print(f"Successfully entered integer: {user_num}")
    
except ValueError:
    print("Error: Invalid input! You must enter a valid integer text.")



#3.numbers = [10, 20, 30, 40, 50]
#Ask the user for an index and print the value. Handle IndexError.
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter a list index to fetch (0 to 4): "))
    print(f"Value at index {index} is: {numbers[index]}")
    
except IndexError:
    print(f"Error: Index out of range! Please choose a number between -5 and 4.")
except ValueError:
    print("Error: Index must be an integer.")


#4.student = {"name": "Rahul", "age": 22, "course": "Python"}
#Ask the user for a key and print its value. Handle KeyError.
student = {"name": "Rahul", "age": 22, "course": "Python"}

try:
    key = input("Enter a student property to look up (e.g., name, age, course): ")
    print(f"The value for '{key}' is: {student[key]}")
    
except KeyError:
    print(f"Error: The key '{key}' does not exist in the student dictionary.")

#5.Write a program that accepts two inputs and performs division. Handle both ValueError and ZeroDivisionError. 
try:
    val1 = input("Enter numerator: ")
    val2 = input("Enter denominator: ")
    
    # Converts inputs to floats (might trigger ValueError)
    num1 = float(val1)
    num2 = float(val2)
    
    # Divides inputs (might trigger ZeroDivisionError)
    result = num1 / num2
    print(f"Result: {result}")
    
except ValueError:
    print("Error: One or both inputs are not valid numbers.")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

#6.Write a program that converts "abc" into an integer.and display the exception message.
try:
    text = "abc"
    number = int(text)
    
except ValueError as error_message:
    print(f"Caught Exception: {error_message}")

#7.Write a program to open data.txt and read its contents. Handle FileNotFoundError.Use finally to display: File operation completed
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()
    
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
    
finally:
    print("File operation completed")

#8.Create a login program.
#username = "admin"
#password = "python123"
#Ask the user for username and password.Handle invalid input and use finally to print:
#Login process completed
CORRECT_USER = "admin"
CORRECT_PASS = "python123"

try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username != CORRECT_USER or password != CORRECT_PASS:
        # Raising a ValueError if credentials do not match
        raise ValueError("Invalid username or password credentials provided.")
    else:
        print("Login successful! Welcome back.")
        
except ValueError as e:
    print(f"Authentication Error: {e}")
    
finally:
    print("Login process completed")

#9.Create a situation where an undefined variable is accessed. Handle NameError. 
try:
    print(mystery_variable)
    
except NameError as e:
    print(f"Error caught: {e}")

#10.Create a situation where a method is called on an object that doesn't support that method. Handle AttributeError.  
try:
    number_variable = 42
    number_variable.upper()
    
except AttributeError as e:
    print(f"Error caught: {e}")

'''
