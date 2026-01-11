"""
#DECORATORS:
-Adding the functionality to the main function without modifying the main function is known as decorators.
-Decorators are achieved by using nested function.
They are used to monitor the task, for authorization.
-Syntax:
        def outer(func):      ---------2
           def inner(*args,*kwargs):    ------6
           #before calling the main function    ---7
           func(*args,**kwargs)   ---------8
        return inner         ----------3

        @outer              ----1
        def main(parameter):    #main==inner add     -----4  -------9
            stmt
            return stmt   ----10
        main(argument)         ------5


-@outer is a function calling used in decorators
-It will consider the name and memory address of function below it as an argument.

*Types of decorators:

1)User defined decorators:The decorators which are created to perform specific task which cannot be
                         performed by the pre-defined decorators.We use them when we are not satisfied
                          with pre-defined decorators.

2)Pre defined decorators:The decorators which are already developed while creation of the software
                         are known as Pre defined decorators.The functionality of these decorators
                         are already defined in the software by the developer.

-Steps:
1)It should be nested function.
2)Main function will call the outer function.
3)Outer function will accept one i.e main function address
4)It will allocate the inner function address.
5)Outer function will return inner function address.
6)Inner function address will store into main function(Those who we call outer function)
7)It will call main function,but internally it will call inner function and accept args of main function.
8)After that it will call func i.e main function
9)It will accept the arguments for main function and perform the operations.
10)It will return the output.
"""
"""
def abhi(func):
    def neha(*args,**kwargs):
        print('I am performing Addition')
        func(*args,**kwargs)
        print('Addition performed')
    return neha
@abhi
def add(a,b):
    print(a+b)
add(22,11)

def check(func):
    def num(*args,**kwargs):
        print('Checking for greater number')
        func(*args,**kwargs)
        print('Greater number found')
    return num
@check
def subs(a,b):
    if a>b:
        print(a-b)
    else:
        a,b=b,a
        print(a-b)
subs(22,33)"""

# wap to perform decoration operations where positional value of the argument will give you the sum
# of the elements and keyword argument will return you the length of the dictionary

def decorator(func):
    def wrapper(*args, **kwargs):
        if args:  # If positional arguments are given
            print("Sum of positional arguments:", sum(args))
        if kwargs:  # If keyword arguments are given
            print("Length of dictionary:", len(kwargs))
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_func(*args, **kwargs):
    print("Original function executed!")
def decorator(func):
    def wrapper(*args, **kwargs):
        if args:  # If positional arguments are given
            print("Sum of positional arguments:", sum(args))
        if kwargs:  # If keyword arguments are given
            print("Length of dictionary:", len(kwargs))
        return func(*args, **kwargs)
    return wrapper

9

