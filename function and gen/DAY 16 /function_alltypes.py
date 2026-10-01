"""
def aman1(a,b,c):
    print(a,b,c)
aman1(1,2,3)
print()

def aman2(a,b,c):
    print(a,b,c)
aman2(a=1,b=2,c=3)
print()

def aman3(a,b,/,c):
    print(a,b,c)
aman3(1,2,c=3)
print()

def aman4(a,b,*,c):
    print(a,b,c)
aman4(1,2,c=3)
print()

def aman5(a,b,/,*,c):
    print(a,b,c)
aman5(1,2,c=3)
print()

def aman6(*args):
    print(args)
aman6(1,2,3)
print()

def aman7(**kwarge):
    print(kwarge)
aman7(a=1,b=2,c=3)
print()

def aman8(*args, **kwargs):
    print(args,kwargs)
aman8(1,2,c=3)
print()"""














'''
# ==================== 3 ARGUMENT EXAMPLES ====================

# 1. Positional argument
def aman1(a, b, c):
    print(a, b, c)
aman1(1, 2, 3)
print()

# 2. Keyword arguments
def aman2(a, b, c):
    print(a, b, c)
aman2(a=1, b=2, c=3)
print()

# 3. Only Positional argument (/)
def aman3(a, b, c, /):
    print(a, b, c)
aman3(1, 2, 3)
print()

# 4. Only keyword arguments (*)
def aman4(*, a, b, c):
    print(a, b, c)
aman4(a=1, b=2, c=3)
print()

# 5. Variable Positional arguments (*args)
def aman5(*args):
    print(args)
aman5(1, 2, 3)
print()

# 6. Variable keyword arguments (**kwargs)
def aman6(**kwargs):
    print(kwargs)
aman6(a=1, b=2, c=3)
print()

# 7. Combination of only Positional and only keyword arguments
def aman7(a, b, /, *, c):
    print(a, b, c)
aman7(1, 2, c=3)
print()

# 8. Combination of *args and **kwargs
def aman8(*args, **kwargs):
    print(args, kwargs)
aman8(1, 2, c=3)
print()


# ==================== 5 ARGUMENT EXAMPLES ====================

# 1. Positional argument
def aman9(a, b, c, d, e):
    print(a, b, c, d, e)
aman9(1, 2, 3, 4, 5)
print()

# 2. Keyword arguments
def aman10(a, b, c, d, e):
    print(a, b, c, d, e)
aman10(a=1, b=2, c=3, d=4, e=5)
print()

# 3. Only Positional argument (/)
def aman11(a, b, c, d, e, /):
    print(a, b, c, d, e)
aman11(1, 2, 3, 4, 5)
print()

# 4. Only keyword arguments (*)
def aman12(*, a, b, c, d, e):
    print(a, b, c, d, e)
aman12(a=1, b=2, c=3, d=4, e=5)
print()

# 5. Variable Positional arguments (*args)
def aman13(*args):
    print(args)
aman13(1, 2, 3, 4, 5)
print()

# 6. Variable keyword arguments (**kwargs)
def aman14(**kwargs):
    print(kwargs)
aman14(a=1, b=2, c=3, d=4, e=5)
print()

# 7. Combination of only Positional and only keyword arguments
def aman15(a, b, c, /, *, d, e):
    print(a, b, c, d, e)
aman15(1, 2, 3, d=4, e=5)
print()

# 8. Combination of *args and **kwargs
def aman16(*args, **kwargs):
    print(args, kwargs)
aman16(1, 2, 3, d=4, e=5)
print()
'''
# =====================================================================
# Python Function Argument Types: 3 & 5 Argument Examples
# =====================================================================

# --- 1. Positional Arguments ---
def positional_3(first, middle, last):
    print("1. Positional (3):", first, middle, last)

def positional_5(a, b, c, d, e):
    print("1. Positional (5):", a + b + c + d + e)


# --- 2. Keyword Arguments ---
def keyword_3(name, age, city):
    print(f"2. Keyword (3): {name} is {age} from {city}")

def keyword_5(brand, model, year, color, price):
    print(f"2. Keyword (5): {year} {brand} {model}, {color}, ${price}")


# --- 3. Only Positional Arguments (/) ---
def only_positional_3(a, b, c, /):
    print("3. Only Positional (3):", a, b, c)

def only_positional_5(a, b, c, d, e, /):
    print("3. Only Positional (5):", a, b, c, d, e)


# --- 4. Only Keyword Arguments (*) ---
def only_keyword_3(*, theme, font, size):
    print(f"4. Only Keyword (3): {theme}, {font}, {size}")

def only_keyword_5(*, id, role, status, email, phone):
    print(f"4. Only Keyword (5): ID {id}, {role}, {status}, {email}, {phone}")


# --- 5. Variable Positional Arguments (*args) ---
def variable_positional_3(*args):
    print("5. Variable Positional (3): Tuple is", args)

def variable_positional_5(*args):
    print("5. Variable Positional (5): Tuple is", args)


# --- 6. Variable Keyword Arguments (**kwargs) ---
def variable_keyword_3(**kwargs):
    print("6. Variable Keyword (3): Dict is", kwargs)

def variable_keyword_5(**kwargs):
    print("6. Variable Keyword (5): Dict is", kwargs)


# --- 7. Combination of Only Positional and Only Keyword Arguments ---
def combo_positional_keyword_3(a, b, /, *, c):
    print(f"7. Combo Only Pos / Only Kw (3): Positional=({a}, {b}), Keyword={c}")

def combo_positional_keyword_5(a, b, c, /, *, d, e):
    print(f"7. Combo Only Pos / Only Kw (5): Positional=({a}, {b}, {c}), Keyword=({d}, {e})")


# --- 8. Combination of *args and **kwargs ---
def master_combo_3(*args, **kwargs):
    print(f"8. Combination *args / **kwargs (3): args={args}, kwargs={kwargs}")

def master_combo_5(*args, **kwargs):
    print(f"8. Combination *args / **kwargs (5): args={args}, kwargs={kwargs}")


# =====================================================================
# Executing and Testing the Arguments
# =====================================================================

print("--- Testing 3-Argument Implementations ---")
positional_3("John", "Robert", "Smith")
keyword_3(city="Chicago", name="Alice", age=30)
only_positional_3(5, 10, 15)
only_keyword_3(theme="Dark", font="Arial", size=14)
variable_positional_3(10, 20, 30)
variable_keyword_3(item1="Pen", item2="Book", item3="Bag")
combo_positional_keyword_3(1, 2, c=3)
master_combo_3("X", "Y", status="Success")

print("\n--- Testing 5-Argument Implementations ---")
positional_5(10, 20, 30, 40, 50)
keyword_5(color="Red", price=25000, model="Civic", brand="Honda", year=2024)
only_positional_5(1, 2, 3, 4, 5)
user_5_data = {"id": 101, "role": "Admin", "status": "Active", "email": "a@b.com", "phone": "123"}
only_keyword_5(**user_5_data) # Alternative clean way to pass 5 keywords unpacking a dict
variable_positional_5('Apple', 'Banana', 'Cherry', 'Date', 'Elderberry')
variable_keyword_5(Math=95, Science=90, English=88, History=85, Art=92)
combo_positional_keyword_5(10, 20, 30, d=40, e=50)
master_combo_5(1, 2, 3, color="Blue", visible=True)
