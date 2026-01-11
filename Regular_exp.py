"""
#Regular expression:
-If we want to represent a group of string,according to particular pattern/format then we should
go for regular expression format.
-It will only support for string datatype.
-Step 1:   import re
-Here re refers to regular expression.
-Following are the methods used in the regular expression:
1)match()
2)fullmatch()
3)search()
4)finditer()
5)sub()
6)subn()
7)findall()
8)split()


#match():
-syntax:new_var_name=re.match("pattern",source_of_string)
-It will check if the pattern we  pass is present in the beginning.
-If it matches it will return object address
-If it doesn't match it will return None
-It won't check middle or last characters it will check the first characters

#fullmatch():
-syntax:new_var_name=re.fullmatch("pattern",source_of_string)
-Here it will check complete iterable as a pattern if it matches it will give us object address
-If it doesn't match with complete string it will return None

#search():
-syntax:new_var_name=re.search("pattern",source_of_string)
-If it matches it will return object address
-If it doesn't match it will return None
-Here it will give us a position of the character which we are supposed to find.
-But it wil only consider the first occurrence of the character.
-Here we can check in the middle,end or beginning according to the requirement.

#finditer()
-Syntax:new_var_name=re.finditer("pattern",source_of_string)
-Here it will give us all occurrences of the data in the string.
-Here it will give us callable iterator object as a output to get a proper output there are 2 ways:
1)looping
2)typecasting

#sub():
-These are replace methods.
-Syntax:new_var_name=re.sub("old_pattern",'new_pattern,source_of_string,count)
-Return type is string

#subn():
-These are replace methods.
-Here 'n' refers to the number of characters replaced.
-The return type of subn is tuple.

#findall():
-Syntax:new_var_name=re.findall("pattern",source_of_string)
-The return type of findall is list.


*If we want to find only t start we have to use ^ symbol and if we have to find end we have to use $ symbol.

"""
import re
"""
#match()
s="python class"
w=re.match('pyt',s)             #------><re.Match object; span=(0, 3), match='pyt'>
print(w)
print(w.start())        #--->0
print(w.end())         #------->3
print(w.group())       #------->pyt

#fullmatch()
s='Data base'
w=re.fullmatch('Data base',s)
print(w)                #-------------><re.Match object; span=(0, 9), match='Data base'>
print(w.start())        #------------->0
print(w.end())          #------------>9
print(w.group())        #----------->Data base

#search()
x="Welcome all"
y=re.search('e',x)
print(y)            #----><re.Match object; span=(1, 2), match='e'>
print(y.start())      #-------->1
print(y.end())          #-------->2
print(y.group())       #------>e

#finditer()
s="Good afternoon everyone"
w=re.finditer('o',s)
print(w)             #---># <callable_iterator object at 0x000001ABD27F1000>

#print(list(w))      #----->[<re.Match object; span=(1, 2), match='o'>, <re.Match object; span=(2, 3), match='o'>,
                           # <re.Match object; span=(11, 12), match='o'>, <re.Match object; span=(12, 13), match='o'>,
                           # <re.Match object; span=(20, 21), match='o'>]

for i in w:
    print("o-->",i)      #o--> <re.Match object; span=(1, 2), match='o'>
                         #o--> <re.Match object; span=(2, 3), match='o'>
                         #o--> <re.Match object; span=(11, 12), match='o'>
                         #o--> <re.Match object; span=(12, 13), match='o'>
                        #o--> <re.Match object; span=(20, 21), match='o'>

#sub()
d="programming"
w=re.sub('g','*',d,6)
print(w)"""

"""
#findall()
s='Welcome to ALL 2025'
w=re.findall('[a-z]+',s)
print(w)

w1=re.findall('[a-z]',s)
print(w1)"""
"""
#match any number between 0-9
a=('The cost of the books is Rs.100')
w=re.findall('[0-9]',a)
print(w)
w1=re.findall('[0-9]+',a)
print(w1)

#match only lower case letter and upper case letter
b='Hello how ARE you'
w=re.findall('[a-zA-Z]',b)
print(w)

#write a program to count the number of white spaces in a given string
c='Hello world welcome to python HI how are you.Hii how are you'
w3=re.findall('\s',c)
print(len(w3))

#wap to sum all the digits
word='cfghjkl345678igfdcx'
num=re.findall('[0-9]',word)
print(num)
total_sum=0
for i in num:
    total_sum+=int(i)
print(total_sum)

#match everything apart from numbers between 0-9
a=('The cost of the books is Rs.100')
w=re.findall('[A-Za-z]+',a)
print(w)

#match everything apart from abcd
a='abcdefghjkytrd'
w=re.findall('[^abcd]+',a)
print(w)

#match only numbers
word='@234dtyujnbvcghjk'
w=re.findall('[0-9]+',word)
print(w)

#extract file extension
s='Downloading the archive.zip file to download folder python hero.py and afternoon.txt'
q=re.findall("[a-zA-Z]+\.[A-za-z]+",s)
print(q)

d='back space'
import re
w=re.search('c',d)
print(w.start())
print(w.end())
print(w.group())
print()
print(w.start())
print(w.end())
print(w.groups())
"""
"""
#creating acronyms of the file format
file_format=['Graphic Interchange Format',
             'Advanced Audio Coding',
             'Hypertext Markup Language',
             'Content Management System',
             'Windows Audio Media']
for i in file_format:
    pattern=re.findall('[A-Z]',i)

    print(''.join(pattern))

w='Helloworld welcome to python'
q=re.sub('','\n',w)
print(q)


#replace all digits with **
q='hello 123 mic testing 123 123'
w=re.sub('123','**',q)
print(w)

#print  only dob
text='My date of birth is 22-5-2025'
w=re.findall(r'\d{2}-\d{1,2}-\d{4}',text)
print(w)

#wap to print tha pan card number
a=('My pan card number is ABCWE1234X and other number is POIUY1237V'
   'and id is  123abcd45')
b=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1}',a)
print(b)

#wap to print adhar card
text='my adhar card number is 1234-5678-9876'
y=re.findall(r'\d{4}-\d{4}-\d{4}',text)
print(y)

#wap to print pin code
s=('Banglore pincode is 560001 and area code is BSK234567 ')
w=re.findall( r'\b\d{6}\b', s)
print(w)

#wap to fetch the protocol

#wap to print the phone number (in us style)
phonenum=['123-234-7893','253-678-0987','900-234567890']
for i in phonenum:
    pattern=re.findall('\d{3}-\d{3}-\d{4}',i)
    print(pattern)


#wap to print email
emails=['rutupatil1009@gmail.com'
        'dapatil12@gmaail.com',
        'ujwala12@gmail.in']

for i in emails:
    pattern=re.findall(r'[A-Za-z0-9]+@[A-Za-z]+\.[a-z]+',i)
    print(pattern)"""


import re
x='my phone number is 9168803722'
y=re.search(r'(\d{3})(\d{3})(\d{4})',x)
print(y.group())      #------>9168803722
print(y.group(1))     #------>916
print(y.group(2))     #------>880
print(y.group(3))     #------>3722
print(y.groups())      #------>('916', '880', '3722')




