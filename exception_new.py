"""
#Assert:
-Syntax:
     assert condition message
-Here message is optional
-Here if our statement is satisfied the program will continue the execution else it will  throw the assertion error.
-It is one of the debugging tool
"""
"""
x=-100
assert x>0 ,'Greater than 0'
print('working')
"""
l=[1,2,3,4]
assert len(l)>0
print('list have some elements')
"""
#User defined error:
-SYNTAX:
    class userdefinederror(base exceptionn/exception):
       pass/...
       
-If we want to use our own exception we need to use raise keyword.
-Here pass and class are keywords.




"""
"""
class NegativeError(BaseException):
    pass

def Demo(s):
    if s>0:
        print("positive")
    else:
        raise NegativeError

Demo(-50)

class Length_error(Exception):
    ...
def password(s):
    if len(s)>=6:
        print('Valid password length')
    else:
        raise Length_error
password('12')

class PalindromeError(BaseException):
    pass
def display(r):
    if r==r[::-1]:
        print("Palindrome")
    else:
        raise PalindromeError
try:
 display('money')
except:
    print("Something went wrong")"""


"""
1)WHAT ARE THE DIFFERENCES BETWEEN ERROR AND EXCEPTION
2)WHAT ARE TYPES OF ERRORS
3)WHAT ARE DIFFERENCES BETWEEN EXCEPTION AND EXCEPTION HANDLING
4)WHAT ARE TRY AND EXCEPT BLOCKS
5)TYPES Of EXCEPT BLOCK
6)NESTED TRY AND EXCEPT BLOCK
 7)difference between assert and raise
"""

"""
class PositiveError(BaseException):
    pass

def Demo(s):
    if s<0:
        print("Negative")
    else:
        raise PositiveError

Demo(50)

class mobile_num_error(BaseException):
    pass
def num(s):
    if len(s)==10:
        print('Data stored')
    else:
        raise mobile_num_error
num('123456789')"""


