"""
#Exception handling:
-Exception refers to problem or error.
-It refers to problem-solving.
-Unwanted and unexcepted  event which happens suddenly while execution are needed to be handled that process
is known as exception handling.
-Exception handling is a process to handle the  error by the help of try and except block.

-Types of errors:
1)Syntax error:
-They can't be handled
-These error occurs due to mistake of a user.

2)Runtime error:
-They can be handled with the help of try and except block.
-It usually occurs during the execution of the program.

-Runtime error types:
1)Predefined:
-These are inbuilt error whose names cannot be changes by the user.
-Eg:index error,value error,key error,Type error

2)User defined:
-Here we only create an error with the help of RAISE keyword.
-Eg:Metro error,pen error,phone error,positive error.

#Try and except block:
-When the code in try block have any error it will move towards the except block and execute it.
-If we don't have any error in try block except block won't be executed.
-If we write try block it is mandatary to write except block.

#Types of except block:
1)Default except block :
-It is used when we don't know what kind of error it will occur during the execution of the program.
-Syntax:
try:
   Risky code/errorLine
except:
   statement/problem-solving

2)
"""
"""
x=100
y=0
try:
  print(x/y)
except:
    print("Error done")

s=(1,2,3,4,5,6)
try:
   print(s[14])
except:
    print("Problem solved")"""


# try:
#     a=int(input('S:'))
#     b=int(input('Y:'))
#     result=a/b
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero")


# try:
#     a=int(input('A:'))
#     result=a
#     print(result)
# except ValueError:
#     print("Invalid integer")








