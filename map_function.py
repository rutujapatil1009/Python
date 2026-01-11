"""
#Map:
-It is an inbuilt function
-Here we have to pass the element one by one from iterable to function.
-Function is nothing, but we can use lambda or normal map function.
-Map will give the output in object address format.
-To avoid object address we have to follow :
1)typecasting
or
2)looping.
-To avoid the repetition and avoid the lengthy process we can use map function.
-Syntax:
        map (function_name,iterable1,iterable2.....,iterable n)
-Here we can use any function name but without parenthesis.
-We can pass multiple iterables but the length of iterables should be equal or data loss can take place.
-Map is a keyword which cannot be changed as it is the inbuilt function.
-We can execute map in two ways by using function and lambda.
-Lambda is used to save the time.

"""
"""
#function(map)
x=[2,4,6,8,9]
def cube(i):
   return i**3
q=map(cube,x)
print(q)            #------><map object at 0x0000013B585B06D0>
print(list(q))      #------>[8, 64, 216, 512, 729]

#lambda with map

new=lambda x:x**3
print(map(new,x))
print(list(map(new,x)))      #------->[8, 64, 216, 512, 729]

#wapt concatenate two lists
#return
x=[1,2,3,4,5]
y=[1,2,3]
def adding(a,b):
    return a+b
new=map(adding,x,y)
print(new)      #----><map object at 0x000001FEECDA06D0>
print(list(new))  #--->[2, 4, 6]
#Here if the length of iterable is not equal data loss takes place as above

#print
def adding(a,b):
   print(a+b)
new=map(adding,x,y)
print(new)      #---->2,4,,6
print(list(new))     #--->[None, None, None]

#lambda 
k=lambda i,j:i+j
print(list(map(k,x,y)))       #------[2, 4, 6]

#waptd the length of words inn the list 
x=['abc','python','snap','chat']
def length(q):
    return len(q)
new=map(length,x)
print(list(new))    #---------->[3, 6, 4, 4]

l=lambda q:(len(q),q)
print(list(map(l,x)))     #------------->[(3, 'abc'), (6, 'python'), (4, 'snap'), (4, 'chat')]

#wapt convert the positive number to negative number
e=[1,2,-28,-9876,11]
def positive(b):
   return abs(b)
s=map(positive,e)
print(list(s))          #----->[1, 2, 28, 9876, 11]

l=lambda b:abs(b)
print(list(map(l,e)))        #------>[1, 2, 28, 9876, 11]"

#waptd the given output from the list
x=['hello','world','python','enter','joy']
# o/p=['hello@','world@','python@','enter@','joy@']

def add(a):
    return a+'@'
new=map(add,x)
print(list(new))        #-->['hello@', 'world@', 'python@', 'enter@', 'joy@']

w=lambda c:c+'@'
print(list(map(w,x)))   #------------>['hello@', 'world@', 'python@', 'enter@', 'joy@']"""


"""
#1)wap to square the numbers in the list
num=[1,2,3,4,5]
#function
def square(num):
    return num**2
new=map(square,num)
print(list(new))          #------->[1, 4, 9, 16, 25]

#lambda
w=lambda a:a**2
print(list(map(w,num)))      #----->[1, 4, 9, 16, 25]


# 2.wap to merge two list
a=[1,2,3]
b=[4,5,6]
#function
def adding(a,b):
    return a+b
new=map(adding,a,b)
print(new)
print(list(new))  #--->[5, 7, 9]

#lambda
k=lambda i,j:i+j
print(list(map(k,a,b)))  #---->[5, 7, 9]


#3)wap to convert number to string
x=[10,20,30,40]

w=lambda i:str(i)
print(list(map(w,x)))        #--->['10', '20', '30', '40']


#wap to print the length of the word
words=["Python","map","example","students"]

w=lambda i:(i,len(i))
print(list(map(w,words)))           #------------>[('Python', 6), ('map', 3), ('example', 7), ('students', 8)]

##wap to capitalize the word
words=["apple","banana","cherry"]
w=lambda i:i.capitalize()
print(list(map(w,words)))             #------------->['Apple', 'Banana', 'Cherry']

#wap to find check even and odd
num=[1,2,3,4,5,6]
odd=lambda a:a%2==0
print(list(map(odd,num)))             #------->[False, True, False, True, False, True]

#Absolute values
x=[-5,-2,0,3,7]
n=lambda x:abs(x)
print(list(map(n,x)))              #------------>[5, 2, 0, 3, 7]

#Concatenate strings with "*"
words = ["Hi", "Hello", "Python"]
add=lambda a:a+'*'
print(list(map(add,words)))           #---------->['Hi*', 'Hello*', 'Python*']

#Strip spaces from strings
words = ["  python ", " map ", " function  "]
a=lambda x:x.strip()
print(list(map(a,words)))            #------------>['python', 'map', 'function']

#.#Check palindrome words
words = ["mom", "python", "dad", "level"]
a=lambda x:x==x[::-1]
print(list(map(a,words)))          #--------->[True, False, True, True]

#Convert floats to integers
nums = [1.2, 3.7, 5.9]
a=lambda x:int(x)
print(list(map(a,nums)))         #--------->[1, 3, 5]

#wap to return list of name and length pair
n=['laptop','mouse','board','house','week']
a=lambda x:(x,len(x))
print(list(map(a,n)))           #-------->[('laptop', 6), ('mouse', 5), ('board', 5), ('house', 5), ('week', 4)]

##wap to return if the key is individual return its values else return its type
s={10:"ten","hai":"value",(1,2,3):"collection",1.2:"decimal"}

x=lambda i:s[i] if isinstance(i,(int,float,bool)) else type(i)
print(list(map(x,s)))          #-------->['ten', <class 'str'>, <class 'tuple'>, 'decimal']"""




