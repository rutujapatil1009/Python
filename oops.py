"""
#OOPs:
-To represent real world object to software world.
-Why do we use OOPs:
1)Easily store the data
2)Easily access the data
3)Code reusability
4)Code maintenance


##CLASS:
-It is nothing but combination of properties and attributes.
-It is nothing but blueprint,design,plan,MODEL for an object.
-Syntax:
   class class-name :
      pass

##Object:
-Physical existence of a class.
-With the help of a single class we can create multiple object.
-Syntax:
      new_vn = class_name():


-Whenever we create class it has 3 things:
1)class variable:It is a variable which is present inside the class
2)method:function inside the class
3)constructor


"""
"""
#How to create empty class?
class Python:
    pass
#How to create object?
a=Python()
print(a)              #---------><__main__.Python object at 0x000002592AD66F90>

x=Python
print(x)             #---------><class '__main__.Python'>

#How to  create class variable?
class Student:
    '''STUDENT INFORMATION'''
    name='kiran'
    score=98
    reg_no=121

#Accessing the variable in class
#----->with using object
a=Student()
print(a.name)
print(a.score)
print(a.reg_no)

#---->with using class name
print(Student().name)
print(Student().score)
print(Student().reg_no)

#---->To print doc(description of the class)string
s=Student()
help(Student())  #----->it gives us whole view of the class
print(Student().__doc__)       #------>It gives us only title
print(Student().__dict__)   #------->every data stored will be present in the format of key and value pairs.
"""

"""
-POINTS TO REMEMBER:
1)If we do modification in main class it will affect all the objects of that class.
2)If we do modification in any of the object it won't affect main class or other objects.
-When we do modification in object for a particular variable connection between that variable of object and 
main class will get lost .
3)If we again do modification in main class it will not affect the object in which we have separately done 
modification of that object.
"""
"""
class Python():
    name='rahul'
    age=25

object1=Python()
object2=Python()

print('BEFORE MODIFICATION')
print(Python.age)
print(object1.age)
print(object2.age)

print('Modification in main class')
#syntax for modification in main class=class_name.v_n=value
Python.age=30
print(Python.age)
print(object1.age)
print(object2.age)

print('Modification in obj 1')
print('Before modification in obj 1')
print(Python.age)
print(object1.age)
print(object2.age)

print('After modification in obj 1')
#syntax for modification in object=object.v_n=value
object1.age=35
print(Python.age)
print(object1.age)
print(object2.age)

class Student():
    score=100
    subject='python'

data1=Student()
data2=Student()

print('BEFORE MODIFICATION')

print(Student.subject)
print(data1.subject)
print(data2.subject)

print('After modification in Main class')

Student.subject='SQL'
print(Student.subject)
print(data1.subject)
print(data2.subject)

print('Modification in data1')

data1.subject='PowerBI'
print(Student.subject)
print(data1.subject)
print(data2.subject)

print('Again modification in main class')
Student.subject='Data analysis'
print(Student.subject)
print(data1.subject)
print(data2.subject)
"""

"""
Methods:
-A function inside the class.
-Types of method:
1)instance method
2)class method
3)stat method

#instance method:
-Here instance is nothing but object.
-It is a method it will accept first argument of an object address.
-Syntax:
     class class_name:
         def method_name(self):
             statement
     
     new v_n = class_name()
-It is same as normal function when we call it outside the method
-In normal function it is not mandatory to pass any parameter if we don't
pass it will be empty while in instance method it will take SELF as a default 
parameter even if we don't pass any.
- The self is always pointing to object   


"""
"""
#how to access class variable in instance method
#1)by using class name
#2)by using object

#modification in main class
class Amazon():
    product='Iphone'
    price=80000
    color='White'
    add='Pyspiders_deccan'

    def mobile_information(self):

        print(f'My product name is {Amazon.product} and my product price is {Amazon.price} and color is'
              f' {Amazon.color} and address is {Amazon.add}')       #-------->by using object

a=Amazon()
Amazon.price=50000
Amazon.color='Rose gold'
a.mobile_information()

#When we call variables by using class name we have to do modification using class name
"""
"""
#modification in object
class Amazon():
    product='Iphone'
    price=80000
    color='White'
    add='Pyspiders_deccan'

    def mobile_information(self):

        print(f'My product name is {self.product} and my product price is {self.price} and color is'
              f' {self.color} and address is {self.add}')       #-------->by using object

a=Amazon()
a.add='Deccan'
a.mobile_information()
#When we call variables by using object we have to do modification using object only
"""
"""
class student():                                                                           
    name='Rutu'
    age=21
    subject='python'
    yop=2026

    def student_information(self):
        print(f'The name of student is {self.name} having age {self.age} years old '
              f'and the course included is {self.subject} and year of pass out is {self.yop}')
a=student()
a.student_information()

#modification in main class using object
class student():
    name='Rutu'
    age=21
    subject='python'
    yop=2026

    def student_information(self):
        print(f'The name of student is {self.name} having age {self.age} years old '
              f'and the course included is {self.subject} and year of pass out is {self.yop}')

a=student()
a.name='shravani'
a.student_information()


#modification in main class using class name
class student():
    name='Rutu'
    age=21
    subject='python'
    yop=2026

    def student_information(self):
        print(f'The name of student is {student.name} having age {student.age} years old '
              f'and the course included is {student.subject} and year of pass out is {student.yop}')

a=student()
student.yop=2025
a.student_information()
"""
"""
#CLASS METHOD

# class Test:
#     @classmethod
#     def spam(cls):
#         print(cls)
#     def demo(self):
#         print(self)
#
#
# t=Test()
# print(t)
# t.demo()
# t.spam()



class Demo:
    @classmethod
    def spam(cls):
        print(cls)
d=Demo()
print(d)  #<__main__.Demo object at 0x00000238BEE692B0>
d.spam()  #<class '__main__.Demo'>

print("********************************************************")
class Test:
    def Display(self):
        print(self)  #<__main__.Test object at 0x000001E9DFE1AF90>
t=Test()
print(t)   #<__main__.Test object at 0x000001E9DFE1AF90>
t.Display() 

class School():

    @classmethod
    def display(cls):
        print(cls)          #-------><class '__main__.School'>
        print('Display the class')         #------->Display the class

s=School()
print(s)             #--------><__main__.School object at 0x000001E7EAC770E0>          
s.display()
School.display()

#MODIFICATION FOR CLASS NAME OUTSIDE

class School:
    name='Qspiders'

    @classmethod
    def change_school_name(cls):
        print(f'My school name is {School.name}')

    @classmethod
    def display(cls):
        def school_name(cls):
            print(f'My school name is {cls.name}')

w=School()
# School.name='PYspider'
w.name='Jspiders'
w.change_school_name()
"""

"""
DIFFERENCE BETWEEN CLASS AND INSTANCE
-INSTANCE IS NOTHING BUT OBJECT
-METHOD IT WILL ACCEPT FIRST ARGUMENT AS AN OBJECT ADDRESS

-ANY METHOD USED TO DECORATE
"""