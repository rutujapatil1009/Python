"""
#Function-
-A set of statement or block of code it will execute when we are calling function_name,without calling the function_name
if we execute it will show blank space.

*Why we are using functions?
-To avoid repetition.
-Code reusability.

*Types of function:
1)Predefined functions(inbuilt)(Eg:len(),id(),type()...)
2)User defined functions(created by user)

*Syntax_1:
def function_name(parameter):    ---->function declaration
   block of code
function_name(argument)          ---->function calling

-Parameter is variable name and argument is value.
-If we don't pass any parameter then we don't need to pass any argument.
-If we use print function in block of code we don't need to pass print function again outside,
if we do it will show none as output.
-If we use function_name without parenthesis it will act as a normal word and won't show any error.
-If we want to print object address we can use print(function_name) as it will be pointing to complete
functions object address.

*Syntax_2:
def fun_name(parameter):    ---->function declaration
   block of code
   return data1,data2
new_v_n=fun_name(Argument)
print(new_v_n)

-If we use return keyword inside the function it is mandatary outside we need to use print()
if we won't, we will get blank space as an output.
-Here return is a keyword used to access local variable outside the function.
Eg:
def hii():
   c='python'
   return c
a=hii()
print(a)
-Here we can't use multiple return keyword if we use multiple return keyword it only
 executes first operation and terminate it won't move forward.
-Here if we want to use multiple return keyword we have passed them in single line.
-If we carry out multiple operations it will give us output in tuple format.

##LOCAL VARIABLE:
-Any variable present inside the function is known as local variable.
-We can't access local variable outside it, we access it will show name error,
to avoid error we have to use return keyword.

#Types of argument while calling the functions:

1)Normal argument(positional):
-Eg:
     def fun(a,b,c):
         print(a,b,c)
     fun(1,2,3)
-Here a will be pointing to  1 and b to 2 and so on,if we miss anyone argument equivalent to the
    parameter it will show type error.
-Number of parameter should always be equal to number of arguments.

2)Variable positional argument------>(*args):
-* is a mandatory as it acts like a fixed property while in the place of args we can use any name.
-Return type of *args will be tuple.
-While calling we need to pass property without *.
-Eg:
    def fun(*args):
       print(args)
    fun()
-If we don't pass any  argument it will return us empty tuple as an output.
-Here we can pass unlimited argument.

3)keyword argument------>>var_name=value---->parameter=argument:
-Here parameter=argument is mandatary as it will act like a keyword if we don't it will act as a positional argument.
-Eg:
    def spam(a,b,c):
        print(a+b+c)
    spam(a=1,b=2,c=3)

4)variable keyword argument---------->(**kwargs):
-Return type of **kwargs will be dictionary.
-Here **kwargs is a property where ** is mandatary while we can use any name in the place of kwargs.
-Here if we won't pass data in the format of v_n and value it will show error.
-If we pass nothing it will give us empty dictionary.
-Eg:
   def spam(**kwargs):
       print(kwargs)
   spam()---------->empty dict
   spam(1)--------->error
   spam(aa=1,b=2,c=3)---------->will work like key value pair.
   -Here we can pass unlimited characters.

5)combination of *args and **kwargs:
-Eg:def think(*args,**kwargs):
       print(args,kwargs)
    think()
    -Here if we don't pass data we will get the output as a empty tuple and empty dictionary.

6)only positional  argument(/)
-before / we need to pass positional argument while after we need to pass keyword argument or positional

7)only keyword arguments(*)
#before * we can  pass positional argument or keyword  while after we need to pass keyword argument.

8)combination of only keyword and only positional arguments

#Type of argument:

        TOA
         |
       Scope
       / |  \
      /  |   \
    / non-local\
local            \
variable         global variable
           |
    function program
           |
        lambda
          map
        filter
           |
        Recurssion
           |
        generator
"""
"""
def greet():
    print('Good morning!!')
greet()

#wap to check if number is odd or even.

def num(x):
    if x%2==0:
        print('even num')
    else:
        print('odd num')
num(30)
num(5)
num(3111)

#wap to check if the given element is a palindrome
def element():
    x=input('Enter the element:')
    if x==x[::-1]:
        print('it is a palindrome')
    else:
        print('it is not a palindrome')
element()

s=[1,2,3,4,5]
l=[]
for i in s:
    l.append(i**2)
print(l)

def sqr(list):
    l=[]
    for i in list:
        l.append(i**2)
sqr([1,2,3,4,5])

#s='Backspace'
def ascii(s):
    a={}
    for i in s:
        a[i]=ord(i)
        a.update({i:ord(i)})
    print(a)
ascii('Backspace')

#wap to print which number is divisible by 5
#x=[12,45,67,90,100,30]
def num(x):
    l=[]
    for i in x:
        if i%5==0:
            l.append(i)
    print(l)
num([12,45,67,90,100,30])

#wap to print only odd length word
#y=['num','lock','apple','mango','word','the']
def word(y):
    l=[]
    for i in y:
        if len(i)%2==1:
            l.append(i)
    print(l)
word(['num','lock','apple','mango','word','the'])"""


"""
#POSITIONAL ARGUMENT:
def demo(a,b,c):
    print(a,b,c)
demo(1,2,3)
demo(1,2)    # TypeError: demo() missing 1 required positional argument: 'c'

#VARIABLE POSITIONAL ARGUMENT:
def demo(*py):
    print(py)
demo([1,2,3,4],'hii',{1:3})

#KEYWORD ARGUMENT:
def spam(a, b, c):
    print(a + b + c)
spam(a=1, b=2, c=3)

#VARIABLE KEYWORD ARGUMENT:
def spam(**kwarg):
    print(kwarg)
spam()                 #------->{}
spam(1)                #------->TypeError: spam() takes 0 positional arguments but 1 was given
spam(a=2,b=4,h=10)     #------>{'a': 2, 'b': 4, 'h': 10}
spam(a=100,600)        #----->SyntaxError: positional argument follows keyword argument

#COMBINATION OFF *ARGS AND **KWARGS:
def think(*args,**kwargs):
    print(args,kwargs)
think()                       #------>() {}
think(1,2,3,4,5)              #----->(1, 2, 3, 4, 5) {}
think(1,2,3,4,x=10,y=19)      #----->(1, 2, 3, 4) {'x': 10, 'y': 19}

#ONLY POSITIONAL ARGUMENT(/):
def display(a,b,/,c):
    print(a,b,c)
display(10,20,c=30) #before / we need to pass positional argument while after we need to pass keyword argument or positional
display(a=10,b=20,60)      #---->SyntaxError: positional argument follows keyword argument

#ONLY KEYWORD ARGUMENT(*):
def fun(a,*,b,c):
    print(a,b,c)
fun(1,b=10,c=20)    #---->1 10 20
fun(a=200,b=300,c=700)    # -->200 300 700
fun(a=300,1,2)            #SyntaxError: positional argument follows keyword argument

#COMBINATION OF * AND /
def hii(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
hii(1,2,c=3,d=4,e=90)    #---->1 2 3 4 90
hii(a=10,b=20,c=3,d=4,e=10)     #TypeError: hii() got some positional-only arguments passed as keyword arguments: 'a, b'
"""
#return keyword
"""def hii():
   c='python'
   return c
a=hii()
print(a)

def py(a,b):
    return a+b,a-b,a*b
op=py(10,20)
print(op)"""



#PRACTICE

# 1.wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference
# def op():
#     a=int(input('Enter a:'))
#     b=int(input('Enter b:'))
#     if a>b:
#         return a+b
#     else:
#         return a-b
# c=op()
# print(c)

# 2.wap to check string is palindrome or not (take user input)
# def palindrome(a):
#     a=input('Enter the string:')
#     if a==a[::-1]:
#         print('Palindrome')
#     else:
#         print('Not palindrome')
# palindrome()

# 3.wap to return length of variable keywords arguments

# def variable(**kwargs):
#     print(len(kwargs))
# variable(a=20,b=20,c=90)

# # 5.waf to search for character in a given string and return corresponding index
# s = "coding part is done"
#
# def char():
#     a = input("Enter the character: ")
#     for i, j in enumerate(s):
#         if j == a:
#             return i
#     return "not found"
#
# c = char()
# print(c)

# 6.wap to squaring of the element in the given list
# l=[1,2,3,4,5]

# def squ(*args):
#     a = []
#     for i in args:
#         a.append(i**2)
#     return a
# l=[1,2,3,4,5]
# b=squ(*l)
# print(b)

# def squ(l):
#     a=[]
#     for i in l:
#        a.append(i**2)
#     return a
# b=squ([1,2,3,4,5])
# print(b)


# 7.wap to fetch last digit number

# def last():
#     a=input('Enter the number:')
#
#     print(a[-1])
# last()

# 8.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number
# def op():
#     a=int(input("Enter a number 1:"))
#     b=int(input("Enter a number 2:"))
#     c=int(input("Enter a number 3:"))
#     result=a+b
#     print(f'Addition of first two numbers:  {result}')
#     print(f'Substraction from the result of addition: {result-c}')
# op()


# # 9.wap to find square,cube,square root and cube root of a number
# def operations():
#     a=int(input('Enter a number:'))
#     return a**2,a**3,a**0.5,a**(1/3)
# print(operations())

# # 10.wap to check the given characters is alphabets or digit or special characters
#
# def identify():
#     a=input('Enter a character:')
#     if a.isdigit():
#         print('Number')
#     elif a.isalpha():
#         print('Alphabet')
#     else:
#         print('Special Character')
# identify()


# 11.wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable
# def sequence():
#     a=eval(input('Enter the iterable:'))
#     if isinstance(a,(list,tuple,str)):
#          return a[::-1]
#     else:
#          new_result=list(a)
#          new_result.append('mom')
#          return new_result
# print(sequence())

# 12.write a function to print the below output func("TRACXN",1)
#should print RCN
# def op(a,n):
#     b=a[1:len(a):2]
#     return b
# print(op("TRACXN",1))

# 13.write a function to print the below output
# func("TRACXN",0)
#should print TAX
# def func(a,n):
#     b=a[0:len(a):2]
#     return b
# print(func("TRACXN",0))

# 14.A function take variable number of positional arguments
   # as input. how to check if the arguments are more than 5.

# 15.waf to return a dictionary with characters and ascii value pair
#
# def func():
#     b={}
#     a=input('Enter the characters:')
#     for i in a:
#      b[i]=ord(i)
#     return b
# print(func())

# 16.waf to reverse a iterable if you are passing string or list or tuple else print type of the data
# def iterable():
#     a=eval(input('Enter the iterable:'))
#     if isinstance(a,(str,list,tuple)):
#         return a[::-1]
#     else:
#         return type(a)
# print(iterable())


# 17.wap to check if a given character is alphabet or digit or special character (without using inbuilt function).
# def identify():
#     a = input("Enter the character: ")
#     x = ord(a)
#     # A–Z → 65 to 90
#     # a–z → 97 to 122
#     if (x >= 65 and x <= 90) or (x >= 97 and x <= 122):
#         print("Alphabet")
#     # 0–9 → 48 to 57
#     elif x >= 48 and x <= 57:
#         print("Digit")
#     else:
#         print("Special Character")
# identify()

# 18.write a function to check the given number is prime or not
