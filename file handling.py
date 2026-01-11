"""
FILE HANDLING:

STEP 1: import os
-Methods used in file handling:

1)getcwd():(Current working location in directory)
-It gives you the location where you are currently present in the system.
-Syntax: os.getcwd()

2)chdir():
-It is used if we want to change the current location of the directory.
-Syntax: os.chdir(r'Path')
-Here r indicates the raw string which is used to execute the path as a normal arrangement instead of a special
arrangement, and it won't act as an operation.We will get the output as it is.
-We can also use event slash(\\) if we want to print the sequence as it is.

3)mkdir()
-It is used to create a new folder or directory in a currently present folder.
-Syntax:os.mkdir('folder_name')

4)listdir():
-It is used to list all the files in a directory.
-Syntax: os.listdir()

5)rmdir():
-It is used to remove a directory.
-Syntax: os.rmdir('folder_name')

6)remove():
-It is used to remove a file.
-Syntax: os.remove('file_name.extension')

7)popen():
-It is used to open a file automatically.
-Syntax: os.popen('file_name.extension')

8)rename():
-It is used to rename a file.
-Syntax: os.rename('file_name.extension', 'new_name')

#QUESTIONS:
1)What is difference between chdir() and getcwd()?
2)Can we delete folder by using popen() method?
3)what is the difference between getcwd() and chdir()?
4)How to avoid special sequence present inside the path?
5)How to change the filename/folder name in file_handling?

#File:
-It is a group of data or collection of information.
-It is used when we want to store data temporarily or permanently.

-Types of file:
1)text file--->here we store information or data
2)binary file--->here we store images,video,audio.

-File operations/mode:
1)'r'-read
2)'w'-write
-Here it will always consider the updates data, and we lose data.To avoid this we use append method.
3)'a'-append
4)'x'-create

#file handling syntax:

1)Without context manager:
    new_vn=open('file_name.extension','mode')
-modes(r,w,a,x)
-In without context manager we have to close file manually.

-This are properties and modes used in the file handling.
-The methods where we don't use parenthesis they are known as properties and where we use parenthesis they are known as a modes.
f=open('hello.txt','w')
print(f.mode)           #---->Gives us the mode file is currently present in.
print(f.name)           #---->Gives file name.
print(f.readable())     #---->Gives output in boolean values,True if file is in readable else false.
print(f.writable())     #---->Gives output in boolean values,True if file is in writable else false.
print(f.closed)         #---->Checks if file is closed or not,if closed it will give output as true or else false.
f.close()

#w mode:
- It will always take updated data and previous one will be vanished.
#write():
-It is a mode of file handling.
-It is used to write  single line in a file.
-While using this method our file must be in w mode.
-Syntax:vn=open('file _name.extension','mode')
        vn.write('data')

#writelines():
-It is used to write  multiple lines in a file.
-Syntax:vn.write(['data1\n','data2\n'.....])


#x mode:
-By using x mode we can create a file.
-By using 'w' and 'a' mode also we can create a file, and we can perform operation also,
 but we can't perform any operation.
 -Here we can only create a file.

#r mode:
-read():vn.read()
-readline():vn.readline()
-readlines():vn.readlines()
-read(n):vn.read(n)    ----------->It will give number of characters

2)WITH CONTEXT MANAGER:
-Syntax:
       with open('file_name.extension','mode') as file_object/new vn:
                 pass                   ------>bcoz we are not doing any operations

-Here it will close the file automatically.
-Modes=a,r,w,x

"""
#getcwd()
# import os
# print(os.getcwd())



#ch.dir()
#os.chdir(r'C:\Users\Rutuja\Desktop\New folder')    #--->1
#os.chdir(r'C:\\Users\\Rutuja\\Desktop\\New folder')    #--->2

#print(os.getcwd())

#mkdir()
#os.mkdir('Python')
#os.mkdir('java')
#os.mkdir('sql')

#listdir()
#print(os.listdir())

#rmdir()
#os.rmdir('Python')
#os.rmdir('java')

#remove()
#os.remove('A11.txt')

#popen()
#os.popen('hii.txt')

#rename()
#os.rename('hii.txt','hello.txt')
#os.rename('sql','datalab')

#file=open('hello.txt','r')

#This are properties and modes used in the file handling.
#The methods where we don't use parenthesis they are known as properties and
# where we use parenthesis they are known as a modes.
"""f=open('hello.txt','w')
print(f.mode)           #---->Gives us the mode file is currently present in.
print(f.name)           #---->Gives file name.
print(f.readable())     #---->Gives output in boolean values,True if file is in readable else false.
print(f.writable())     #---->Gives output in boolean values,True if file is in writable else false.
print(f.closed)         #---->Checks if file is closed or not,if closed it will give output as true or else false.
f.close()
print(f.closed)"""

# import os
# print(os.getcwd())
# os.chdir(r'C:\Users\Rutuja\Desktop\New folder')
# print(os.getcwd())
"""
file=open('data.txt','w')
#print(file.write('Welcome to python class'))
#file.write('Good morning')
file.writelines(['python\n','powerbi\n','sql\n','web-tech\n','data'])
os.popen('data.txt')


file2=open('newset.txt','w')
#file2.write('Good luck')
#file2.write('Python programming')
file2.writelines(['Hii\n','hello\n','byee'])
os.popen('newset.txt')

file3=open('dataset.txt','a')
file3.write('Good morning')
file3.write('Good afternoon')
file3.writelines(['Python\n','java\n','cpp\n','PowerBi'])
os.popen('dataset.txt')

file3=open('dataset.txt','r')
#print(file3.read())
#print(file3.readline())
#print(file3.readline())
#print(file3.readlines())
print(file3.read(4))"""

"""#How to create empty textfile without context manager?
new=open('newfile.txt','x')

#How to create empty textfile with context manager?
with open('empty.txt','x'):
    pass

#How to read the file by using without context manager?
new1=open('newfile.txt')

#How to read the file by using with context manager?
with open('dataset.txt','r') as file:
    #print(file.read())
    #print(file.readline())
    print(file.read(5))

#How to write the file by using with context manager?
#write mode
with open('EPSON.txt','w')as file:
     #file.write('File handling')
     #file.write('Hello World')
     file.writelines(['hii\n','byee\n','Good morning\n','good night'])
os.popen('EPSON.txt')

#append mode
with open('append.txt', 'a') as file:
     file.write('File handling\n')
     file.write('Hello World\n')
     file.writelines(['hii\n', 'byee\n', 'Good morning\n', 'good night'])
os.popen('append.txt')"""

"""
4/9/25
CSV FILES:
-Extension-file_name.csv
-They are also known as as comma separated files and spreadsheets.
-Here the data will be present in the rows and columns format.
-STEPS:
1)import csv
-Reading into csv file
   1.reader()
   2.dict_reader() 
   
-Writing into the csv file
    1.writer()
    2.dict_writer()
    
-writer():
1)writerow():Here we can only write single rows.
-syntax:new_var.writerow([data1,data2,data3,....])
2)writerows()Here we can write multiple rows.
-syntax:new_var.writerow([data1,data2,data3,....],[data1,data2,data3,....])

##Syntax:with object ('filename.extension','mode') as file_object:
new_var=csv.writer(file_object)

-dict_writer():
1.writerow():
-Syntax:({data1,data2,data3,....})
2.writerows():
-Syntax:([{},{},{}])
3.writeheader():
"""
#creating empty csv file

#import csv
#with open('second.csv','x') as file:
  #  pass

#adding data into csv
"""with open('second.csv','w',newline='') as file:
   x=csv.writer(file)
   # x.writerow(["HII",'Byee'])
   x.writerows([['Name','Qualification','ID'],['Rutuja','BE','R1234'],['Kiran','BCA','K1234']])
os.popen('second.csv')

with open('students.csv','a',newline='') as file:
   x=csv.writer(file)
   x.writerow(["HII",'Byee'])
   x.writerows([['Name','Qualification','ID'],['Rutuja','BE','R1234'],['Kiran','BCA','K1234'],['Nayan','Btech','N1234']])
os.popen('students.csv')

with open('newdata.csv','w',newline='') as file:
    y=csv.DictWriter(file,['Food_name','Price'])
    y.writeheader()
    y.writerow({'Food_name':'Dosa','Price':'100'})
    y.writerow({'Food_name':'Idli','Price':'20'})
    y.writerows([{'Food_name':'Dosa','Price':'100'},{'Food_name':'Vadapav','Price':'20'},{'Food_name':'Misal','Price':'100'}])
os.popen('newdata.csv')


with open('newdata.csv','r') as file:
    new=csv.DictReader(file)
    # print(new)           #----------><csv.DictReader object at 0x0000024054F35550>
    # print(list(new))     #---------->[{'Food_name': 'Dosa', 'Price': '100'}, {'Food_name': 'Idli', 'Price': '20'},
    # {'Food_name': 'Dosa', 'Price': '100'}, {'Food_name': 'Vadapav', 'Price': '20'}, {'Food_name': 'Misal', 'Price': '100'}]

for i in new:
    print(i)
os.popen('newdata.csv')"""


"""
#Pickle:
-Process to convert normal python object to bytestream.
-It is also known a serialisation.
-To convert bytestream to normal python object is known as unpickling or deserialisation.
-Byte stream we cannot read completely.
-Here if we work on pickling first step is to---->import pickle.
-Here extension should be .pkl.
-While working pickle we are supposed to use rb and wb mode instead of r and w i.e read binary and write binary.

-PICKLE OPERATIONS:
1)Without file handling operations:
   -dumps()
   -loads()
2)With file handling operations:
  -dump()
  -load()
  
#dump() and dumps():
-Used to convert normal python object to bytestream.

#loads() and loads():
-Used to convert bytestream to normal python object.


"""
"""
import pickle

x=['abc','back','snap','hitman','HP']
q=pickle.dumps(x)
# print(q)

w=pickle.loads(q)
print(w)
"""
"""
syntax for dumps()
new_var=pickle.dumps(iterable)

syntax for loads()
new_var=pickle.loads(previous_var_name)
"""

"""
#With using file handling:

-dump():
syntax 1:
   with open ("filename.pkl","mode") as file_object:
   new_var=pickle.dump(file_object,iterable)
   os.popen('filename.pkl')
   
-load():
Syntax 2:
   with open ("filename.pkl","mode") as file_object:
   new_var=pickle.load(file_object)
   os.popen('filename.pkl')"""
   

import os
print(os.getcwd())
os.chdir(r'C:\Users\Rutuja\Desktop\New folder')
print(os.getcwd())
"""
import pickle

with open('back.pkl','wb') as file:
    w=pickle.dump(['abc','back','snap','hitman','HP'],file)

    os.popen('back.pkl')

with open('back.pkl','rb') as file:
    data=pickle.load(file)
    print(data)
"""
"""
with open('happy.txt','w') as file:
    file.writelines(['Filehandling\n','Regular expression\n','OOPS concept\n',
                     'Exception handling\n','Function and generators'])
    os.popen('happy.txt')

from itertools import islice


-It is used to read the file data from top to bottom
with open('filename.ext,'mode') as file_object:
new_var=islice(file obj,si,ei+1,sv)

with open('happy.txt','r') as file:
    data=islice(file,0,3,1)
    for i in data:
     print(i)"""

from collections import deque

"""
with open('filename.ext','r') as file_object:
    new_var=deque(file_obj,no of lines to be printed)
"""

# with open('happy.txt','r') as file:
#     x=deque(file,2)
#     print(x)
"""
s=deque([1,2,3,4])
s.append(100)
s.appendleft(200)
s.extend('RAM')
s.extendleft("RAM")
s.pop()
s.popleft()
print(s)


a=['a','b','c','d','a','b','c']
d={}
for i in a:
    d[i]=a.count(i)
print(d)

from collections import Counter
q=Counter(a)
print(q)

z=[1,2,3,4,3,2,1,3,4,5,6,7,7,6,5,4,3]
w=Counter(z)
print(w)

print()

x=w.most_common(2)
print(x)"""

"""
#tell():Tells us the current position of the cursor in the file.It will always starts from 0th position

#seek():It is used to navigate your cursor and transfer it from one location to another according to your requirement


with open('happy.txt','r') as file:
    print(file.tell())      #----->0
    print(file.read())       #---->It will give all data present in the file
    print(file.seek(3))       #------>3
    print(file.readline())    #------>ehandling
"""


import pickle

x=['abc','back','snap','hitman','HP']
q=pickle.dumps(x)
print(q)

with open('back.pkl','rb') as file:
    data=pickle.load(file)
print(data)