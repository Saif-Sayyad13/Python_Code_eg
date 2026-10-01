
'''import os
print(os.getcwd())
os.chdir(r"C:\Users\prabh\Desktop\e14")
import csv'''
'''
with open("PQR.csv","w",newline="")as file:
    new_var=csv.writer(file)
    # new_var.writerow(["Apple",100,200])
    # new_var.writerow(["Mango",10,20])
    new_var.writerows([["Apple",100,200],
                       ["Mango",10,20],
                       ["Banana",150,200]])
os.popen("PQR.csv")
'''

'''
with open("note.csv","w",newline="")as file:
    x=csv.DictWriter(file,fieldnames=["EID","ENAME","SAL"])
    x.writeheader()
    # x.writerow({"EID":111,"ENAME":"A","SAL":9000})
    # x.writerow({"EID":112,"ENAME":"B","SAL":10000})
    x.writerows([{"EID":111,"ENAME":"A","SAL":9000},
                 {"EID":112,"ENAME":"B","SAL":8000},
                 {"EID":113,"ENAME":"C","SAL":7000},
                 {"EID":114,"ENAME":"D","SAL":6000}])

os.popen("note.csv")

'''








'''
with open("note.csv","r")as file:
    e=csv.DictReader(file)
    for i in e:
        print(i)
'''
'''
with open("note.csv","r")as file:
    e=csv.reader(file)
    print(tuple(e))
'''









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
'''import os
import csv
os.chdir('/Users/saifsayyad/Downloads/Python QSP')

with open ('RCB.csv','w',newline="") as file:
    x=csv.writer(file)
    x.writerows([["Name",'Subject','Rating'],['A',"PY","*"],['B',"SQL","1.5"],['C',"power bi","2"]])
    
os.system('open RCB.csv')
'''
"""import os
import csv
os.chdir('/Users/saifsayyad/Downloads/Python QSP')

'''with open('file1.csv','w',newline="") as file:
    x=csv.DictWriter(file,fieldnames=['EID','ENAME','SAL'])
    x.writeheader()
    x.writerows([{"EID":111,"ENAME":"aman","SAL":6754}])
    
os.system('open file1.csv')
'''
with open("file1.csv","r")as file:
    e=csv.reader(file)
    for i in e:
        print(i)"""
        
'''
import os
import csv
os.chdir('/Users/saifsayyad/Downloads/Python QSP')

file_name = 'inventory.csv'
headers = ['PROD_ID', 'ITEM_NAME', 'PRICE']

is_empty = not os.path.isfile(file_name) or os.path.getsize(file_name) == 0

with open(file_name, 'a+', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    if is_empty:
        writer.writeheader()
 
    writer.writerows([{"PROD_ID": "P101", "ITEM_NAME": "Laptop", "PRICE": 55000}])
os.system(f'open {file_name}')
'''