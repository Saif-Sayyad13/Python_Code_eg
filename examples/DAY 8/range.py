'''# range()---- start point endpoint step value
for i in range(10):
    print(i,end=" ")

print()
# to include end index
for i in range(10+1):
    print(i ,end=" ")
print()  
    
    
#  wap to print 15 to 31
for i in range(15,31,1):
    print(i,end=" ")
print()
#wap to print 10 to 20 in between even number
for i in range(10,21,2):
    print(i,end=" ")
print()

for i in range(10,21,1):
    if i%2==0:
        print(i,end=" ")
print()      
#wap to print 10 to 1
for i in range(10,0,-1):
    print(i,end=" ")
print()
#wap to 50 to 35
for i in range(50,34,-1):
    print(i,end=' ')
print()
# wap to print position of character in the given string
s='PYTHON'
for i in range(len(s)):
    print(i,s[i])
print()

#
s=['Morining','wallmart','Hello','joy','Part']
for i in range(len(s)):
    print(i,'-----',s[i])
print()

#wap to print sum of the number (0-10)
Totle=0
for i in range(11):
    Totle=Totle+i
print(Totle)'''

'''s="Hello"
x={}
for i in s:
    x[i]=ord(i)  
#   x.update({i:ord(i)})
print(x)'''
'''
#range()-----> startPoint  --->EndPoint --->stepvalue

for i in range(10):
    print(i,end=" ")
print()

#To include endindex
for i in range(10+1):
    print(i,end=" ")
print()

#useing Three Parameters
for i in range(0,10,1):
    print(i,end=" ")
print()


#wap to print 15 to 30
for i in range(15,31,1):
    print(i,end=" ")
print()

#wap to print 10 to 20 in between even number
for i in range(10,21,1):
    if i%2==0:
        print(i,end=" ")
print()
for i in range(10,21,2):
    print(i,end=" ")
'''
'''
#wap to print 10 to 1--->???
for i in range(10,0,-1):
    print(i,end=" ")
'''

'''
#wap to print Position of the Character in the
#given string
s="PYTHON"
print(s[0])

#o/p---->0,1,2,3,4,5
for i in range(len(s)):
    print(i,s[i])   #indexing-----> var_name[Position]

print()
s=["Morning","wallmart","Hello","joy","Part"]
for i in range(len(s)):
    print(i,"------->",s[i])
'''

'''
#wap to print sum of the number(0---->10)
Total=0
for i in range(0,11,1):
    Total=Total+i
print(Total)
'''

'''
s="Hello"
#o/p-------->{H:72,e:Ascii,l:Ascii,0:Acii}
x={}
for i in s:       #var_name[key]=value
    # x[i]=ord(i)   #var_name.update({key:value})
    x.update({i:ord(i)})
print(x)
'''
'''
# 3.Count uppercase letters
s = "PyTHon"
total_character=0
for i in s:
    if i.isupper():
        total_character=total_character+1
print(total_character)
'''

"""
20.wap to print the number form 1 -20 segregate 
even and odd number into list
"""

even=[]
odd=[]
for i in range(1,21,1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


