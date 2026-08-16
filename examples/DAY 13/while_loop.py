"""
 While Loop:- A set of instruction block of code which will execute repeatedly until
 the condition is satisified   

Syntax:-
intilization
while <condition>:
    S.B/logics
        updation
    
    
    
if we skip updation it will go in infinite loop  
    
"""
'''
#WAP to print 'Idli vada ' for 5 times
i=0
while i<5:
    print('Idli Vada')
    i+=1.   #-----i=i+1
print()  
#WAP to print number from 1 to 10
i=1
while i<11: #-------i<10:
    print(i,end=' ')
    i+=1
print()
# WAP to print reverse no from 10 to 1
i=10
while i>=1:
    print(i,end=" ")
    i-=1
print()

#WAP to check even no from 1-10
i=1
while i<=10:
    if i%2==0:
        print(i,end=" ")
    i+=1
print()

#WAP to print odd no from 1 to 50
i=50
while i>=1:
    if i%2==1:
        print(i,end=" ")
    i-=1
    '''
   
'''#WAP  to print sum of n natural number 
n=int (input('enter the number: '))
i=1
add=0
while i<=n:
    add=add+i
    i+=1
print(add) #-- we write print outside to get direct answer if we print inside whiel it will show one by one all iteration
'''
'''#WAP to print multiplaction
n=int(input('enter a number : '))
i=1
add=0
while i<=n:
    add=add*i
    i+=1
print(add)'''

'''#WAP to to fetch lower case
st = input('enter a string : ')  # Removed eval()
out = ''
out1 = ''  # Changed to string so we can join digits
out2 = ''

i = 0
while i < len(st):
    if st[i].islower():
        out = out + st[i]
    elif st[i].isupper():
        out2 = out2 + st[i]
    elif st[i].isdigit():
        out1 = out1 + st[i]
    i += 1

print("Lowercase:", out)
print("Digits:", out1)
print("Uppercase:", out2)



'''
'''
#WAP to do addition of int number in given list
A = [10, 4j+9, 'SHR', "DON", 45, 90, 'DI']
total_sum = 0

for x in A:
    if type(x) == int:
        total_sum += x

print(total_sum)

# WAP to fetch str value from a list only if len is>3
items = ["hello", "cat", "python", "java", "c", "html"]

for x in items:
    if type(x) == str and len(x) > 3:
        print(x)

# WAP to do addition of  ASCII value of the special char in a string
st = "hello@123#$&"
sum = 0

for char in st:

    if not char.isalnum():
        sum += ord(char)

print(sum)
'''
