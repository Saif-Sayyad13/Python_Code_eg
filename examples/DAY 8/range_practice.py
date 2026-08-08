'''Practice Questions

1. Print each character of a string
a="Tree Notes"

2.Print vowels only
s = "education"

3.Count uppercase letters
s = "PyTHon"

4.Print digits from string
s = "ab12cd34"

5.Sum of list elements
x=[25,70,90,100]

6.Print even numbers from list
e=[23,45,66,78,90]

7.Print negative numbers
l = [4,-2,7,-9,3]

8.Count odd numbers
l = [1,2,3,4,5,6,7]

9.Print odd numbers 1 to 20

10.wap Sum from 1 to 50

11.wap Print numbers divisible by 5 (1 to 51)

12.Reverse 10 to 1

13.Squares from 1 to 10

14.Print ASCII values of characters
s='ABC'

15.wap to Count consonants
s = "education"

16.Print numbers greater than 50
l = [23,67,12,89,54]

17.Count positive numbers
l = [-1,4,-3,7,9]

18.wap to Separate even/odd
e=[1,2,3,4,5,6,7,8]

19.Sum of even numbers
e=[1,2,3,4,5,6,7,8]


20.wap to print the number form 1 -20 segregate even and odd number into list

21.wap to extract vowels and digits in a string
s="hello123"


22.wap to capitalize only the first letter of every word in the given list
l=["vaidegi","rahul","shivam","kapil","patil"]


23.wap to extract only individual data types form the list
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]


24.wap to extract only individual data types from the list and sum all the individual data types
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]


25.wap to print the count of alphabets and numbers and space in the given string
s="india got the independence in the year 1947"

 
'''
'''#1. Print each character of a string a="Tree Notes"
a="Tree Notes"
for i in a:
    print(i,end=" ")'''
    
'''#2.Print vowels only
s = "education"
for i in s:
    if i in"aeiouAEIOU":
        print(i,end=" ")'''
        
'''#3.Count uppercase letters
s = "PyTHon"
count=0
for i in s:
    if i.isupper():
        count=count+1
print(count,end=" ")
    '''
#4.Print digits from string
s = "ab12cd34"