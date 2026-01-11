"""
#Generator:

-Generator is  a type of function.
-It will return sequence of element one by one.
-Generator is also known as lazy iterator.
-Iterator-It will generate one by one value.
-We use generator if we want to save memory because in function we can't save memory.
-In generator we use yield keyword instead of return.
-Here in generator we can use multiple yield keyword.
-Yield keyword pause(hold) the execution.
-
               GENERATOR --->sequence of element
                   |
               Yield keyword

-Syntax:
     def generator_name(parameter):       --------->Generator declaration
          statement
          yield data1
          yield data2                     --------->block of code
          yield data3
     new_var=generator_name(argument)     --------->generator calling
     print(new_var)

-If we directly execute generator it will give us generator object address,to avoid this we have 3 types:
    1)typecasting
    2)next()-it will accept generator object.
             -Syntax:  next(generator_object)
             -Generator object is a variable where we store complete program.
    3)looping



"""
"""
def generator_name():
    yield 'hii'
    yield 'hello'
    yield 'bye'
gen=generator_name()
print(gen)   #-------------><generator object generator_name at 0x000001A673685D20>

#typecasting:
print(list(gen))     #['hii', 'hello', 'bye']

#looping:
for i in gen:
    print(i)    #---->hii,hello,bye

#next():
print(next(gen))      #----->hii
print(next(gen))      #----->hello
print(next(gen))      #----->bye
print(next(gen))      #------>StopIteration

#function
def rt(l):
    a=[]
    for i in l:
      a.append(i**0.5)
    return a
d=rt([25,16,49,81,9,16])
print(d)
#generator
def rt(l):
    a=[]
    for i in l:
      a.append(i**0.5)
    yield a
d=rt([25,16,49,81,9,16])
print(next(d))

#fuction
def fun(l):
    for i in l:
        if isinstance(i,complex):
           print(i)
fun([1,2,3,4,4+5j])

#generator
def fun(l):
    for i in l:
        if isinstance(i,complex):
             yield(i)
comp=fun([1,2,3,4,4+5j])
print(next(comp))

def op(a,b):
    yield a+b
    yield a+b
    yield a*b
    yield a/b
b=op(10,20)
print(next(b))
print(next(b))
print(next(b))
print(next(b))"""

# d=[1,2,3,4,5]
# print([i for i in d if i%2==1])
#
# print([i for i in d])
#
# print([i**2 if i%2==0 else i**3 for i in d])
#
# print((i for i in d  if i%2==1))    #--------->generator expression

#
# def cube(a):
#     for i in range(1, a + 1):
#         yield i**3
#
# a = int(input('Enter N: '))
# for value in cube(a):
#     print(value)

# wap to convert value in add ,sub,multiply
# def func(a,b):
#     yield a+b
#     yield a-b
#     yield a*b
# print(list(func(30,10)))


#wap to generate square of numbers in given list
# l=[2,5,7,8,9]
# def op(l):
#     for i in l:
#         yield i**2
# print(list(op(l)))   #[4, 25, 49, 64, 81]

#wap to generate only the string with odd length in the given list
# words=["king","queen","jack","kohli","hero"]
# def snap(words):
#     for i in words:
#         if len(i)%2==1:
#             yield i
# print(list(snap(words)))   #['queen', 'kohli']

#wap to generate only the numeric value in list
# item=["hello",23,85.6,[4,2,9],True,3+5j]
# def func(item):
#     for i in item:
#         if isinstance(i,(int,float,complex,bool)):
#             yield i
# print(list(func(item)))   #[23, 85.6, True, (3+5j)]

#wap to generate a list if it is individual data type reverse it else keep it as it is
# a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]
# def rev(a):
#     for i in a:
#         if isinstance(i,(int,float,complex,bool)):
#             yield str(i)[::-1]
#         else:
#             yield i
# print(list(rev(a)))  #['good', '54', [1, 2], '6.87', (4, 5), ')j7+8(', {9, 7}, 'eslaF', {'a': 75}]

#wap to return an iterator having the words and its length pair as a dictionary inside the tuple.









