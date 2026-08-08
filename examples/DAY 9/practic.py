'''
30.wap to create a dictionary with element and its count pair

l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
output:-->
{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}


31.wap to find the length of the string without using inbuilt function
s="Never Give Up"

33.wap to reverse a string without using inbuilt function
x="you did it guys"

33.wap to print alternative character from a given string
s="hello python"



34.wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}


35.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"

o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}




36.wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

37.wap to create a dictionary Ascii and character pair
l=[89,51,111,77,108,120]

o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}

38.wap to  create a list of characters and its Ascii value pair
s="sunday"
o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)

'''


'''#30
l = ["yellow", "red", "black", "pink", "orange", "green", "red", "pink", "yellow"]

d = {}

for x in l:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

print(d)

#32
s = "Never Give Up"

c = 0

for x in s:
    c = c + 1

print(c)

#32
x = "you did it guys"

r = ""

for i in x:
    r = i + r

print(r)

#33
s = "hello python"

for i in range(0, len(s), 2):
    print(s[i], end="")
 
#34   
s = "tomorrow is weekend and non-veg special"

l = s.split()
d = {}

i = 0

for x in l:
    d[i] = x
    i = i + 1

print(d)
#35
s = "tomorrow is weekend and non-veg special"

l = s.split()
d = {}

for x in l:
    c = 0

    for y in x:
        c = c + 1

    d[x] = c

print(d)
#36
s = "sunday"

d = {}

for x in s:
    d[x] = x.upper()

print(d)
#37
l = [89, 51, 111, 77, 108, 120]

d = {}

for x in l:
    d[x] = chr(x)

print(d)
#38
s = "sunday"

l = []

for x in s:
    l.append((x, ord(x)))

print(l)'''