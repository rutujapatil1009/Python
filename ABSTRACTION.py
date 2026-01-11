"""
ABSTRACTION:
-Abstraction is a hiding the complexity of the feature which will only be showing the required things to the end user.
-Things to learn:

1)Abstract method:
-When we don't know the implementation,but we still declare the method it refers to the abstract method.
-It is decorated with----> @abstractmethod
-@abstractmethod will be present inside the 'abc' module.
-Without importing the module if we call the method it wil show the name error.

2)Abstract class:
-When we don't know the implementation,but we still declare the partial class it refers to the abstract class.
-Declaration of Abstract class:
                      Class Test
                        pass
- It will be derived from 'ABC' class.
-If we derive it from the module then only it is known as Abstract class else it will act as a normal class.

-Difference between 'ABC' and 'abc':
ABC--->Class name
abc--->module name

3)Concrete method:
-If we want to work on abstraction we have to take help of inheritance.
-In parent class we have to always declaration while in child class we can do both implementation and declaration.
-The class where we do both declaration and implementation is known as concrete class same with the concrete method.
-We cannot create any object for parent class/abstract class because it is derived from abc class and we have
passed @abstractmethod.
"""


from abc import ABC, abstractmethod
"""
#case1
class Test(ABC):
    pass
t=Test()

#case2
class Test(ABC):
    def spam (self):
        print("Spam")
t1=Test()
t1.spam()

class Test2:
    @abstractmethod
    def demo(self):
        print("Demo")

#case3
.
y=Test2()
y.demo()

class Hero(ABC):
    @abstractmethod
    def display(self):
        print('Display method')
h=Hero()
h.display()   #TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'display'
"""
"""
class Student(ABC):
    
    @abstractmethod
    def student_name(self,name):
        pass
    
    @abstractmethod
    def student_marks(self,marks):
        pass
    
    @abstractmethod
    def student_clg_name(self,clg_name):
        pass

class Student_info(Student):

    def student_name(self, name):
        print(f'Student name: {name}')
        
    def student_marks(self,marks):
        print(f'Student marks: {marks}')
        
    def student_clg_name(self, clg_name):
        print(f'Student clg name: {clg_name}')
        
i=Student_info()
i.student_name('Ravi')
i.student_marks(80)
i.student_clg_name('Pyspiders')

class Account_details(ABC):

    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

class Account(Account_details):
    def __init__(self,Account_holder_name,balance,Bank_name):
        self.Account_holder_name = Account_holder_name
        self.balance = balance
        self.Bank_name = Bank_name

    def balance(self):
        print(f'Total balance: {self.balance}\n'
              f'Account holder name: {self.Account_holder_name}\n'
              f'Bank name: {self.Bank_name}\n')

    def deposit(self,amount):
        print(f'Before deposit: {self.balance}')
        self.balance += amount
        print(f'After deposit: {self.balance}')

    def withdraw(self,amount):
        print(f'Before withdraw: {self.balance}')
        self.balance -= amount
        print(f'After withdraw: {self.balance}')

d=Account('Praveen',3000,'icici')
print(f'Account holder name: {d.Account_holder_name}\n'
      f'Bank name: {d.Bank_name}\n'
      f'Account balance: {d.balance}')
d.deposit(10000)
print(f'After deposit: {d.balance}')
d.withdraw(5000)
print(f'After withdraw: {d.balance}')

class Institute(ABC):

    @abstractmethod
    def Institute_name(self):
        pass

    @abstractmethod
    def Joining_date(self):
        pass

    @abstractmethod
    def course(self):
        pass

    @abstractmethod
    def attendance(self):
        pass

    @abstractmethod
    def fees(self):
        pass

class Information(Institute):

   def __init__(self,Institute_name,Joining_date,course,attendance,total_fees,first_installment,second_installment,additional_course):
      self.Institute_name = Institute_name
      self.Joining_date = Joining_date
      self.course = course
      self.attendance = attendance
      self.total_fees = total_fees
      self.first_installment = first_installment
      self.second_installment = second_installment
      self.additional_course = additional_course
   def Institute_name(self):
       print(f'Institute name: {self.Institute_name}')

   def Joining_date(self):
       print(f'Joining date: {self.Joining_date}')

   def course(self):
       print(f'Course: {self.course}')

   def attendance(self):
       print(f'Attendance: {self.attendance}')

   def fees(self):
       print(f'Fees: {self.fees}')

   def first_installment(self):
       print(f'First installment: {self.first_installment}')

   def second_installment(self):
       print(f'Second installment: {self.second_installment}')

   def additional_course(self):
       print(f'Additional course: {self.additional_course}')

i=Information('Pyspiders','01-july-2025','Python full stack+DA','75%',
              30000,15000,15000,'SQL')

print(f'Institute name: {i.Institute_name}\n'
      f'Joining date: {i.Joining_date}\n'
      f'course: {i.course}\n'
      f'attendance: {i.attendance}\n'
      f'Total_fees: {i.total_fees}\n'
      f'First installment: {i.first_installment}\n'
      f'second installment: {i.second_installment}\n'
      f'additional_course: {i.additional_course}')

"""


