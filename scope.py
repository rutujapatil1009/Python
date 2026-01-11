"""scope:---> Place where we are storing the variable name

Types of scope(3)
1.local variable scope
2.global variable scope
3.Nonlocal variable scope"""
"""
#step1
#local variable i am accessing inside the function
def Local_fun():  #function_declaration

    name="Kiran"  #------> Local variable
    sal=25000     #------> Local variable

    print(f'my name is {name} and my total salary is {sal}')
Local_fun()      #function_calling

#step2

#local variable am accesing outside without using return keyword
 
def Local_fun():  #function_declaration

    name="Kiran"  #------> Local variable
    sal=25000     #------> Local variable

    print(f'my name is {name} and my total salary is {sal}')
Local_fun()
print(name,sal) #NameError

#Note:--> without return keyword if we access local variable outside
#        it will show name error.

#step3

#local variable am accesing outside with using return keyword

def Local_fun():  #function_declaration

    name="Kiran"  #------> Local variable
    sal=25000     #------> Local variable

    return (f'my name is {name} and my total salary is {sal}')
new_var=Local_fun()
print(new_var)

"""


"""
Global variable

#step1----> global variable am accessing inside and outside the function
x=100    #Global variable
def Display():
    y=200    #local variable
    print(x)
Display()
print(x)


#step2
#global variable modification outside the function.

x=100    #Global variable
def Display():
    y=200    #local variable
    print(x)  #100
Display()
x=x+400  #x+=400   100=100+400
print(x)  #500

"""
#step3---> global variable modification inside the function

'''
global variable modification inside the function without using global keyword
x=100    #Global variable
def Display():
    x=x+400
    print(x)  #UnboundLocalError
Display()
print(x)
'''

"""
Global variable modification inside the function by using global keyword
x=100    #Global variable
def Display():
    global x
    x=x+400
    print(x)
Display()
print(x)
"""
"""
Non_local variable 
#step1
x=10  #Global variable
def Outer():
    y=20   #non_local variable
    print(y)
    print(x)
    def inner():
        print(y)
        z=30    #local variable
        print(x)
        print(z)

    inner()
    print(y)
    print(x)
    # print(z)  #Name error

Outer()
print(x)
# print(y)  #NameError
# print(z)  #Name error

#step2--->
def Outer():
    y=100
    def inner():
        nonlocal y
        y=y+200
        print(y)
    inner()
Outer()
"""

#wap to perform addition if a is greater than b else print difference
"""
def operation(a,b):
    if a>b:
        print(a+b)
    else:
        print(a-b)
operation(10,25)
operation(40,6)

def operation():
    a=int(input('Enter the first number: '))
    b=int(input('Enter the second number: '))
    if a>b:
        print(a+b) 
    else:
        print(a-b)
operation()

#wap to check string is palindrome or not
def palindrome():
    a=input('Enter the string:')
    if a==a[::-1]:
        print('String is palindrome')
    else:
        print('String is not palindrome')
palindrome()

#wap for squaring and cubing the element is the given list
def sq(l):
    b=[]
    for i in l:
        b.append((i**2,i**3))
    return b
s=sq([1,2,3,4,5])
print(s)

#wap to fetch the last digit
x=123
def num(a):
    return a%10
d=num(123)
print(d)

def sl(a):
    return str(x)[-1]
t=sl(123)
print(t)

#wap to take 3 numbers from user and add first two and result is to be subtracted by third number
def op():
    a=int(input('Enter the first number: '))
    b=int(input('Enter the second number: '))
    c=int(input('Enter the third number: '))
    ad=a+b
    print(ad)
    sub=c-ad
    print(sub)
op()

#wap to find sq,cube and sqroot and cuberoot

def sq():
    a=int(input('Enter the number: '))
    return a**2,a**3,a**0.5,a**0.333
op=sq()
print(op)

import math
def sq():
    a=int(input('Enter the number: '))
    return a**2,a**3,math.sqrt(a),math.cbrt(a)
op=sq()
print(op)

#wap to check whether the given character is alphabet or digit or special character
def character(x):
    if x.isalpha():
        print("Character is alphabet")
    elif x.isdigit():
        print("Character is number")
    else:
        print("Character is special character")
character('a')
character('11')
character('@')

x='TRACXN'
def data(x,i):
    return x[i::2]
sl=data('TRACXN',0)
print(sl)

#wap to check if the arguments passed in a positional variable argument are greater than 5
def fun(*args):
    if len(args)>5:
        print('The length of args is greater than 5')
    else:
        print('The length of args is less than 5')
fun(1,2,3,4,5,6,7)"""

#