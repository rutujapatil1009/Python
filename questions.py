#GROUP 1
#1)Function to add two numbers(user_input)
"""def add():
    a=int(input('Enter a number 1: '))
    b=int(input('Enter a number 2: '))
    print(a+b)
add()

#2)Function to check even or odd
def num():
    a=int(input('Enter a number: '))
    if a%2==0:
        print('Even')
    else:
        print('Odd')
num()

#3)Function to find factorial
def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    print(result)
fact(4)


#4.Function to reverse a string (take user input)
def rev():
    a=input('Enter a string:')
    print(a[::-1])
rev()

#5.Function to check palindrome
def palindrome():
    a=input('Enter a string:')
    if a==a[::-1]:
        print('Palindrome')
    else:
        print('Not a palindrome')
palindrome()

#6.Function to find maximum number in a list
#x=[1,2,3,4,55]
def max_num(x):
    num=x[0]
    for i in x:
        if i>num:
            num=i
    print(num)
max_num([1,2,3,4,55])

#7)Function to count vowels in a string
#s="i Love India"
def vowel(s):
    a=0
    for i in s:
        if i in 'aeiouAEIOU':
          a+=1
    print(f'The total number of vowels is {a}')
vowel("i Love India")

#8.Function to calculate simple interest
#formula=P*R*T/100
#P=1000,Rate=120 T=30
def si(P,R,T):
    print(f'Simple interest:',P*R*T/100)
si(1000,120,30)

#9.Function to check Armstrong number (take user input)
num=int(input("Enter a number :"))
def armstrong(num):
    sum=0
    x = len(str(num))
    print("Length of num",x)
    for i in str(num):
         sum = sum + int(i) ** x
    if sum == num:
     print("Armstrong number")
    else:
        print("Not armstrong number")
armstrong(num)

#10.Function to calculate sum of digits
#s=12345
def sum(s):
    a=0
    for i in s:
        a+=int(i)
    print(a)
sum('12345')"""

"""
#GROUP 2
#1.Function to check leap year (take user input)
def leap_yr():
    a=input('Enter a year :')
    if int(a)%4==0:
        print('Leap Year')
    else:
        print('Not a leap year')
leap_yr()

#2.Function to count words in a string
#string="Python is powerful"
def words(string):
  count=string.count(' ')
  print('Number of words in a string:',count+1)
words('Python is powerful')

#3.Function to merge two dictionaries
#s={1:2,4:5,6:7}
#s1={11:34,78:100}
def dictionary():
    a=eval(input('Enter a dictionary :'))
    b=eval(input('Enter a dictionary :'))
    a.update(b)
    print(a)
dictionary()

#4.Count vowels and consonants
#x="Hello world"
def vowel_consonant(x):
    vowel=0
    consonant=0
    for i in x:
        if i in 'aeiouAEIOU':
            vowel+=1
        else:
            consonant+=1
    print('Number of Vowels:',vowel,'Number of consonants:',consonant)
vowel_consonant('Hello word')

#5.Reverse string without slicing
s="Python"
def rev(s):
  for i in reversed(s):
    print(i,end='')
rev('Python')

#Merge two lists (without +)
#x=[1,2,3,4]
#y=[4,5,6,7]
def merge(a,b):
    a.extend(b)
    print(a)
merge([1,2,3,4],[4,5,6,7])

#7.Function to check positive, negative or zero
def num():
    a=int(input('Enter a number :'))
    if a>0:
        print('Positive number:',a)
    elif a<0:
        print('Negative number:',a)
    elif a==0:
        print('Zero:',a)
num()

#8)Function to find minimum number in a list (without inbuilt)
#s=[1,2,3,4]
def max_num(x):
    num=x[0]
    for i in x:
        if i<num:
            num=i
    print(num)
max_num([1,2,3,4])

#9.Function to calculate area of circle
def area():
    r=int(input('Enter radius :'))
    print("Area of circle:",3.14*(r**2))
area()

#10.Function to calculate area of rectangle(lengthxwidth)
def rect():
    a=int(input('Enter a Length:'))
    b=int(input('Enter a width:'))
    print('Area of rectangle:',a*b)
rect()"""

#GROUP 3
"""#1.Function to check if string is an anagram

#2.Function to count digits in a number
#s=12345
def digit(s):
    count=0
    for i in s:
        if i.isdigit():
            count+=1
    print(count)
digit('12345')

#3)Function to remove duplicates from list
#l=[1,2,2,3,4,4,5]
def dup(l):
    result=[]
    for i  in l:
        if i not in result:
            result.append(i)
    print(result)
dup([1,2,2,3,4,4,5])

#4)Function to return largest word in a sentence
#s="Python is very powerful language"
def fun():
    s = "python is very powerful language"
    large= ""
    for i in s.split():
        if len(i) > len(large):
            large= i
    print('Largest word:',large)
fun()

#5.Function to swap two numbers without temp
def swap(a,b):
    a,b=b,a
    print(a,b)
swap(10,20)

#6.Remove spaces from string
#s="hello world"
def space(s):
        print(s.replace(' ',''))
space("hello world")

#7.Convert string to title case
#x="python programming"
def title(x):
    print(x.title())
title("python programming")

#8.Sum of list elements
#c=[1,2,3,4]
def sum(c):
    s=0
    for i in c:
        s+=int(i)
    print(s)
sum([1,2,3,4])

#9.Product of list elements
#c=[1,2,3,4]
def product(c):
    s=1
    for i in c:
        s*=i
    print(s)
product([1,2,3,4])

#10.Count even numbers in list
#d=[1,2,3,4,6]
def even(d):
    count=0
    for i in d:
        if i%2==0:
            count+=1
    print(count)
even([1,2,3,4,6])"""

#GROUP 4
"""
#1.Count odd numbers in list
#s=[1,2,3,4,6]
def odd(d):
    count=0
    for i in d:
        if i%2==1:
            count+=1
    print(count)
odd([1,2,3,4,6])

#2.Count uppercase and lowercase letters
#s="HeLLo GuYs"
def upper_lower(s):
    upper=0
    lower=0
    for i in s:
        if i.isupper():
            upper+=1
        else:
            lower+=1
    print('uppercase letters:',upper,'Lowercase letters:',lower)
upper_lower("HeLLo GuYs")

#3.Replace spaces with underscore
#x="I love Python"
def rep(x):
    print(x.replace(' ','_'))
rep("I love Python")

#4. Find max and min in tuple(min(),max())
#s=(1,5,2)
def max_num(x):
    max=x[0]
    min=x[0]
    for i in x:
        if i>max:
            max=i
        else:
           min=i
    print('Maximum number:',max)
    print('Minimum number:',min)
max_num((1,5,2))

#5.Function to sum all values in a dictionary
#x={'a':10, 'b':20, 'c':30}
def sum(x):
    s=0
    for i in x.values():
        s+=i
    print(s)
sum({'a':10, 'b':20, 'c':30})

#6.Function to count words in a string
#y="Python makes coding easy"
def words(string):
  count=string.count(' ')
  print('Number of words in a string:',count+1)
words('Python makes coding easy')

#7.Remove all digits from a string
a="He11o2025"
#o/p-->Heo
def digit(a):
    result=''
    for  i in a:
        if i.isalpha():
            result+=i
    print(result)
digit("He11o2025")

#8.Swap first and last characters of a string
#s="Python"
#o/p-->nythop
def swap(s):
    s=list(s)
    s[0],s[-1]=s[-1],s[0]
    s = ''.join(s)
    print(s)
swap('Python')

#9.Convert list of tuples to dictionary
#x=[("a",1),("b",2),("c",3)]
#o/p-->{'a':1,'b':2,'c':3}
def tup(x):
    t=dict(x)
    print(t)
tup((("a",1),("b",2),("c",3)))

#10.Check if key exists in dictionary
def key(x):
    a=input('Enter the key:')
    if a in x.keys():
        print('Key exists in a dictionary')
key({'a':1,'b':2,'c':3})"""

#GROUP 5
"""
#1.Create dictionary from two lists
#a=["a","b","c"]
#b=[1,2,3]
#o/p-->{'a':1,'b':2,'c':3}
def dic(a,b):
    result={}
    for i,j in zip(a,b):
        result.update({i:j})
    print(result)
dic(["a","b","c"],[1,2,3])"""

#Convert dictionary to list of tuples
#x={"a":1,"b":2,"c":3}
#o/p--> [('a',1),('b',2),('c',3)]
def dic(x):
    result=tuple(x)
    print(result)
dic({"a":1,"b":2,"c":3})






