"""
CONSTRUCTOR:
-It is one of the special member inside the class.
-We  have use magic method __init__ for defining the constructor.We cannot use any other name for constructor.
-the object always point to the self here.
-Syntax:
  class class_name :
     def __init__(self ):
        statement
  new_vn = classname()
  classname.__init__(new_vn)

"""
"""
class Student:
    def __init__(self):
        print(self)         #----------><__main__.Student object at 0x000002139CD36F90>
        print("Student Class")

s=Student()
print(s)    #---------------><__main__.Student object at 0x000002139CD36F90>
# whenever we create any new variable constructor is called automatically



class Test:
    def __init__(self):
        print('CONSTRUCTOR CLASS')

    def demo(self):
        print('Demo Class')

t=Test()
t.demo()

print('through class name')
Test.__init__(t)
Test.demo(t)
"""

"""
Types of constructor:
1)Default constructor:
-The constructors which are working internally and which are not visible are known as default constructors.
-Eg:instance method

2)User defined constructor:
-The constructor which is created by user using the syntax is known as user defined constructor.
-Here parameters is nothing but variable.
-There are two types of user defined constructors:

1)With parameterized constructor
-Here we need to pass parameters.

2)Without parameterized constructor


"""
"""
# default constructors
class Test:
    def demo(self):
        pass
object=Test()
print('Object operation done properly')

class Display:
    def spam(self):
        print('spam')
s=Display()         #----internally it will be s.__init__()
s.spam()


class Product:
    def __init__(self):
        name='Pen'
        price=15
        print(f'Product name is {name} and price is {price}')

p=Product()
Product.__init__(p)

# instance variable syntax:self.new_vn=value
# The above syntax can be used in instance variable and constructor
# Instance variable will always point to object
# Here if we have to do modification we have to do it with the help of object bcoz instance variable always points to object.

class Product:
    def __init__(self):
        self.name='Pen'
        self.price=15
        print(f'Product name is {self.name} and price is {self.price}')

p=Product()
Product.name='Marker'        #-->it won't affect while doing it through class
p.name='Marker'

# This example is recommended

class Bank:
    def __init__(self,bal):
        self.bal=bal

    def deposit(self,amt):
        self.bal += amt
        print(f'Total amount after deposit is {self.bal}')

b=Bank(1000)
Bank.bal=2000   #------->We cannot do modification through class
print(b.bal)
b.deposit(500)    #--------->We can do modification through object

#without parameterised eg

# drawback=here we can create multiple object we will always get same output.

class Bank:
    def __init__(self):
        self.Account_holder_name='praveen'
        self.Account_number='123456789'
        self.Bal=1000
        self.bank_name='SBI'
        self.IFSC_code='SBIN009'
        self.Branch='Deccan'

        print(f'My bank name is {self.bank_name} and account holder name is '
              f'{self.Account_holder_name} and account number is {self.Account_number}'
              f' and bank balance is {self.Bal} and ifsc code is {self.IFSC_code} and my branch is {self.Branch}')
b=Bank()
print()


class Student:
    def __init__(self,name,subject,marks,id):
        self.name=name
        self.subject=subject
        self.marks=marks
        self.id=id
        # here in the place of new variable name we can pass anything but in value place of value we have to
        # pass the same parameters which we passed with self

        print(f'My name is {self.name} and my subject name is {self.subject} and my marks are {self.marks} and my id is {self.id}')

s=Student('Rutu','python',45,'A1')
# My name is Rutu and my subject name is python and my marks are 45 and my id is A1
print()
s1=Student('ABC','SQL',55,'X1')
# My name is ABC and my subject name is SQL and my marks are 55 and my id is X1
print()
s2=Student('XYZ','powerbi',50,'b1')
# My name is XYZ and my subject name is powerbi and my marks are 50 and my id is b1

# Calling through class name will give error
Student.__init__('abhi','manual',66,123)
# TypeError: Student.__init__() missing 1 required positional argument: 'id'


class Flipkart():
    def __init__(self,product,price,product_id,ratings,stock,color):
        self.x=product
        self.y=price
        self.z=product_id
        self.q=ratings
        self.t=stock
        self.s=color

    def Product_details(self):
        print(f'My product name is {self.x} and my product price is {self.y} and product id is {self.z}')

    def Extra_info(self):
        print(f'My product current ratings are {self.q} and current stock is {self.t} and color is {self.s}')

    def both_method_info(self):
        self.Product_details()
        self.Extra_info()

f=Flipkart('Iphone17','130000','A23456','1',10,'pink')
f.Product_details()  #--->My product name is Iphone17 and my product price is 130000 and product id is A23456
f.Extra_info()   #--->My product current ratings are 1 and current stock is 10 and color is pink
f.both_method_info()
# ----->My product name is Iphone17 and my product price is 130000 and product id is A23456
# My product current ratings are 1 and current stock is 10 and color is pink
"""
'''
class Information:
    def __init__(self,l,w):
        self.l=l
        self.w=w
        self.area=self.l *self.w
        
#here I'm doing operation in constructor
    
    def Area_show(self):
        print(f'Total length is {self.l} and width is {self.w} and total area value is {self.area}')

i=Information(10,5)
i.Area_show()

class Student:
    name='ABC'
    def __init__(self,marks,id):
        self.m=marks
        self.i=id
        print(f'Total marks id is {self.i} and student id is {self.m}')  #-->Total marks id is A1 and student id is 55
        # here I want to access class variable into the constructor
        print(f'By using class name {Student.name}')   #-->By using class name ABC
        print(f'By using object {self.name}')  #-->By using object ABC
        print(f'By using instance object accessing class variable {self.__class__.name}') 
        #-->By using instance object accessing class variable ABC
        print(self.__class__)
s=Student(55,'A1')  #--><class '__main__.Student'>

#first method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Grade(self):
        return 'pass' if self.marks > 50 else 'fail'
s = Student('ram', 35)
print(s.Grade())

#second method
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.result=self.Grade()
        print(self.result)

    def Grade(self):
        return 'pass' if self.marks>50 else 'fail'
s=Student('ram',35)

class Display:
    def __init__(self):
        return 10
d=Display()
#--->TypeError: __init__() should return None, not 'int'
# If we use return keyword directly inside the constructor it will give us typeerror.
# If we want to use we can use it in any other instance method.

class Car:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a,b)

    def __init__(self,a,b,c):
        print(a,b,c)

# c=Car(10)     #------>TypeError: Car.__init__() missing 2 required positional arguments: 'b' and 'c'
# c1=Car(10,20)   #----->TypeError: Car.__init__() missing 1 required positional argument: 'c'
c2=Car(10,20,30)   #------->10 20 30
"""
Method overloading:
-Developing a multiple methods with a same name and variation in argument list means either datatype or order of occurrence.
-Here also we cannot achieve 100% method overloading we have to use default value to achieve it completely.
"""
class Car:
    def __init__(self,a):
        print(a)          #---------->10 0 0

    def __init__(self,a,b):
        print(a,b)        #-------->10 20 0

    def __init__(self,a=0,b=0,c=0):
        print(a,b,c)          #------>10 20 30
c=Car(10)
c1=Car(10,20)
c2=Car(10,20,30)
'''

class Car:
    def __init__(self):
        self.name='BMW'
        self.price=1000000
        print(f'car name is {self.name} and price is {self.price}')
    def Modification(self):
        self.name='Audi'
        print(self.name)

c=Car()
c.name='Audi'
print(c.name)
c.Modification()
