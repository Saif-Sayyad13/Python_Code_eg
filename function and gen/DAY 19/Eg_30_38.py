
# 29.wap to check the given characters is
# alphabets or digit or special characters
x = input("Enter character: ")

if x.isalpha():
    print("Alphabet")
elif x.isdigit():
    print("Digit")
else:
    print("Special Character")


# 30.wap to check given iterable is a sequence,
# if it is a sequence reverse it,if 
# not add one extra element to the iterable
def check_item(item):
    # Check if it is a string, list, or tuple
    if isinstance(item, (str, list, tuple)):
        ans = item[::-1]
        print("Reversed:", ans)
    else:
        print("Not a sequence. Adding item...")
        if isinstance(item, set):
            item.add("new")
        elif isinstance(item, dict):
            item["key"] = "value"
        print("Updated:", item)

# Example
check_item([1, 2, 3])


# 31.write a function to print the below output
# func("TRACXN",1)
#should print RCN
def func(text, start):
    # Slice from start index to the end, skipping every 2nd letter
    return text[start::2]

print(func("TRACXN", 1))  # Output: RCN
print(func("TRACXN", 0))  # Output: TAX

#
# 32.write a function to print the below output
# func("TRACXN",0)
#should print TAX
def check_count(*args):
    total = len(args)
    if total > 5:
        print("More than 5 arguments. Total is:", total)
    else:
        print("5 or less arguments. Total is:", total)

check_count(1, 2, 3, 4, 5, 6)


# 33.A function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5.
def make_dict(text):
    out = {}
    for ch in text:
        out[ch] = ord(ch)
    return out

print(make_dict("ABC"))  # Output: {'A': 65, 'B': 66, 'C': 67}




# 34.waf to return a dictionary with characters and ascii value pair
def rev_data(data):
    if isinstance(data, (str, list, tuple)):
        return data[::-1]
    else:
        print("Type is:", type(data))

# Example
rev_data({1, 2, 3})


# 35.waf to reverse a iterable if you are passing string or list or tuple else print type of the data
ch = input("Enter character: ")

if len(ch) == 1:
    num = ord(ch)
    # A-Z or a-z
    if (65 <= num <= 90) or (97 <= num <= 122):
        print("Alphabet")
    # 0-9
    elif 48 <= num <= 57:
        print("Digit")
    else:
        print("Special Character")

# 36.wap to check if a given character is alphabet or digit or special character (without using inbuilt function).
#
ch = input("Enter character: ")

if len(ch) == 1:
    num = ord(ch)
    # A-Z or a-z
    if (65 <= num <= 90) or (97 <= num <= 122):
        print("Alphabet")
    # 0-9
    elif 48 <= num <= 57:
        print("Digit")
    else:
        print("Special Character")


# 37.wap to return length of an iterable without using len() function
def get_size(data):
    count = 0
    for item in data:
        count = count + 1
    return count

print(get_size("hello"))  # Output: 5

# 38.wap to count the number of arguments passed inside the function call(both positional and keyword)

def count_args(*args, **kwargs):
    p_count = len(args)   # Positional count
    k_count = len(kwargs) # Keyword count
    total = p_count + k_count
    
    print("Total arguments:", total)

count_args(1, 2, a=10, b=20)  # Output: Total arguments: 4
