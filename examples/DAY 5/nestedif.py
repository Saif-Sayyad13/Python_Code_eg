'''# nested if stnt:
# A if stnt inside another if stnt is know as nested if stnt:

# wap to check whether the middle value in a list is str or not
ls=eval(input('Enter the list:'))
if len(ls)%2==1:
    if type(ls[len(ls)//2])==str:
        print("The middle is string")
    else:
        print('The middle value is not string')
else:
    print('The length is even and no middle value')'''
    
'''#wap to check whether the character is vowel or not
ch=input('enter the chr:')
if ch.isalpha():
    if ch in 'AEIOUaeiou':
        print(ch,'  is a vowel')
    else:
        print(ch,'    is a consonant ')
else:
    print(ch,'   chr is not alphabet')'''
    
'''# wap to check whether the last value in a list is palindrome or not and start with vowel or not
ls=eval(input('enter a list data:'))
if ls [-1]==ls[-1][::-1]:
    if ls[-1][0] in 'AEIOUaeiou':
        print(ls[-1],'--> is a palindrome and start with vowel..')
    else:
       print(ls[-1],'--> is a palindrome and start with consonant..')
else:
    print('last value / element is not a plindrome') '''
    
'''# wap to check instagram login 
correctusename="aman"
correctpassword='aman@123'
user_name=input('Enter the username')
password=input('Enter the password')
if correctusename==user_name:
    if correctpassword==password:
        print('login successful')
    else:
        print('invalid password ')
else:
    print('user not found')
    
    '''

''''''
'''#wap to check greatest of 4 number
a=int(input('Enter the first number'))
b=int(input('Enter the second number'))
c=int(input('Enter the third number'))
d=int(input('Enter the fourth number'))
if a>b:
    if a>c:
        if a>d:
            print(a,'is the greatest number')
        else:
            print(d,'is the greatest number')
    else:
        if c>d:
            print(c,'is the greatest number')
        else:
            print(d,'is the greatest number')
else:
    if b>c:
        if b>d:
            print(b,'is the greatest number')
        else:
            print(d,'is the greatest number')
    else:
        if c>d:
            print(c,'is the greatest number')
        else:
            print(d,'is the greatest number')'''
      
 '''           
# wap pop append clear 
ls=eval(input('Enter the list data :'))
if  type(ls)==list:
    print('1--pop()')
    print('2--append()')
    print('3--clear()')
    
    choice=eval(input('Enter your choice:'))
    if choice==1:
        ls.pop()
        print(ls)
    else:
        if choice==2:
            data=eval(input('enter the data'))
            ls.append(data)
            print(ls)
        else:
            if choice==3:
                ls.clear()
                print(ls)
            else:
                print('invalid choice')
else:
    print('invalid data type')'''
    
