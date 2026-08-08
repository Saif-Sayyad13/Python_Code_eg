"""
'''
normal syntax
    enuerate(iterable)----- inbuild function
    |
    |
    |
    Date will convert to object address
    |
    |
    |
    Object adress data again convert to readable form
               |
               |
               |
    Two ways 1. Type casting        2. looping
              \
              \
               \
        syntax for type casting 
              |
              |
        list(enumerate(iterable))
       tuple(enumerate(iterable)) 
       dict(enumerate(iterable)) 
       set(enumerate(iterable)) 
             |
             |
             | 
       syntax for looping
           | 
           |
           |
        for varable in enumerate(iterable)
            statemnet 
              \
              \
              \
            output of emerate function ----(position,value)
            
            
            
            
            
            
            
            
'''
s='Hello' # 0---H
print(enumerate)

#way---1 typecasting
print(list(enumerate(s)))
#[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(tuple(enumerate(s)))
#((0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))
print(dict(enumerate(s)))
#{0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
print(set(enumerate(s)))
#{(2, 'l'), (3, 'l'), (4, 'o'), (1, 'e'), (0, 'H')}

#way2----- looping
for i in enumerate(s):
    print(i)
'''      packet output
(0, 'H')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
'''
for i,j in enumerate(s):
    print(i)# print(i,j) to print both position as well as value in unpack formate 
''' unpack output when we use two referance
i---- position    # first on always target to position
j---value   
0
1
2
3
4 

here we use two referance varable
here we get unpack
'''
k=[10,20,30,40,50]
for i in enumerate(k):
    print(i)
a={1:2,2:3,3:4}
for i in enumerate(a):
    print(i)
    """