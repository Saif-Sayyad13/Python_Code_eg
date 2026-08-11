"""
1.break-- when the condition is true it will break the loop and exit from the loop
2.continue-- when the condition is true it will skip the current iteration and move to the next iteration
3.pass -- it is a null statement, it does nothing when executedn
all of this three are keywords
if we wan tot skip current iteration and move to the next iteration then we can use continue keyword
all three called transfer of control statements  
   
"""
'''x=[1,2,3,4,5,6,7,8,9]
for i in x:
    if i in x:
        if i==4:
            break
            
    print(i)

print()

b="Good Morning"
stop="d"
for i in b:
    if i==stop:
        break
    print(i)
   
#wap to print only negative number 
s=[1,12,-3,90,-4,-5,900,-12]
for i in s:
    if i>0:
        continue
    print(i)'''
    
'''
s='python class'
stop='n'
for i in s:
    if i==stop:
        continue
    print(i,end="")
    
print()

for i in s:
    if i==stop:
        break
    print(i,end="") 
print()'''

"""s="Hello" # if you want to hold that block we ca use pass or ...
for i in s: # if you for loop and you want to do nothing in the loop then you can use pass keyword
    pass    """ #in the part of pass use three dots(...) to indicate that the code is intentionally
#left blank. It is used as a placeholder for future code or to create minimal classes or functions.

