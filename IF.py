#1)wap to check if the given character is string.
"""a="python"
if type(a)==str:
    print(f'The given character {a} is string')

#user input
a=eval(input('Enter a character: '))
if type(a)==str:
    print(f'The given character {a} is string')
else :
    print(f'The given character {a} is not string')

#2)wap to check if the given value is a single value datatype

a=eval(input('Enter a data: '))
if type(a) in (int,bool,float,complex):
    print(f'The given character {a} is single valued datatype')

#3)wap to check if the given value is a collection datatype
a=eval(input('Enter a data: '))
if type(a) in (str,list,set,tuple,dict):
    print(f'The given character {a} is collection datatype')

#using is instance
a=eval(input('Enter a data: '))
if isinstance(a,(str,list,set,tuple,dict)):
    print(f'The given character {a} is collection datatype')
    print(type(a))

#4)wap to check the given number is positive
a=eval(input('Enter a number: '))
if a>0:
    print(f'The given character {a} is positive')

#5)wap to check the given number is negative
a=eval(input('Enter a number: '))
if a<0:
    print(f'The given character {a} is negative')

#6)wap to check if a number is zero

a=eval(input('Enter a number: '))
if a==0:
    print(f'The given character {a} is zero')

#7)wap if a given number is divisible by 5

b=eval(input('Enter a number: '))
if b%5==0:
    print(f'The given character {b} is divisible of 5')

#8)wap a program to check if 88 is less than 100

c=88
if c<100:
    print(f'The given  {c} is less than 100')

#9)wap a program if a number is three digit number

s=eval(input('Enter a number: '))
if s>=100:
    print(f'The given number {s} is three digit number')

#10)wap a program if a number is three digit number
s=eval(input('Enter a number: '))
if 1000<=s<=9999:
    print(f'The given number {s} is four digit number')

#11)wap if string is in lowercase
a="hello"
if a.islower():
    print(f'The given string {a} is lowercase')

#12)wap if string is uppercase
a="HELLO"
if a.isupper():
    print(f'The given string {a} is uppercase')

#13)wap if a given string contains space
s="hello world"
if ' ' in s:
    print(f'The given string {s} contains space')

#----->using isspace():here we need to pass only space
s=" "
if s.isspace():
    print(f'The given string {s} contains space')

#14)wap to check if the given string starts with capital letter
x="Python"
if x[0].isupper():
    print(f'The given string {x} starts with uppercase')

#15)wap to check if a string contains only alphabets

s=eval(input('Enter a string: '))
if s.isalpha():
    print(f'The given string {s} contains only alphabets')

#16)wap to check if a given string contains only digits
s=eval(input('Enter a string: '))
if s.isdigit():
    print(f'The given string {s} contains only digits')

#17)wap to check if the string ends with a period '.'

s=eval(input('Enter a string: '))
if s.endswith('.'):
    print(f'The given string {s} ends with a period')

#18)wap to check if "a" is present in the string
s="apple"
if "a" in s:
    print(f'The given string {s} contains a')

#19)wap to check if the first and last character of the string is same

s="level"
if s[0]==s[-1]:
    print(f'The given string {s} starts and endswith same character')

#20)wap to check if the given character is vowel

x=input('Enter a character: ')
if x in ("a","e","i","o","u","A","E","I","O","U") : /'aeiouAEIOU'
    print(f'The given character {x} is vowel')

#21)wap to check if the given character is upper case
x=input('Enter a character: ')
if x.isupper():
    print(f'The given character {x} is uppercase')

#22)wap to check if the given character is lowercase
x=input('Enter a character: ')
if x.islower():
    print(f'The given character {x} is lowercase')

#23)wap to check if the given character is digit.
x=eval(input('Enter a data: '))
if x.isdigit():
    print(f'The given data {x} is digit')

#24)wap to check if the asci value of a character is greater than 100
a=input('Enter a character: ')
if ord(a)>100:
    print(f'The given character {a} has ascii value  greater than 100')

#25)wap to check if 5 exists in a list
a=[1,2,3,4,5]
if 5 in a:
    print(f'The given number 5 is a part of the list')

#26)write a program if the last number in the list is even
a=[1,2,3,4,5,6]
if a[-1]%2==0:
    print(f'The given number {a[-1]} is even')

#27)wap to check if the first two elements are same
a=[1,1,2,3,4,5]
if a[0]==a[1]:
    print(f'The first two elements of list are equal')

#28)wap to check if the sum of the list is greater than 100
y=[50,40,30]
if sum(y)>100:
    print(f"Total sum of the list {y} is greater than 100")

#29)wap to check if the year is a leap year.
year=2024
if year%4==0:
    print(f'The given year {year} is leap year')

#30)wap to check if the file name endswith .txt
file='python.txt'
if file.endswith('.txt'):
    print(f'the given file {file} ends with the .txt')

#31)wap to check if the number is divisible by both 3 and 7
num=42
if num%3==0 and num%7==0:
    print(f'The given number {num} is divisible by 3 and 7')

#32)wap to check if the cc no is 16 digit and contains only digits
c='4567829466252468'
if len(c)==16 and c.isdigit():
    print(f'The given cc number is 16 digit and contains only digits')

#33)wap to check if student has scored 70 print good luck
marks=eval(input('Enter marks: '))
if marks==70:
    print(f'Good luck')

#34)wap to check which number is greater
a=98
b=67
if a>b:
    print(f'The given number {a} is greater than the given number {b}')

#35)wap to check if the given string has a even number of characters
a='hey guys you all are great'
if len(a)%2==0:
    print(f'The given string {a} has even number of characters')

#36)wap to check if the given programming language is present in a list
l=['java','c','c++','python','c#','ruby']
check=eval(input('Enter a element: '))
if check in l:
    print(f'The given string {check} is a programming language present in list')

#37)wap to check if person is eligible to vote
age=eval(input('Enter the Age: '))
if age>18:
    print(f'The person is eligible to vote')

#38)wap to check if the given string is palindrome
a=eval(input('Enter a string: '))
if a==a[ : :-1]:
    print(f'The given string {a} is palindrome')

#39)wap to check if a given number is palindrome
a=121
b=str(a)
if b==b[ : :-1]:
    print(f'The given number {a} is palindrome')

#40)wap to check if the first letter of the given string in consonant
a='Rutuja is a good student '
if a[0]  not in 'aeiouAEIOU':
    print(f'The first letter of {a} is a consonant')

#41)wap to check if given value is string
a=input('Enter a value: ')
if type(a)==str:
    print(f'The given value {a} is string')

#42)wap to display 'Python coding' if the given number is greater than 1 and less than 5
num=eval(input('Enter a number: '))
if num>1 and num<5:
    print(f'Python coding')

#43)wap to check if the given number is even and if even,store it in a list
num=eval(input('Enter a number: '))
b=[]
if num%2==0:
    b.append(num)
    print(f'The given number {num} is an even number')
    print(b)

#44)without using inbulit function
b=20
l=[ ]
if b%2==0:
    l=l+[b]
    print(l)

#45)wap to check if the given number is betn 45 to 200 and divisible by both 4 and 5 if so display its ascii character
a=eval(input('Enter a number: '))
if 45<=a<=200 and a%4==0 and a%5==0:
    print(chr(a))

#46)wap to check if a string contains specific substring
a='hello world'
if 'world' in a:
    print(f'The given substring is present in the given string {a}')

#46)wap to check if the character is an alphabet if yes store it in a dict with the char as a key and ascii as value.
a=input('Enter a character: ')
b={}
if a.isalpha():
    b[a]=ord(a)
    print(b)

#47)with using inbuilt function
a=input('Enter a character: ')
b={}
if a.isalpha():
    b.update({a:ord(a)})
    print(b)


#48)wap to check if the given character is uppercase if it is convert it into lowercase and store in dict as a key and ascii as a value
a=(input('Enter a character: ')
b={}
if a.isupper():
    c=a.lower()
    b[c]=ord(c)
    print(b)

#49)with inbuilt function
a=input('Enter a character: ')
b={}
if a.isupper():
    C=a.lower()
    b.update({a:ord(a)})
    print(b)

#50)wap to check if the given  number is even without using %

#by using floor division for even number
a=eval(input('Enter a number: '))
if(a//2)*2==a:
    print(f'The given number {a} is an even number')

#51)by using floor division for odd number
a=eval(input('Enter a number: '))
if(a//1)*1==a:
    print(f'The given number {a} is an odd number')

#52)using bin function
a=eval(input('Enter a number: '))
print(bin(a))
if (a&1)==0:
    print(f'The given number {a} is an even number')
else:
    print(f'The given number {a} is an odd number')

#53)using string conversion
d=6
s=bin(d)[-1]
print(s)
if s=='0':
     print(f'The given number {d} is an even number')

#54)wap to convert uppercase character to lower without using inbuilt function
x='H'
if ord('A')<=ord(x)<=ord('Z'):
    print(chr(ord(x)+32))

#55)wap to convert uppercase character to upper without using inbuilt function
x='h'
if ord('a')<=ord(x)<=ord('z'):
    print(chr(ord(x)-32))

#56)wap to check the given number is digit
a='6'
if ord('0')<=ord(a)<=ord('9'):
    print(f'The given number {a} is digit')

#57)wap to check if given element is digit/uppercase/lowercase
s=eval(input('Enter a element: '))
if (ord('A')<=ord(s)<=ord('Z')) or (ord('a')<=ord(s)<=ord('z')) or (ord('0')<=ord(s)<=ord('9')):
    print(f'The given element is ',s)

#58)wap to check if given element is special character
s=eval(input('Enter a element: '))
if  not (ord('A')<=ord(s)<=ord('Z')) or (ord('a')<=ord(s)<=ord('z')) or (ord('0')<=ord(s)<=ord('9')):
    print(f'The given element is ',s)"""

