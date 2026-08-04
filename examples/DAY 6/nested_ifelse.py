'''# wap to check wheteher the given number is even and greater than 5
num=eval(input('Enter the number:  '))
if num%2==0:
    print(f'the given number is {num} even')
    
    if num>5:
        print(f'the given number {num} is greater')
        
    else:
        print(f" the given number {num} is less")
else:
    print(f' the given number{num} is odd')
    '''

'''#wap to check the no is odd  and check if the number is divisible by 7
n=eval(input('enter the number'))
if n%2==1:
    print(f' the given number{n} is even')
    
    if n%7==0:
        print(f' the number {n } is divisible by 7')
        
    else:
        print( ' the number is not divisible:')
        
else:
    print(f' the given number {n} is even')'''
    
'''# wap  to validate  facebook username and password condition is "python" and password="python master"

FB_username=eval(input('enter the username'))
if FB_username=="python":
    print('username is valid')
    
    Password=eval(input('enter the password'))
    
    if Password=="python master":
        print('Password is valid')
    else:
        print('passwords is invalid')
        
else:
    print('username is invalid')'''
  

'''#wap  to perform  list operation user should enter only list data type,
#if option1 pop().option2 sort().optiion3 clear() invalid operation data type

data=eval(input('enter the data type'))
if isinstance(data,list):
    print('yes we are passing only list  data type')
    
    Option=eval(input('enter the option(1,2,3)'))
    
    if Option==1:
        print(data.pop())
    elif Option==2:
        data.sort()
        print(data)
    elif Option==3:
        data.clear()
        print(data)
    else:
        print('Invalid Option')
else:
    print('invalid data type')'''
    

'''#wap  to perform  string operation user should enter only string data type,
#if option1 upper().option2 lower().optiion3 swapcase() oprtyion4 Capitization() invalid operation data type

data=eval(input('entter the string'))
if isinstance(data,str):
    print('yes the neter data is string')
    
    option=eval(input('enter the option(1,2,3,4)'))
    
    if option== 1:
        print(data.upper())
    elif option==2:
        print(data.lower())
        
    elif option==3:
        print(data.swapcase())
        
    elif option==4:
        print(data.capitalize())
    else:
        print('invalid option')
else:
    print('invalid data type ')'''
    
#

'''
#wap to check the theater name, movie name, ticket price and seat number using nested if else
theater=["PVR", "INOX", "CINEMAX", "CINEPOLIS"]
user=eval(input('enter the theater name:  '))
if user in theater:
    print(f'user is selected  {user} therater name')
    
    movies=["RRR", "KGF", "PUSHPA", "AVATAR"]
    user1=eval(input('enter the movie name:  '))
    if user1 in movies:
        print(f'user is selected {user1} movie name')
        
        ticket_prive=[200, 300, 400, 500]
        user2=eval(input('enter the ticket_price:  '))
        if user2 in ticket_prive:
            print(f'user is selected {user2} ticket price')
            
            seats=["A1", "A2", "A3", "A4"]
            user3=eval(input('enter the seat number:  '))
            if user3 in seats:
                print(f'user is selected {user3} seat number')
                
                print('booking is confirmed')
            else:
                print('invalid seat number')
        else:
            print('invalid timing')
    else:
        print('invalid movie name')
else:
    print('invalid theater name')'''
    
    
'''# 7.wap to purchase a phone from the shopping app apps=[“flipkart”,”amazon”]
#categories=[“electronics”,”mobile”,”fashion”,”furnitures”]

apps=["flipkart","amazon"]
user=eval(input('enter the app name:  '))
if user in apps:
    print(f'user is selected {user} app name')
    
    categories=["electronics","mobile","fashion","furnitures"]
    user1=eval(input('enter the category name:  '))
    if user1 in categories:
        print(f'user is selected {user1} category name')
        
        mobile_brands=["samsung","apple","oneplus","vivo"]
        user2=eval(input('enter the mobile brand name:  '))
        if user2 in mobile_brands:
            print(f'user is selected {user2} mobile brand name')
            
            price=[20000,30000,40000,50000]
            user3=eval(input('enter the price:  '))
            if user3 in price:
                print(f'user is selected {user3} price')
                
                print('purchase is confirmed')
            else:
                print('invalid price')
        else:
            print('invalid mobile brand name')
    else:
        print('invalid category name')
else:
    print('invalid app name')
    '''
    
    
'''
#8.wap to give 10% off only who is purchasing in credit card and min 3 product
# should purchase and each product price should be more than 500

products=["product1","product2","product3","product4","product5"]
user=eval(input('enter the product name:  '))
if user in products:
    print(f'user is selected {user} product name')
    
    payment_method=["credit card","debit card","net banking"]
    user1=eval(input('enter the payment method:  '))
    if user1=="credit card":
        print(f'user is selected {user1} payment method')
        
        quantity=eval(input('enter the quantity:  '))
        if quantity>=3:
            print(f'user is selected {quantity} quantity')
            
            price=eval(input('enter the price:  '))
            if price>500:
                print(f'user is selected {price} price')
                
                discount=price*0.1
                final_price=price-discount
                print(f'final price after 10% discount is: {final_price}')
            else:
                print('price should be more than 500')
        else:
            print('quantity should be more than 3')
    else:
        print('payment method should be credit card')
else:
    print('invalid product name')'''
    


'''
#6.wap to find middle element is even or odd s=[3,4,6,7,9,1,5]
s=[3,4,6,7,9,1,5]
middle_element=s[len(s)//2]
if middle_element%2==0:
    print(f'the middle element {middle_element} is even')
else:
    print(f'the middle element {middle_element} is odd')
'''