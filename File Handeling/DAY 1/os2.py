'''import os
os.chdir('//Users//saifsayyad//Downloads//Python QSP')
file=open("aman.txt","w+")
file.write("aman is king")
print(file.tell())
file.seek(0)
print(file.readline())'''

'''import os
os.chdir('//Users//saifsayyad//Downloads//Python QSP')
with open("abc.txt","a") as file:
    file.write('qwerty')
    file.write('123456')
    file.write('qwerty,qwe345trgdf')
os.popen("abc.txt")
'''

'''import os
os.chdir('//Users//saifsayyad//Downloads//Python QSP')
import csv
with open ('RCB.csv','w',newline="") as file:
    x=csv.writer(file)
    x.writerows([["Name",'Subject','Rating'],['A',"PY","*"],['B',"SQL","1.5"],['C',"power bi","2"]])
    
os.popen("RCB.csv")'''
import os
print(os.getcwd())
os.chdir(r"C:\Users\prabh\Desktop\e14")
import csv
with open("RCB.csv","w",newline="")as file:
    x=csv.writer(file)
    # x.writerow(["ID","ENAME","SAL"])
    # x.writerow(["A123","ABC","1000"])
    # x.writerow(["A55","xyz","100"])
    x.writerows([["Name","sub","Rating"],["A","PY","*"],["B","SQL",1.5],["C","PowerBI",2]])
os.popen("RCB.csv")


























'''
file=open("dell.txt","r")
print(file.readline())
print(file.tell())
print(file.readline())
http://file.seek(0)
print(file.tell())
print(file.readline())
http://file.seek(2)
print(file.tell())
print(file.readline())
'''

'''
file=open("done.txt","w+")
file.write("class completed")
print(file.tell())
http://file.seek(0)
print(file.tell())
print(file.readline())
print(file.tell())
'''
'''
file=open("marker.txt","r+")
print(file.readline())
file.write("\n Good luck\n")
http://file.seek(14)
print(file.readline())
'''

"""
new_var=open("File_extension","mode")

            OR
            
with open("File_extension","mode")as file_object:
    pass
"""
'''
with open("abc.txt","w") as file:
    # file.write("ABCDEFGHIJKL")
    # file.write("234567890-09876543")
    file.writelines(["12345\n","asdfghj\n"])

os.popen("abc.txt")
'''










