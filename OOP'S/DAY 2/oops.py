'''a=[1,2,3,4,5]
for i in reversed(a):
    print(i,end=" ")
print()
print(a[::-1])
a.reverse()
print(a)
x="man"
print(''.join(reversed(x)))

for i in range(5,-1,-1):
    print(i,end="")
   
print() 
rev=""
for char in x:
    rev=char+rev
print(rev)'''

a=[1,2,3,4,5]
def reverse_array():
    for i in a:
        reversed(i)
        return i
s=reverse_array()
print(s)
