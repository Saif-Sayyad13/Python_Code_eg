'''
Regular Expression
step1:- import re 


1) match()
new_var=re.match('pattern','source string)
                     |
                     Data should be present left 
                     
                     
2) fullmatch() 
var_name=re.fullmatch('pattern','source_of_string)  

3) search()
new_var=re.search('pattern',var_name)  

4) finditer()
var_name=re.finditer('pattern','source_of_string)
  
5) findall()
var_name=re.findall('pattern','source_of_str')


6) sub()
new_var=re.sub('old','new',var_name,count)

7)subn()
new_var=re.sub('old','new',var_name,count)

8)split()    
           
'''




import re
a="Good Morning"

'''x=re.match('Good',a)
print(x)#<re.Match object; span=(0, 4), match='Good'>
x1=re.match("ood",a)
print(x1)#None
print(x.start())#0
print(x.end())#4
print(x.group())#Good
'''
'''b=re.fullmatch('Good Morning',a)
print(b)'''
'''
c=re.search('G',a)
print(c)
c=re.search('M',a)
print(c)
c=re.search('n',a)
print(c)
c=re.search('o',a)
print(c)
c=re.search('k',a)
print(c)#None if specific char is not present 
c=re.search('Morni',a)
print(c)
'''
'''d=re.finditer('o',a)
for i in d:
    print("o---------->",i)

d=re.finditer('n',a)
for i in d:
    print("n---------->",i)'''
    
    
'''e=re.sub('o','*',a)
print(e)
e=re.sub('o','*',a,20)
print(e)
e=re.sub('o','*',a,1)
print(e)'''# written type str

'''
f=re.subn('o','*',a)
print(f)
f=re.subn('o','*',a,2)
print(f)
f=re.subn('o','*',a,30)
print(f)'''# written type tuple
'''
h=re.findall('[a-z]',a)
print(h)
h=re.findall('[A-Z]',a)
print(h)
h=re.findall('[0-9]',a)
print(h)
h=re.findall('[a-zA-Z]',a)
print(h)
h=re.findall('[a-z]+',a)
print(h)

h=re.findall('[a-z]*',a)
print(h)'''

'''i="jhvtersreed7uyhHFTRD567YIUK212532566989(*&^%$#$@)"
a=re.findall('[0-9]',i)
print(a)
a=re.findall(r'\d',i) # all the number
print(a)
a=re.findall(r'\D',i) # except number all 
print(a)

'''

'''
x='Hi Hello Hey'
a=re.findall(' ',x)
print(a)
a=re.findall(r'\s',x) # only white space
print(a)
a=re.findall(r'\S',x) # except white space
print(a)
a=re.findall(r'\S+',x)
print(a)'''



'''x="jhvtersreed 7uyhHFTRD56   7YIU _  K212_53    25669    89(*&^% $#$@   )"
a=re.findall(r'\w',x) # all the character / number / _
print(a)
a=re.findall(r'\W',x) # only special character
print(a)'''
'''
a='ABCDEF12345xyz'
i=re.findall('[^ABCD]',a)# if we use ^ it will be exculuded
print(i)
#['E', 'F', '1', '2', '3', '4', '5', 'x', 'y', 'z']
i=re.findall('[ABCD]',a)
print(i)
#['A', 'B', 'C', 'D']

'''

