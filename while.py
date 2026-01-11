"""
                                                      WHILE LOOP
-Looping:executing set of instructions again and again.
-While loop:It is used whenever we don't know the number of iterations.Here it will execute set of instructions again
               and again until the condition becomes false.
-Here increment and decrement are to be done manually.

-Steps to follow inn while loop:
1)Start(initialisation)
2)Stop(condition)
3)Update(increment/decrement)

-Syntax:
        start(new variable)
        while condition:
               statement(new variable)
               update(new variable)(+/-)

-here the variable used in start is supposed to be used in the place of statement and update.
-here the variable used is always pointing towards the position of the character.



-While loop types:
1)Finite loop:
-Whenever we are executing using all three steps(start,stop,update) then we are supposed to use finite loop.
- Flowchart for finite loop:

           start
            |
        condition(true)
            |
        executed
            |
        update
            |
        stop condition(false)


2)Infinite loop:
-Whenever we are executing using only two steps(start,stop) then we are supposed to use infinite loop.
-Flowchart of infinite loop:

          start
            |
        condition(true always)
            |
        executed
            |
        repeated forever


"""
from math import factorial

"""
#wap to print 1 to 5 numbers
start=1
while start<=5:
    print(start)
    start+=1

#waptp 1 to 10 num

i=1
while i<=10:
    print(i)
    i+=1
#waptp 10 to 1 num
i = 10
while i >= 1:
    print(i)
    i-=1

#waptp all the characters
x='PYTHON'
k=0
while k<len(x):
    print(k,x[k])
    k+=1

#waptp all numbers in list
w=[11,12,13,14,15]
k=0
while k<len(w):
    print(k,w[k])
    k+=1

d=('hii',[1,2,3,4],{56,65},45.89)
i=0
while i<len(d):
    print(i,d[i])
    i+=1


d={1:67,89:100,45:200}
i=0
while i<len(d):
    print(i)
    i+=1

#wap to calculate total of all the elements.
#FOR LOOP
x=[1,2,3,4,5]
total=0
for i in x:
    total=total+i
print(total)

#WHILE LOOP
x=[1,2,3,4,5]
total=0
i=0
while i<len(x):
    total=total+x[i]
    i+=1
print(total)

#waptp only complex value
y=['abc',123,900,34+5j,6.7]
#o/p=34+5j
i=0
while i<len(y):
    if type(y[i])==complex:
         print(y[i])
    i=i+1


#waptp collection datatype
y=['abc',[1,2,3],900,34+5j,6.7]
i=0
while i<len(y):
    if type(y[i]) in (list,str):
         print(y[i])
    i=i+1

#waptp only vowels and digits
x='India won the cup  in 2024'
i=0
while i<len(x):
    if x[i] in 'aeiouAEIOU' or x[i].isdigit():
        print(x[i],end=' ')
    i=i+1

#waptp alternate character in the given string
s='Work hard'
i=0
while i<len(s):
    print(s[0::2])
    break
    
s='Work hard'
i=0
while i<len(s):
    print(s[i])
    i=i+2

#waptp odd length of the words
s=['snap','cam','num','shift','ALT','FH','ESC']
i=0
while i<len(s):
    if len(s[i])%2==1:
        print(s[i],end=' ')
    i=i+1
    
#waptp table of 2
#for loop
num=int (input('Enter a number: '))
for i in range(1,11,1):
    print(f'{num}*{i}={num*i}')

#while loop
num=int (input('Enter a number: '))
i=1
while i<=10:
    print(f'{num}*{i}={num*i}')
    i=i+1

#waptp odd and even numbers in 0 to 20 in list

even=[]
odd=[]
i=0
while i<=20:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i += 1
print(even)
print(odd)

#waptp10,20,20,....300
i=0
while i<=300:
    print(i)
    i+=10


#waptp a-z
x = ord('a')
while x <= ord('z'):
    print(chr(x), end=' ')
    x += 1

#waptp A-Z

x=ord('A')
while x<=ord('Z'):
    print(chr(x),end=' ')
    x+=1

#waptp Aa-Zz
x = ord('A')
y=ord('a')
while x<=ord('Z') and y<=ord('z'):
    print(chr(x),chr(y))
    x+=1
    y=y+1

x=[900,123,'abc',8.9,True,4+5j,['a','b','c','d']]
#o/p:x=[900,123,'abc',8.9,True,4+5j,'a','b','c','d']
i = 0
while i < len(x):
    if type(x[i]) == list:
        nested = x.pop(i)       
        b=x+nested
        print(b)
    i+=1

#wapt iterate inside list check if it has nested list it yes merge it
y=['hello',10,20.55,True,False,'hai','bye',[False,'goodnight','enjoy the holiday']]
i=0
while i<len(y):
    if type(y[i])==list:
        a=y.pop(i)
        b=y+a
        print(b)
    i+=1

#wap to count number of  occurrence of a specified element is the collection
s='Hello guys python is a programming language'
a=eval(input('Enter the character:'))
i=0
total_char=0
while i<len(s):
    if s[i]==a:           #both side same char it will be true or else false
       total_char+=1
    i+=1
print(total_char,end=' ')

#waptp the position of the substring
st1=eval(input('Enter the string:'))
st2=eval(input('Enter the substring:'))
i=0
while i<len(st1):
    if st2 in st1[i]:
        print(st1[i],i)
    i+=1

# 6.wap to print the names only if the length of the names is even
l=["vaidehi","ashwini","patil","shrinidhi","sushmita","rahul","priyanka","usha"]
i=0
while i<len(l):
    if len(l[i])%2==0:
        print(l[i])
    i+=1

# 7.wap to print the elements which in tuple, print only  if
# it is collection data types
values=(10,2.5,[10,20],"hero", True,(3,4,5),{2,7},{90:"super"})
i=0
while i<len(values):
    if isinstance(values[i],(str,list,tuple,set,dict)):
       print(values[i])
    i+=1

# 8.wap to print the name which is starting with vowel in the given list
x=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
i=0
while i<len(x):
    if x[i][0] in "AEIOUaeiou":
        print(x[i])
    i+=1

# 10.wap if a names ends with vowels then reverse a names else print its length
n=["Kumar","Latika","Umesha","Priyanka"]
i=0
while i<len(n):
    if n[i][-1] in "AEIOUaeiou":
        print(n[i][::-1])
    else:
        print(len(n[i]))
    i+=1

# 11.wap to print following numbers
#105,98,91...........7
i=105
while i>=7:
    print(i)
    i-=7

#Sum of first N natural numbers
num=int(input('Enter a number:'))
sum=0
i=1
while i<=num:
    sum+=i
    i+=1
print(sum)


#Factorial of a number
num=int(input('Enter a number:'))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)"""












