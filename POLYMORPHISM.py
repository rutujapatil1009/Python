"""
POLYMORPHISM:
-An object showing different behaviour at different stages of life cycle.
-Poly-Many
 Morphism-Forms

-Topics to be done:
1)Method overloading
2)Method overwriting
3)Operator loading
4)Duck typing

NOTE:
-We cannot achieve method overloading in python because python is a dynamic typed
language but can do it partially by using class name explicitly.
-We can do method overwriting by using Super function.

*Magic method/Dundar method:
-We can achieve operator overloading by using magic method.
-We use double underscore at the beginning and ending of the magic method.
  Eg: __init__
-In magic method operators will be present as given below:
+ -> __add__
- -> __sub__
* -> __mul__
/ -> __truedivision__
// -> __floordiv__
% ->  __mod__


"""
"""
#OPERATOR LOADING

class Total:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
         return self.a + other.a
        # print(self.a + other.a)

    def __str__(self):    #user friendly
        return f'{self.a}'

    def __repr__(self):   #developer friendly
        return f'Total {self.a}'
t=Total(10)
t1=Total(20)
print(t+t1)
# t+t1
x=t+t1
print(x)

print(repr(x))

class Test:
    def __init__(self, x):
        self.x = x

     # def __sub__(self, other):
     #     return self.x - other.x

    def __sub__(self, other):  #-->using class name
        return Test (self.x - other.x) #---><__main__.Test object at 0x00000166315B4F50>

    def __str__(self):
        return f'{self.x}'

    def __repr__(self):
        return f'{self.x}'
t=Test(20)
t1=Test(5)
print(t-t1)

a=t-t1
print(a)

print(repr(a))

class Product:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Product(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Product(self.x - other.x, self.y - other.y)
    def __mul__(self,other):
        return Product(self.x * other.x, self.y * other.y)
    def __truediv__(self,other):
        return Product(self.x / other.x, self.y / other.y)
    def __floordiv__(self,other):
        return Product(self.x // other.x, self.y // other.y)
    def __mod__(self,other):
        return Product(self.x % other.x, self.y % other.y)

    def __str__(self):
        return f'{self.x} and  {self.y}'


t=Product(10,20)
t1=Product(5,25)
print(f'Addition:{t+t1}')
print(f'Subtraction:{t-t1}')
print(f'Multiplication:{t*t1}')
print(f'Division:{t/t1}')
print(f'Floor Division:{t//t1}')
print(f'Modulus:{t%t1}')

class Data:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __gt__(self,other):  #--->greater than
        return (self.x > other.x, self.y > other.y)

    def __lt__(self,other): #--->less than
       return (self.x < other.x, self.y < other.y)

d=Data(10,5)
d1=Data(5,10)
print(d>d1)
print(d<d1)
"""
"""
DUCK TYPING:
-In duck type we do not focus on object and type we only focus on behaviour.


class Dog:
    def sound(self):
        print('bark')

class Cat:
    def sound(self):
        print('Meowww')

class Duck:
    def sound(self):
        print('Quack')

class Cow:
    def sound(self):
        print('hammaa')

def Animal(Q):
    Q.sound()

# d=Dog()
# x=Duck()
# c=Cow()
# c1=Cat()


# Animal(d)
# Animal(c)
# Animal(c1)
# Animal(x)

w=[Dog(),Cat(),Duck(),Cow()]
for i in w:
    Animal(i) 
"""

class Book:
    def read(self):
        print('Book reading')

class Newspaper:
    def read(self):
        print('Newspaper reading')

class PDF:
    def read(self):
        print('PDF reading')

class Dictionary:
    def read(self):
        print('Dictionary reading')

def Funny(k):
    k.read()

r=[Book(),Newspaper(),PDF(),Dictionary()]
for i in r:
    # Funny(i)  #duck type
    i.read()    #normal way


