'''import re
a='abaaabbaaababbabaa'
x=re.findall('a',a)
print(x)
x=re.findall('a+',a)
print(x)
x=re.findall('a*',a)
print(x)
x=re.findall('a?',a)
print(x)
x=re.findall('a{2}',a)
print(x)
x=re.findall('a{4}',a)
print(x)'''

'''
import re
a="my oancard mnumber is ABCDE1234K"
d=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
print(d)
d=re.findall(r'\D{5}\d{4}\D{1}',a)
print(d)

b='My addhar number is 1234-5678-9012'
r=re.findall(r'\d{4}  /d{4}  /d{4}',b)
print(r)'''

"""
#1.matches any number between 0-9
a="The cost of the book is Rs.100"


#2.matches only lower case letter and upper case letter
b="hello HOW ARE YOU"



#3.write a program to count the number of white space in a given string
c="HELLO world welcome to python Hi how are you. Hi how are you"



#4.sum all the numbers in the below string
word="PYTHON12nREG567exp2"



#5.matches everything apart from numbers between 0-9
a="The cost of the book is Rs.100"



#6.matches everything apart from "a","b","c","d"
b="abcdefghijklmnop"



#7.matches only numbers
word="@hello12world34welcome!123"



#8.extracting file with extension

s="Downloading http://archive.zip file to download folder python http://hero.py and afternoon.txt and slicing.jpeg"



#9.wap to extract only pincode

s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"




10.wap to print the AADHAR CARD numbers

s="my aadhar number is 1234-4567-8910"




11.wap to print the pan card number

a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"




http://12.How to fetch the protocols
a="https://www.google.com"

o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
o/p--->['https://www.google.com']        (second output)



13.creating acronyms of the file format

file_format=["Graphic Interchange Format",
              "Advanced Audio Coding",
            "HyperText Markup Language",
             "Content Management System",
            "Windows Media,Audio",
            "Comma Separated Values"]

o/p-->GIF,AAC,HTML,CMS,WMA,CSV





14.wap to match email ids

emails=["mailto:test.user@company.gov"mailto:,"test_user@company.edu"mailto:,"123test-T.user@company.in","testing@company"mailto:,"pspider@company.in"]




15.matching phone numbers

phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727","123-345-12","900-938-0987"]




16.replace whitespace with newline characters

s="helloworld welcome to python"




17.replace all digits with **

s="hello 123 mic testing 123 123"

""" 

import re
'''
#13.creating acronyms of the file format

file_format=["Graphic Interchange Format",
              "Advanced Audio Coding",
            "HyperText Markup Language",
             "Content Management System",
            "Windows Media,Audio",
            "Comma Separated Values"]

#o/p-->GIF,AAC,HTML,CMS,WMA,CSV
for i in file_format:
    res=re.findall('[A-Z]',i)
    print("".join(res),end=" ")'''
    
'''
#8.extracting file with extension

s="Downloading http://archive.zip file to download folder python http://hero.py and afternoon.txt and slicing.jpeg"
a=re.findall('[A-Za-z]+\.[a-z]+',s)
print(a)
s="Downloading http://archive*zip file to download folder python http://hero*py and afternoon*txt and slicing*jpeg"
a=re.findall('[A-Za-z]+\*[a-z]+',s)
print(a)'''


'''#16.replace whitespace with newline characters

s="helloworld welcome to python"
a=re.sub(' ','\n',s)
print(a)
'''


'''#17.replace all digits with **

s="hello 123 mic testing 123 123"
a=re.sub('123','**',s)
print(a)'''

'''#12.How to fetch the protocols
a="https://www.google.com"
b=re.findall('[a-z]+',a)
print(b)
b1=re.findall(r'\D+',a)
print(b1)
b2=re.findall(r'.+',a)
print(b2)
#o/p--->['https', 'www', 'google', 'com'] (i want first output like this )
#o/p--->['https://www.google.com']        (second output)
'''

'''#4.sum all the numbers in the below string
word="PYTHON12nREG567exp2"
a=re.findall('[0-9]',word)
print(a)
sum=0
for i in a:
    sum=sum+int(i)
print(sum)'''