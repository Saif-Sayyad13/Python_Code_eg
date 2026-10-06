'''
  FILE HANDLING
          OS module:

*OS stands for "operating system".
*to perform file operation/handling we use a methods in OS module that is,

1.getcwd():
    *it stands for "current working directory".

# a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]



         *it will return to its current location.
    syntax: os.getcwd()

    
2.chdir():
    *it stands for "change directory".
 *it will change path/location from current to specified location/path
    syntax: os.chdir("path")

    
3.popen():
    *This method is used to open a file/pop up a file.
    syntax: os.popen("file_name")


4.mkdir():
    *it stands for "make directory".
    *This method is used to create a directory in a specified location/path.
    *it will throw an error if we create a directory which already exists.
    syntax: os.mkdir("directory_name")

5.rmdir():
    *it stands for "remove directory".
    *this method is used to remove the directory from specified location/path.
    *it will throw an error if we try to remove a directory which is already removed.
    syntax: os.rmdir("directory_name")

6.remove():
    *This method is used to remove a file(any kind of file).
    syntax: os.remove("file_name")

7.listdir():
    *it stands for "list directory".
    *it will return a list of files and directory present in a specified location.
    syntax: os.listdir()

8.os.path.exists():
    *it will return True if the specified path exists else it will return False.
    syntax: os.path.exists("path")

9.rename():
    *This method is used to rename a file.
    syntax: os.rename("old_filename", "new_filename")
"""

import os
#example on getcwd()
# print(os.getcwd())
#C:\Users\user\PycharmProjects\M9_python\programs

#example on chdir()
# os.chdir(r"E:\mrng_file")
# print(os.getcwd())
#E:\mrng_file

#example on popen()
# os.chdir(r"E:\mrng_file")
# os.popen("demo.txt")
# os.popen("pic.png")
#example on mkdir()
# os.chdir(r"E:\mrng_file")
# os.mkdir("afternoon")

#example on creating a existing folder/same folder name
# os.chdir(r"E:\mrng_file")
# os.mkdir("afternoon")
# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'afternoon'

#example on creating 5 folders
# fname = ['mon', 'tue', 'wed', 'thu', 'fri']
# os.chdir(r"E:\mrng_file")
# for name in fname:
#     os.mkdir(name)

#example on rmdir()
# os.chdir(r"E:\mrng_file")
# os.rmdir("mon")
# os.rmdir("sample.txt")

# os.chdir(r"E:\mrng_file")
# os.rmdir("mon")
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'mon'

#example on remove()
# os.chdir(r"E:\mrng_file")
# os.remove("sample.txt")
# os.remove("pic.png")

#example on listdir()
# os.chdir(r"E:\mrng_file")
# print(os.listdir())
#['demo.txt', 'fri', 'pic.png', 'thu', 'tue', 'wed']

#example on os.path.exists()
# print(os.path.exists("E:\mrng_file\demo.txt"))
# #True
# print(os.path.exists("E:\mrng_file\sample.txt"))
# #False

#example on rename()
# os.chdir(r"E:\mrng_file")
# print(os.listdir())         #['demo.txt', 'fri', 'pic.png', 'thu', 'tue', 'wed']
# os.rename("demo.txt", "sample.txt")
# print(os.listdir())         #['fri', 'pic.png', 'sample.txt', 'thu', 'tue', 'wed']
                              FILE

*a file is a collection of data/a group of information is called a file.
*each file will be identified by its own extensions.
example:
--------
document file, pdf file, image file, audio file, video file, apk file, programs file, zip file, exe file etc....
example:
--------
.docx, .txt, .pdf, .xlsx, .csv, .ppt, .py, .java, .jpeg, .png, .mp3, .mp4, .exe, etc.....

file operations:
****************
*There are 4 file operations that are read/write/append/create file.
*for each file operation there is mode,
---------------------------------------
* "r" -> read
-------------
    *"r" is a default mode in all the file.
    *it means we can just read a file but we can't write anything inside a file.
    
* "w" -> write
--------------
    *when we want to write anything inside a file then we go "w" mode.
    *it will override old data, meaning old data will be removed and new data will be written.

"a" -> append:
--------------
    *when we want to append something into an existing file then we go "a" mode.
    *it will keep old data and it will add new data in a file.

"x" -> create:
--------------
    *When we want to create a new file we use "x" mode.

*To perform any file operations we need to open a file, to open a file we use a method called "open()" method.


*opening a file in python there are 2 ways,
*******************************************
1.without context manager:
    *in this syntax we should manually close the file.
    syntax:
    -------
    var_name = open("file_name", "mode")
    

2.with context manager:
    *in this syntax we automatically close the file when it comes out of the block.

    syntax:
    -------
    with open("file_name", "mode") as var_name:
        ...

1.creating a file:
******************
*to create a file we use the open() method with "x" mode.
"""
import os
os.chdir(r"E:\build")

# #without context
# file = open("sample.txt", "x")

#creating docx file
# file = open("dim.docx", "x")

#creating image file
# file= open("pic.jpeg", "x")

# #with context
# with open("demo.txt", "x") as file:



2.reading a file:
*****************
*to read a file we use open() method with "r" mode and writing "r" mode is optional because default mode of
open() method will be "r".

*to get the content from the file we have 4 ways,
1.file object:
    *here we need to type-casting/run a for loop to get the correct output.
    syntax:
    -------
    file_object = open("file_name", "r")

2.read():
    *it will read the complete file and return output in string format.
    syntax:
  -------
    file_obj.read()
3.readline():
    *it will return the 1st line of file.
    syntax:
    -------
    file_obj.readline()

4.readlines():
    *it reads the complete file and returns output in list format
.
    *Each line is an individual element of the list.
    syntax:
    -------
    file_obj.readlines()
"""
#without context
#example on file object
# file = open("sample.txt", "r")
# print(file)
#<_io.TextIOWrapper name='sample.txt' mode='r' encoding='cp1252'>

#converting file_object to list
# file = open("sample.txt", "r")
# print(list(file))
#['day without class a day is best day\n', 'guys be interactive\n', 'tomato is to costly\n', 'same house and husband boring.']

#run for loop for file object
# file = open("sample.txt", "r")
# for i in file:
#     print(i.rstrip("\n"))
"""
day without class a day is best day 
guys be interactive
tomato is to costly
same house and husband boring.
"""

#example on read() method
# file = open("sample.txt")
# print(file.read())
"""
day without class a day is best day
guys be interactive
tomato is to costly
same house and husband boring.
"""

#example on readline()
# file = open("sample.txt")
# print(file.readline())
#day without class a day is best day

#example on readlines()
# file = open("sample.txt")
# print(file.readlines())
# #['day without class a day is best day\n', 'guys be interactive\n', 'tomato is too costly\n', 'same house and husband boring.\n']
"""


"""
3.writing into a file:
**********************
*to write into a file we use the open() method with "w" mode.

*in "w" mode it will always over-ride on file.

*if a file is present then it will override the data.

*if file is not present then it will create a file and write into a file 

*to write into a file we have 2 methods that is,

1.write():
    *it will write single line into a file
    syntax:
    ------
    file_obj.write("value")
    
2.writelines():
    *it will write multiple lines into a file.
    *this method will accept iterable as an argument.
    syntax:
    -------
    file_obj.writelines(iterables)
"""
#example on writing into existing file
# with open("sample.txt", "w") as file:
#     file.write("today is tuesday")

#example on writing into not existing file
# with open("sample12.txt", "w") as file:
#     file.write("today is tuesday")

#writing multiple lines in existing file
# with open("sample.txt", "w") as file:
#     file.writelines(["hai\n", "hello\n", "how\n", "bye\n"])
        l.append(line.split()[0]+"\n")

with open("sample.txt", "w") as file:
    file.writelines(l)
"""

"""
4.appending into a file:
************************

*to write data into a file by keeping old data then we go "a" mode.

*if it will keep old data and for the existing file itself only it will write and there is no data loss.

*to append into a file we use 2 methods,
1.write():
    *it will write single line into a file
  syntax:
    ------
    file_obj.write("value")
    
2.writelines():
    *it will write multiple lines into a file.
    *this method will accept iterable as an argument.
    syntax:
    -------
    file_obj.writelines(iterables) 
"""

#appending to a existing file
# with open("sample.txt", "a") as file:
#     file.write("Mahesh 77\n")

#appending to a file not exists
# with open("sample12.txt", "a") as file:
#     file.writelines(["Lokesh 77\n", "Kumar 59\n", "Rum 99\n"]


csv file handling:
******************
*csv stands for "comma separated values".

*When a text file consists of values separated with commas and need to convert to excel then we go to csv format.

*to read and write csv files we should use the import csv module.

reading csv file:
*****************
*to read csv file we have 2 methods,
1.reader():
***********
*reader() method will return output in list format.
syntax:
-------
from csv import *
with open(fil_name) as file_obj:
    data =csv. redader(file_obj)
    
2.DictReader():
**************
*dictreader() method will give output in dictionary format.
*header will become key and cell will become value.
syntax:
-------
from csv import *
with open(fil_name) as file_obj:
    data =csv. Dictreader(file_obj)

"""
writing into csv file:
**********************
*to write in a csv file we use the open() method with "w" mode.
*in csv file for writing there are 2 ways,
1.writer():
***********
*this method will accept only iterables.
*when we are writing multiple rows it will leave one line blank to avoid this we use newline="".
*in writer() method there are 2 ways are present,
1.writerow():
    *it will write only a single row.
    syntax:
    -------
    with open("file_name", "w") as file_obj:
    wb = csv.writer(file_obj)
    wb.writerow(iterable)
    
2.writerows():
    *it will write multiple rows.
    syntax:
    -------
    with open("file_name", "w") as file_obj:
    wb = csv.writer(file_obj)
    wb.writerows(iterable1, iterable2, iterable3, ....)
    
2.DictWriter:
*************
*it will accept a dictionary as an argument.
*First we need to declare the header in the dictwriter() method.
*to write we have 2 methods,

1.writerow():
    *it will write only a single row.
    syntax:
    -------
    with open("file_name", "w") as file_obj:
   wb = DictWriter(file_obj, [header1, header2, header3])
    wb.header()
    wb.writerow([{header1:value, header2:value, header3:value})
    
2.writerows():
    *it will write multiple rows.
    syntax:
    -------
    with open("file_name", "w", newline="") as file_obj:
    wb = DictWriter(file_obj, [header1, header2, header3])
    wb.header()
    wb.writerows([{header1:value, header2:value, header3:value},)
                {header1:value, header2:value, header3:value}, .... ])

"""
#writer() method
#example on writerow() method
"""
with open("data.csv", "w") as file:
    wb = writer(file)
    wb.writerow(["Kumar", "EEE", 78.23, 2019])
"""

#example on writerows() method
"""
with open("data.csv", "w", newline="") as file:
    wb = writer(file)
    wb.writerows([["Kumar", "EEE", 78.23, 2019],
                 ["Komal", "CS", 73, 2017],
                 ["Vimal", "IS", 58, 2020]])
"""

#dictwriter() method
#example on writerow() method
"""
with open("data.csv", "w", newline="") as file:
    wb = DictWriter(file, ['sname', 'branch', 'per', 'mob'])
    wb.writeheader()
    wb.writerow({'sname':'Hemi', 'branch':'ME', 'per':77, 'mob':67893456})
"""

#example on writerows() method
"""
with open("data.csv", "w", newline="") as file:
    wb = DictWriter(file, ['sname', 'branch', 'per', 'mob'])
    wb.writeheader()
    wb.writerows([{'sname':'Hemi', 'branch':'ME', 'per':77, 'mob':67893456},
                 {'sname':'Rami', 'branch':'Civil', 'per':87, 'mob':45678945},
                 {'sname':'Pumi', 'branch':'CS', 'per':57, 'mob':123456}])
"""







'''



'''#OS(Operating System) Module
#Step1-->
#import os
#getcwd() #We will be use this when we have to see the current path
#cwd stand for current working directory

import os
print(os.getcwd())#This is given current path or directory 
                  #O/P--->C:\Users\Victus\AppData\Local\Programs\Python\Python313 

#This is used to change the directory

#os.chdir(r"Path")

#os.chdir("C:\Users\Victus\Desktop\E14")#Here because of single slash it will showing the Unicode
                                        #Error because odd slash is treated as special symbol it comes
                                        #on to the new lines to avoid this there is  one concept called
                                        #raw string

os.chdir(r"C:\Users\Victus\Desktop\E14")


#This is used to making the folder

#os.mkdir(Folder_Name) #By using this only we can create single -single Folders

#os.mkdir("Python") #We have to comment out first created folder before going to created the second folder 

#os.mkdir("SQL")#Here now we are created new folder called SQL


#If we want to create the nested folder then there we have to follow the this
#syntax-->os.makedirs("folder1\folder2\folder3...")

#Example-->

#os.makedirs("A\B\C\D")

#If we want to check how many files are present inside the Main Folder then we have follwed this concept
#Which will return that all files in list format
#print(os.listdir())

#print(os.listdir()) #O/P-->['A', 'hii.txt', 'hii.txt.txt', 'Python', 'SQL']

#This is used to rename the folders

#os.rename("Old_Name","New_Name")
#Example-->

#os.rename("Python","Java")  #Here now name of folder is Java Previously it was Python

#os.rename("hii.txt","string.txt")

#By using this syntax we can delete only the folders

#os.rmdir("Folder Name")

#os.rmdir("SQL") #Here SQL folder is deleted or removed the SQL folder From the E14

#Removing the nested folder by using this Syntax-->os.rmdir("Folder Name")

#os.rmdir("A\B\C\D") #Here one by one folder will be deletd such as here first D folder is deleted 

#os.rmdir("A\B\C") #Now here C folder is deleted

#os.rmdir("A\B") #Now here B folder is deleted now


#os.popen("Folder_Name")

#os.popen("Java")

#File Handleing-->
#Storing the any data Temporarerly or Permanently is called the file handeling

#There are 2 types of files

#1]Text File-->Human readable file
#2]Binary File--->Present in 01010 format or not readable by the humans

#Syntax-->New_Var=open("File_name.extension","Mode")

#file=open("Marker.txt","w")
#print(file.name) #print(Variable_Name.name) this is used to display the name of file o/p-->Marker.txt

#print(file.mode)#By default mode will be r

#print(file.mode)#By default mode will be r

#print(file.writable()) #This will checke whether the given file is in writable mode or not if yes then
                       #it will return as a True  o/p-->True

#print(file.readable())#o/p-->False

#os.popen("Marker.txt") #Directly it will displaying the or open the file

#'r' Mode-->'r' stand for read here using 'r' mode we can create as well as read the data
#The drawback of 'r' Mode is it will stored or hold the latest one text or data only it will removing
#the previouse stored text or data

#print(file.read(12))  #Syntax-->read(n) This is return the character based on the passing the number
#print(file.read()) #It will display all the data from the file
#print(file.readline()) #This will return the first line of the file o/p-->Python

#print(file.readline())
#print(file.readline())



#file2=open("Demo.txt","w")
#file2.write("Good Luck") #Drawback of the write mode is whatever we will be write previously it will
                          #won't show the previous data it will show latest one write data only 
#file2.write("GoodNight")
#os.popen("Demo.txt")
#file1=open("pen.txt","w")
#file1.write("Good Luck")
#os.popen("pen.txt")
#file1.write("Good Luck")
#os.popen("pen.txt")


#'a' mode-->'a' stand for append using 'a' mode we can create or we can write or we read the data or text
#Here advantage is whatever the data we will be write here that previously data or text also can be stored or hold with
#latest one data or text

#fil=open("Data.txt","a")
#fil.write("Sujit")
##os.popen("Data.txt")

'''