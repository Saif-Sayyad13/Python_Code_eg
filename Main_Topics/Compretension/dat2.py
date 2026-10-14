'''for i in range(1,4):
    for j in range(1,4):
        print(i,j,end=" ")

print([(i,j) for i in range(1,4) for j in range(1,4)])
'''

'''a=[[10,20],[30,40],[50,60]]
#output=[10,20,30,40,50,60]
print([j for i in a for j in i])
for i in a:
    for j in i:
        print(j,end="")
        
#output=30,70,110
print([sum(i) for i in a])
for i in a:
    print(sum(i),end=" ")
    '''
    
'''
z=[10,5,25,30,40,15,20]
print([i+j for i in z for j in z if i+j==30])
for i in z:
    for j in z:
        if i+j==30:
            print(i,j,end=" ")'''
            
'''a=[100,200,350,450]
#output=[1000,900,750,650]
print([sum(a)-i for i in a])
for i in a:
    print(sum(a)-i,end=" ")'''