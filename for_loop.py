#LOOPING: A set of instructions it will repeat again and again.
#Types of looping:1)for loop
                # 2)while loop
#while loop:
#-used whenever we don't know the number of iteration.
#-a set of instruction executing again and again until the condition becomes false.
#-here we need to manually do increment and decrement

#for loop:
#-used whenever we know the number of iteration
#-here increment and decrement will happen internally

# for variable in iterable:
#       statement


"""#wap to print all numbers present is a list
x=[10,20,30,40,50]
for a in [10,20,30,40,50]:
    print(a,end=' ')
print()

a='python'
for i in a:
    print(i,end=' ')
print()
#we use end property when we want output in a row format instead of column

a=(11,22,31,21,45)
for i in a:
    print(i,end=' ')
print()

a={'hii','byee',33,21,2}
for i in a:
    print(i,end=' ')
print()

a={1:2,45:22,'hii':3,'py':4}
for i in a:
    print(i,end=' ')
print()

a={1:2,45:22,'hii':3,'py':4}
for i in a.values():
    print(f'{i}',end=' ')
print()

a={1:2,45:22,'hii':3,'py':4}
for i in a.items():
    print(i,end=' ')
print()

a={1:2,45:22,'hii':3,'py':4}
for i in a:
    print(a[i],end=' ')
print()

#wap to print only even numbers
x=[1,2,3,4,5,6]
for i in x:
    if i%2==0:
        print(i,end=' ')

#wap to print only odd numbers
x=[1,2,3,4,5,6,7]
for i in x:
    if i%2==1:
        print(i,end=' ')

#wap to print the even length of the character in the list
y=['abc','xy','a','anop','abcde','ab']
for i in y:
    if len(i)%2==0:
        print(i,end=' ')

#wap to print the odd length of the character in the list
y=['abc','xy','a','anop','abcde','ab']
for i in y:
    if len(i)%2==1:
        print(i,end=' ')

#wap to print which number is divisible by 5
a=[10,15,25,35,78,134,160]
for i in a:
    if i%5==0:
        print(i,end=' ')

#wap to create a dict in key position character and value position ascii value(using inbuilt)
a='evening'
b={}
for i in a:
    b.update({i:ord(i)})
print(b,end=' ')

#wap to create a dict in key position character and value position ascii value(without using inbuilt)
a='evening'
b={}
for i in a:
    b[i]=ord(i)
print(b,end=' ')

#wap to print only single value data type
a=['hello',[1,2,3],True,False,{89:10},7+8j]
for i in a:
    if isinstance(i,(int,float,bool,complex)):
        print(i)

#wap to print only collection data type
a=['hello',[1,2,3],True,False,{89:10},7+8j]
for i in a:
    if isinstance(i,(str,list,tuple,set,dict)):
        print(i)

#wap to extract vowels and digits in a string
s='hello123'
for i in s:
    if i in 'aeiouAEIOU' or i.isdigit():
        print(i)

#wap to capitalize only first letter of every word
a=['vaidehi','rahul','shivam','kapil','patil']
for i in a:
    i=i.capitalize()
    print(i)

#wap to print the count of alphabets and numbers and spaces
a='india got the independence in the year 1947'
alpha=0
num=0
space=0
for i in a:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        num+=1
    else:
        space=space+1
print(f'Total number of alphabets:{alpha}\nTotal number of digits:{num}\nTotal number of spaces:{space}')"""
from itertools import count

#inbilt functions:
#1)range()
#2)reversed()
#3)enumerate()
#4)zip()
#5)zip_longest()


#1)range()--->
#here we can only pass numbers it won't accept characters.
#syntax:    for variable in range(si,ei+1,step value)
#                  statement(variable)


"""#wap to print 1 to 10 numbers
for i in range(1,11,1):
    print(i,end=" ")
print()

#wap to print numbers upto 4 without si and sv.
for k in range(5):
    print(k,end=" ")
print()

#wap to print 0 to 20 even numbers
for i in range(0,21,2):
    print(i,end=" ")

for i in range(0,21,1):
     if i%2==0:
         print(i,end=" ")

#wap to print both index and character in the given string
z='smart'
for i in range(len(z)):   #len(z)----->for i in range(5)
    print(z[i],i)          #indexing--->v_n[position]

#wap to print the string
d=['hello','exit','bye','smart','think']
for i in range(len(d)):
    print(d[i],i)"""


#2)reversed()
#normal syntax:reversed()
#            print(reversed(iterable))
#If we use normal syntax it will give us output in an object and data address
#It is not useful for set as it doesn't accept duplicate character, and it is an unordered datatype.
#It will give us value error is we use it for dict.
#syntax:for variable in reversed(iterable)
#             statement

#---->reverse():it is only used in list datatype
#     reversed():it is used for any iterable


"""s=[1,2,3,4]
for i in reversed(s):
    print(i,end=' ')
print()
a={1:2,3:4,6:4}
for i in reversed(a):
    print(i,end=' ')
print()
y=('abc',999,121,333,555)
for i in reversed(y):
    print(i,end=' ')"""


#Ways to reverse a string

"""#slicing
a='Enter'
for i in a[::-1]:
    print(i,end=' ')
print()

#reversed()
for i in reversed(a):
    print(i,end=' ')
print()

#range()
for i in range(-1,-len(a)-1,-1):
    print(a[i],end=' ')
print()

#without using inbuilt function
s=''
for i in a:
    s=i+s
print(s)"""



#3)enumerate():
#syntax:for variable in enumerate(iterable):
#              statement
#Here we will get the output in the form of tuple
#We can print both position and a character with using enumerate
"""d='Good luck'
for i in enumerate(d):
    print(i,end=' ')
print()
d='Good luck'
for position,character in enumerate(d):
    print(position,character)"""


#4)zip():
#It is used to match position to position format
#Here your iterable length should be equal or else you will lose data
#Here we can pass any iterable
#Here we can pass unlimited variables

"""s='python'
a=[1,2,3,4,5,6]

for i in zip(s,a,):
    print(i,end=' ')"""

#5)zip_longest():
#Step 1:    from itertools import zip_longest
#            for variable in zip_longest(v1,v2,v3.....)


"""from itertools import zip_longest
a=[1,2,3,4,5]
b=(11,22)

for i in zip_longest(a,b):  #zip_longest(v1,,v2,fillvalues=
    print(i,end=' ')

print()
#here we can fill the values which are not mentioned by using fill values
from itertools import zip_longest
a=[1,2,3,4,5]
b=(11,22)

for i in zip_longest(a,b,fillvalue=9):  #zip_longest(v1,,v2,fillvalues=)
    print(i,end=' ')"""


"""#wap to print 1-20 and segregate even and odd numbers into separate lists
even_num=[]
odd_num=[]
for i in range(1,21,1):
    if i%2==0:
       even_num.append(i)
    else:
       odd_num.append(i)
print(f'even_num:{even_num}')
print(f'odd_num:{odd_num}')


#wap to check how many words are present in a given sentence
s='hello world sentence'
words=1
for i in s:
    if " " in i:
        words+=1
print(f'words:{words}')


total_word=0
for in in s.split():
print(i)
    total_word=total_word+1
    print(f'total_word:{total_word}')

#wap to create a dictionary and traverse into it
# and if the length is even print it as is it or else reverse it
a=['apple','google','yahoo','microsoft','gmail','walmart']
b={}
for i in a:
    if len(i)%2==0:
        b[i]=i
    else:
        b[i]=i[::-1]
print(b)

#wap to create a dictionary with element and its count
a=['red','yellow','black','pink','orange','green','red','pink','yellow']
b={}
for i in a:

    if i in b:
        b[i]+=1
    else:

        b[i]=1
print(b)


d={}
for i in a:
   d[i]=a.count(i)
print(d)

#wap to reverse a string without using inbuilt function
x='you did it guys'
for i in x[::-1]:
    print(i,end=' ')
print()

for i in reversed(x):
    print(i,end=' ')
print()

for i in range(-1,-len(x)-1,-1):
    print(x[i],end=' ')
print()

s=''
for i in x:
    s=i+s
print(s)

#wap to extract vowels and digits in a string
s="hello123"
for i in s:
    if i in'aeiou' or i.isdigit():
        print(i,end=' ')

#wap to create a dictionary and print the characters
#and its Ascii value pair
s="hello world"
b={}
for i in s:
    b.update({i:ord(i)})
print(b,end=' ')

#wap to print series of factorial(take user input)
n = int(input('Enter a number: '))
fact = 1

print('Factorial series:')
for i in range(1, n + 1):
    fact *= i
    print(f"{i}! = {fact}")

#wap to find the length of the string without using inbuilt function
s="Never Give Up"
len=0
for i in s:
    len= len + 1
print(f'Length of the string:{len}')

#wap to print alternative character from a given string
s="hello python"
for i in range(0,len(s),2):
    print(s[i],end=' ')


#wap to create a dictionary index and word pair
s="tomorrow is weekend and non-veg special"
z=s.split()     
t={}
for i,j in enumerate(z):   #i--->position,j--->char
    t[i]=j      #t.update({i:j})
print(t)

#.wap to create a dictionary words and its length pair
s="tomorrow is weekend and non-veg special"
t={}
for i in (s.split()):
    t.update({i:len(i)})
print(t)

#wap to create a dictionary characters and its corresponding upper case characters
s="sunday"
t={}
for i in (s):
    t.update({i:i.upper()})
print(t)

#wap to create a dictionary Ascii and character pair
l=[89,51,111,77,108,120]
t={}
for i in l:
    t.update({i:chr(i)})
print(t)

#wap to  create a list of characters and its Ascii value pair
s="sunday"
t=[]
for i in s:
    t.append((i:ord(i)))
print(t)

#wap to create a dictionary with words and its length pair and ends with vowel
s = "Anna is here to enjoy a banana"
t={}
for i in (s.split()):
    if i[-1] in "aeiou":
      t.update({i:len(i)})
print(t)

#.wap to create a dictionary with letter and its words starting with that letter pair
s="hi hello good morning welcome to python session"
t={}
for i in (s.split()):
    if i[0] not in t:
        t[i[0]]=[i]
    else:
        t[i[0]]+=[i]
print(t)


t={}
for i in (s.split()):
    t.setdefault(i[0],[]).append(i)
print(t)

#.wap to create a dictionary word and reverse word pair
s="tomorrow is weekend and non-veg special"
t={}
for i in (s.split()):
    t[i]=i[::-1]
print(t)

#wap to create a dictionary of characters and its indices pair
s="hello python"
a={}
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]  not in a:
            a[s[i]]=[]
            a[s[i]].append(([i],[j]))
print(a)

#Reverse a list without using any built-in functions and slicing.
l = [1, 2, 3, 4]
s=[]
for i in l:
    s=[i]+s
print(s)

#wap to Sum of numbers
s = 'Sony12India567pvt21ltd'
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)

#Print all the missing numbers from 1-10 in the below list
l = [1, 2, 3, 4, 6, 7, 10]
a=[]
for i in range(1,11,1):
    if i not in l:
        a.append(i)
print(a)

#.WAP to remove duplicates from the list without using inbuilt function
d=[1,2,3,4,5,6,7,1,2,3,4]
a=[]
for i in d:
  if i not in a:
      a.append(i)
print(a)

#.wap to replace all the character with "-" if the characters occurs more than once in a string
s="hellohai"
a=""
for i in s:
    if s.count(i)>1:
        a+='-'
    else:
        a+=i
print(a)

for i in s:
     if s.count(i)>1:
         s=s.replace(i,"_")
print(s)

#wap to print first and last char of each name in the list
a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
b=[]
for i in a:
    b.append((i[0],i[-1]))
print(b)

#.wap to create a new list as square of each number of below list
b=[2,4,5,6,7,1]
squ=[]
for i in b:
    squ.append(i**2)
print(squ)

#wap if number is even the print its square else print its cube
c=[2,4,5,3,7,9]
for i in c:
    if i%2==0:
        print(i**2)
    else:
        print(i**3)
print(i)

#wap to create a list with square and cube of each numbers
d=[2,4,5,1,8,9,10]
a=[]
for i in d:
    a.append((i**2,i**3))
print(a)

#wap to create a new list of reversing each name from the list
names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
rev=[]
for i in names:
    rev.append(i[::-1])
print(rev)

#wap to create a new list, of individual and collection data type from list
data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
individual=[]
collection=[]
for i in data:
    if isinstance(i,(int,bool,float,complex)):
        individual.append(i)
    else:
        collection.append(i)
print(f'Individual:{individual}')
print(f'Collection:{collection}')

#wap to create a dictionary characters and its count pair
char=["a","M","i","A","M","I","i","H","a","H"]
d={}
for i in char:
   d[i]=char.count(i)
print(d)

#wap to group fruit name and country pair
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d.keys(),p.values()):
    print(i)

#wap to sum of same index element from l1,l2,l3
l1=[10,20,30,40]
l2=[78,44,11,99]
l3=[1,2,3,4]
for i in zip(l1,l2,l3):
    print(sum(i))

#wap to pair values of both dictionary
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}

for i in zip(d.values(),p.values()):
    print(i)

#wap to print only file name
x=["python.txt","http://java.py","http://sql.in","http://web.com"]
l=[]
for i in x:
    e=i.split('.')     #   o        1
    if e[0] not in l:  #if e[0]------> ["python" "txt"]
        l.append(e[0])
print(l)

#wap to print only extension name
x=["python.txt","http://java.py","http://sql.in","http://web.com"]
l=[]
for i in x:
    e=i.split('.')
    if e[1] not in x:
        l.append(e[1])
print(l)

#wap to print----> abcdef----------->z
x=ord('a')
for i in range(26):
    print(chr(x+i),end='')

#wap to print----> ABCDEFG-------->Z
x=ord('A')
for i in range(26):
    print(chr(x+i),end='')

#wap to print ---->AaBbCc-------->Zz
x=ord('A')
y=ord('a')
for i in range(26):
    print(chr(x+i),chr(y+i),end='')

#.wap to print 2 tables
num=eval(input("Enter a number:"))
for i in range(1,11,1):
    print(f'{num}*{i}={num*i}')

#wap to print  given list into flatten
w=[[1,2],[3,4],[5,6],[7,8]]
#o/p-->[1,2,3,4,5,6,7,8]
z=[]
for i in w:
    z.extend(i)
print(z)

#WAP to get the given o/p
s = 'hi hello good morning'
#exp o/p: 'gninrom doog olleh ih'
res=''
for i in s:
    res=i+res
print(res)
t=''
for i in s:
    t=i[::-1]+''+t
print(t)
"""


"""Transfer statements:
1)break
2)continue
3)pass
"""

"""#Stop when a negative number is found
nums = [10, 20, -3, 40]
for i in nums:
    if i<0:
        break
    print(i)

#Break when sum exceeds 15
l=[1,2,3,4,5,6]
sum=0
for i in l:
    sum+=i
    if sum>15:
        break
    print(sum)

#stop searching for element 9
lst = [4, 7, 2, 9, 5]
for i in lst:
    if i==9:
        break
    print(i)

#Stop after first vowel
s="python"
for i in s:
    if i in 'aeiouAEIOU':
        break
    print(i)

#Stop counting when divisible by both 3 and 5 (1,51)
for i in range(1,52,1):
    if i%3==0 and i%5==0:
        break
    print(i,end=' ')

#CONTINUE

#skip negative numbers
nums = [4, -2, 7, -5, 10]
for i in nums:
    if i<0:
      continue
    print(i,end=' ')

# Skip vowels
s="elephant"
for i in s:
    if i in 'aeiouAEIOU':
        continue
    print(i,end='')

#Print only odd numbers(1,11)
for i in range(1,12):
    if i%2==0:
        continue
    print(i,end=' ')

#Skip numbers divisible by 3(1,21)
for i in range(1,22):
    if i%3==0:
        continue
    print(i,end=' ')

#Skip uppercase letters
s="pytHOn"
for i in s:
    if i.isupper():
        continue
    print(i,end=' ')

#print till value is less than 4
x=[1,2,3,4,5,6]
for i in x:
  if i==4:
     break
  print(i)

a=[12,34,90,67,89,2,4,5,6,10]
for i in a:
    if i%2==1:
        pass   #here it will print all elements as pass just traverse through given data it does not skip any element
    print(i)"""

"""#1.wap to remove repeated values and return in set
l=[2,3,4,2,5,6,2,3]
b=set()
for i in l:
    if i not in b:
        b.add(i)
print(b)

#2.wap to take two lists and return a set by adding elements present same index

l1=[2,3,4,5,6,7,8,9]
l2=[5,6,7,8,9,1,2,3]
a=set()
for i,j in zip(l1,l2):
    a.add(i+j)
print(a)"""

