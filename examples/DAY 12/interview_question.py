'''
anagram : character should be same but it has different meaning
anagram means a word or phrase formed by rearranging the letters of another,
such as "listen" and "silent".
like tea-----eat
bat-----tab
cat-----act

'''


'''a='tea'
b='eat'
#print(sorted(a))
print(sorted(a,reverse=True))
print(sorted(b))
if sorted(a)==sorted(b):
    print('anagram')
else:
    print('not anagram')'''
    
'''
#Armstrong number 
means the no which is given the square or cude wil sum will be same as the number 
if we use 2 number then its squre
if we use 3 number do cude
if we use 4 4**4




a=153
total=0
b=str(a)    #-----153-----'153'
#print(b) #-------iterable
power=len(b)
#print(power)  # 3 -----'153'-------len will be 3
for i in b:    #-----i---'1'------'5'------'3'
    total=total+int(i)**power    #-------power-----3
    #---0  =   +1
if total==a:
    print("its a Armstrong number")
else:
    print('its not')
   '''
   
   
'''
Tables like 1*1=1
         


for i in range(1,11):
    for j in range(2,11):
        print(i*j,end=" ")
    print()
#---------------OR
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} *{j}-----{i*j}")
    print()
        '''
        
        
'''a="Good Day"

for i in range(len(a)):
    print(i+3,a[i])
print()

# -------OR----

for i in enumerate(a,start=3):
    print(i)
    '''
"""
for varable in enumerate(iterable,start=number)
    statement
    
"""

'''
#1.WAP to return a dictionary with word & its len pair
#from a string
string = 'hello good morning how are youu'
#exp o/p : {hello:5, guys:4, morning:7, how:3, are:3, you:4}


s = 'hello good morning how are youu'
d={}
for i in s.split():
    d.update({i:len(i)})  #----------- with using inbuild
print(d)
print()

#---------OR-----
s = 'hello good morning how are youu'
d={}
for i in s.split():
    d[i]=len(i) #---------without using in build
print(d)
print()
    '''
    
"""
2.WAP to count number of vowels present in given string
s = 'GooD mOrnIng'   
count=0
for i in s:
    if i in "aeiouAEIOU":
        count=count+1
print("total count of vowel in given str is :", count)"""


"""
3.WAP to get below o/p:
s = 'Hi how are you'
#exp o/p : 'iH woh era uoy'


s = 'Hi how are you'
res=" "
for i in s.split():
    res=res+" "+i[::-1]
print(res)
"""

"""
4.WAP to print all the digits in a below list
l = ['hello', '123', 'hai', 'python', '345']

for item in l:
    if item.isdigit():
        print(item)

"""

"""
5.WAP to check whether string is ANAGRAM or not

#anagrams : characters should be same it can different meaning
#tea, eat
#silent, listen
#bored , robed
#cat, act
#keep, peek
#lamp, palm
# List of anagram pairs to test
pairs = [
    ('tea', 'eat'),
    ('silent', 'listen'),
    ('bored', 'robed'),
    ('cat', 'act'),
    ('keep', 'peek'),
    ('lamp', 'palm')
]

# Loop through each pair and check
for a, b in pairs:
    if sorted(a) == sorted(b):
        print(f"'{a}' and '{b}' -> anagram")
    else:
        print(f"'{a}' and '{b}' -> not anagram")

"""

"""
#6.Find the sum of even numbers from 1 to 20
total_sum = 0

for i in range(1, 21):
    if i % 2 == 0:
        total_sum += i

print(total_sum)

"""
'''
#7.Count numbers divisible by 3 from 1 to 50count = 0

for i in range(1, 51):
    if i % 3 == 0:
        count += 1

print(count)
'''


'''#8.Replace negative numbers with 0
num= [10, -5, 20, -3, 40]
for i in range(len(num)):
    if num[i]<0:
        num[i]=0
print(num)'''

'''
#9.Print position of each character

word = "PYTHON"
for i in range(len(word)):
    print(i + 1, word[i])
'''

'''#10.Count even and odd numbers in a list.
num= [10, 15, 22, 31, 40, 51]

even_count = 0
odd_count = 0

for x in num:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)'''


'''#11.wap to print repeated char and count the same
s="helloworld"
processed = ""

for char in s:
    if char not in processed:
        count = s.count(char)
        if count > 1:
            print(f"Character '{char}' is repeated {count} times")
        processed += char

'''


'''#12.Grouping flowers and animals separately
items=["lotus-flower","lilly-flower","cat-animal","dog-animal","sunflower-flower"]
flowers = []
animals = []

for item in items:
    if "flower" in item:
        flowers.append(item)
    elif "animal" in item:
        animals.append(item)

print("Flowers:", flowers)
print("Animals:", animals)
'''

'''#13.filter only character except digits
s="Think456 and 123answers it789 guys "
result = ""
for char in s:
    if not char.isdigit():
        result += char

print(result)
'''
'''
#14.replace whitespaces with newline char in the below string
s="hello world welcome to python"
s = "hello world welcome to python"

result = s.replace(" ", "\n")
print(result)
'''


'''
#15.replace all vowels with *
s="hello world welcome to python"
s = "hello world welcome to python"
vowels = "aeiouAEIOU"
result = ""

for char in s:
    if char in vowels:
        result += "*"
    else:
        result += char

print(result)



'''