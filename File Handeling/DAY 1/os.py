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