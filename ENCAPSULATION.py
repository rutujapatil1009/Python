"""
ENCAPSULATION:
-Binding and merging the data in single unit.
-We cannot achieve 100% encapsulation becoz we don't know how private variable internally is stores i.e we
can't get true private attributes
-Access specifiers:(modifiers)
1)Public
2)Private
3)Protected

1)Public access specifiers:
-Before the variable if we don't pass any underscore it is known as Public access specifiers.
-Eg: ->a=100
     ->def spam():
        pass
-Here we can take any variable and method.
-We can use this anywhere we need to pass like inside the class and outside the class.

2)Protected access specifiers:
-Before the variable if we pass single underscore it is known as Protected access specifiers.
-Eg:  ->_a=100
      ->def _spam()):
         pass
-We can pass this inside the class while we can access it outside but according to convention rule we cannot pass it outside.

3)Private access specifiers:
-Before the variable if we pass double underscore it is known as Protected access specifiers.
-Eg: -> __a=100
      ->def __spam()):
         pass
-We have to always access it inside the class.

"""
"""
#PUBLIC METHOD
class Test:
    name='Ram'
    def spam(self):
        print(f'Person name is {self.name}')

t=Test()
# t.name='Rahul'
Test.name='Rahul'
print(t.name)
t.spam()
print(Test.name)

class Employee:
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    def Data(self):
        print(f'Employee name is {self.name} \n'
              f'Employee Salary is {self.salary}\n'
              f'Employee Id is {self.id}\n')

e=Employee('Rohit',25000,'R1')
# print(e.name) #accessing outside
# print(e.salary)
# print(e.id)
e.name='Virat'
e.Data()

#PROTECTED METHOD
# This is the illegal way to do modification
class Bank:
    _Account_holder_name='Virat'
    def _holder_information(self):
        print(f'Account holder name is {self._Account_holder_name}')

b=Bank()
b._Account_holder_name='Pravin'
print(b._Account_holder_name)
b._holder_information()

class Bank:
    def __init__(self,sal):
        self.sal=sal

    def _Amount(self):
        print(f'Amount is {self.sal}')
b=Bank(25000)
b._sal=5000
print(b._sal)
b._Amount()

# To modify the data outside in the protected access specifier we have three methods Getter(),Setter(),Deletter()
# Here it is not important to use this names always we can use any other name.But for easy understanding
# it is recommended to use these names.

#GETTER METHOD
class Account():
    def __init__(self,bank_name,loc):
        self.name=bank_name
        self.loc=loc

    def Getter(self):    #------>getting the values
        return self.name,self.loc

a=Account('SBI','PUNE') 
print(a.Getter())       #-->('SBI', 'PUNE')

#SETTER METHOD

class Account():
    def __init__(self,bank_name,loc):
        self.name=bank_name
        self.loc=loc

    def Getter(self):
        return self.name,self.loc

    def setter(self,name,loc):     #-------->setting the values
        self.name=name
        self.loc=loc

a=Account('SBI','PUNE')
print(a.Getter())
a.setter('ICICI','MUMBAI')
print(a.Getter())

#DELETTER METHOD
class Account():
    def __init__(self,bank_name,loc):
        self.name=bank_name
        self.loc=loc

    def Getter(self):
        return self.name,self.loc

    def setter(self,name,loc):     #-------->setting the values
        self.name=name
        self.loc=loc

    def Deleter(self):
        del self.name,self.loc

a=Account('SBI','PUNE')
print(a.Getter())
a.setter('ICICI','MUMBAI')
print(a.Getter())
a.Deleter()
print(a.Getter())

#PRIVATE METHOD

class Display:
    __x=1000

    def Demo(self):
        print(f'Variable value is {self.__x}')

d=Display()
d.Demo()
print(d._Display__x)
print(Display._Display__X)

class Student:
    def __init__(self,name,sub,marks):
        self.name=name    #-->public
        self._sub=sub     #-->protected
        self.__marks=marks  #-->private

    def Getter(self):
        return (f'Student name is {self.name} \n'
                f'Student subject is {self._sub}\n'
                f'Student marks is {self.__marks}\n')
    def Setter(self,name,sub,marks):
        self.name=name
        self._sub=sub
        self.__marks=marks

    def Deleter(self):
        del self.name,self._sub,self.__marks

x=Student('John','Smith',100)
print(x.Getter())
x.Setter('Abhi','Python','199')
print(x.Getter())
x.Deleter()
print(x.Getter())
"""
"""
Advanced property decorator used for modification:
@property ---> getter()
@method_name.setter ---> setter()
@method_name.deleter ---> deleter()
"""
"""
class Python:
    def __init__(self,student_count):
        self.count=student_count

    @property
    def Data(self):
        print(f'Total student count is {self.count}')

    @Data.setter
    def Data(self,count):
        self.count=count

    @Data.deleter
    def Data(self):
        del self.count

p=Python(120)   #------->getter
p.Data

p.Data=200      #------->setter
p.Data

del p.Data       #----->deleter
p.Data
"""


