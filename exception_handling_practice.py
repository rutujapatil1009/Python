# UNWANTED AND UNEXPECTED EVENT OCCURED WHILE HANDLING THE PROGRAM

# -----------------------------------------------------------------------------------

# EXPECTION HANDLING IS THE PROCESS OF HANDLING THE ERROR BY THE HELP OF TRY AND EXPECT BLOCK

# ---------------------------------------------------------------------------------------------------

# ALL LANGUAGES COMMON ERROS

# ---------------------------------

# 1:-  SYNTAX ERROR:--- (HUMAN ERROR)- WE CANT HANDLE IT WE HAVE TO MANUALLY FIX IT

'''

for i in range(1,10,1) # no colon means human error
print(i)
'''
# no types here

# 2:--- RUNTIME ERROR

# two types in Runtime error


# 1.Predefined Error:-->> inbuilt error we cant change the error name also

# example:- value error,index error,key error, type error

# -------------------------------------------------------------------------------------------

# 2.UserDefined Error:---->> we are the user we only creating the error by the help of raise keyword

# example:-_>> Metro Error, Pen Error Phone Error, Raise Error


# TRY_ EXCEPT BLOC


# TRY BlocK

# ----------------------------------------------------------

# WHILE EXECUTION OF THE PROGRAM WHICH LINE IS SHOWING THE ERROR
# THAT LINE WE HAVE TO MENTION IN TRY BLOCK


# EXCEPT BLOCK
# -----------------------------

# TYPES OF EXPECT BLOCK

'''
1.DEFAULT EXPECT BLOCK:-- WHEN WE DONT KNOW WHAT KIND OF ERROR IT WILL OCCURED THEN WE TO GO FOR DEFAULT EXPECT BLOCK

#-----------------------------------------------------

#SYNTAX:--->

try:
 Risky Code/Error line

except:
   statement/problem solving

'''

# example

'''
e={12:22,34:22,100:200,300:400}
try:

   print(e[1400])

except:

    print("error handled")
'''

# ------------------------------------------------------------------------------
'''  
# 2.SPECIFIC EXPECT BLOCK:-- When We KNOW THE WHAT KIND OF ERROR IS OCCURING 
# THAT TIME WE HAVE TO GO FOR SPECIFIFC EXPECT BLOCK


#SYNTAX:-->

try:
    Risky Code/Error line

except Error_Name: ------------------------------------ # MAIN DIFF IS YOU HAVE TO JUST MENTION THE ERROR NAME
   statement

'''
'''
a=10
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("DivisionError_Handled") #-------------------  2.SPECIFIC EXPECT BLOCK HAVE TO MENTION THE DEFAULT EXPECT METHOD
'''

# ---------------------------------------------------------------------------------

# 3.MULTIPLE EXPECT BLOCK


# BY USING SINGLE TRY BLOCK WE CAN EXECUTE MULTIPLE EXCEPT BLOCK

# ONLY SPECIFIC BLOCK WITH THAT ERROR NAME THAT JAS OCCURED WILL EXECUTE

# BY USING SINGLE TRY BLOCK WE CAN EXECUTE MULTIPLE EXCEPT BLOCK

# MANDATORY TO WRITE THE ERROR NAME LIKE SPECIFIC EXPECT BLOCK

# ----------------------------------------------------------
# SYNTAX

'''
s=[1,2,3,4]
try:
 s.upper(45)
except AttributeError:
    print("AttributeError_Handled")
except TypeError:
    print("TypeError_Handled")
except NameError:
    print("NameError_Handled")
except IndexError:
    print("IndexError_Handled")
except SyntaxError:
    print("SyntaxError_Handled")
except ZeroDivisionError:
    print("ZeroDivisionError_Handled")
except ValueError:
    print("ValueError_Handled")
'''

# 4.GENERIC EXPECT BLOCK

"""
                    Generic except Block:--->
--------------------------------------------------------------------------
* Handled all kind of error

*In Generic except Block we can find the reason for error

#syntax:-->
try:
    Risky_Code/Error_Line

except Exception as msg:
    statement
    print(msg)

"""
s="Good Morning"
'''
try:
    print(s.append())

except:
    print("error Handled")


try:
    print(s.append())

except AttributeError:
    print("AttributeError Handled")

Ex-->1
try:
    print(s.append())

except Exception as msg:
    print("Error Handled")
    print(msg)


s=11
d=0

try:
    print(s/d)
except Exception as x:
    print(x)


s=11
d=0

try:
    print(s/d)
except BaseException as x:
    print(x)
'''


#Combination of try ,except and else block

#syntax:-->
"""
try:
    RiskyCode

except:
    statement

else:
    statement        

a=11
b=3
try:
    print(a/b)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

print()

try:
    print(a/c)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

"""

'''
#combination of try,except,else and finally block
a=11
b=3
try:
    print(a/c)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

finally:
    print("Code_Loading.......")

print()

a=11
b=3
try:
    print(a/b)   #print(11/3)

except:
    print("error done")

else:
    print("No error")

finally:
    print("Code_Loading.......")

'''

# nested try and except block

"""

try:
    Error_line

    try:
        Error_line

    except Error_name:
        statement

except Error_name:
        statement               

s="Morning"

try:
    print(s.upper())
    try:
        s.clear()
    except AttributeError:
        print("AttributeError Handled")
except:
    print("No error")

print()

try:
    s.clear()
    try:
        print(s.upper())
    except:
        print("No error")
except AttributeError:
    print("AttributeError Handled")

"""

'''
#in nested try and except block we are using else and finally block
a={1:2,67:89,100:200}
try:
    print(a[800])
    try:
        print(a[1])
    except:
        print("No error")
except KeyError:
    print("Key error")
else:
    print("error---??????")
finally:
    print("no error guys")

print()

a={1:2,67:89,100:200}
try:
    print(a[1])
    try:
        print(a[555])
    except KeyError:
        print("Key error")
    else:
        print("error---??????")
    finally:
        print("no error guys")
except:
    print("cool")
else:
    print("as of now no error")
finally:
    print("its working")

'''

#userdefined error format


'''
class NegativeError(BaseException):
    pass
def Demo(s):
    if s>0:
        print("its a +ve number")
    else:
        raise NegativeError
Demo(50)
Demo(-50)
'''

'''

class Length_error(Exception):
    ...

def Password(s):
    if len(s)>=6:
        print("valid Password length")
    else:
        raise Length_error
Password('1234567')
Password('12345')

'''

'''
class PalindromeError(BaseException):
    pass

def Display(r):
    if r==r[::-1]:
        return True,r
    else:
        raise PalindromeError
z1=Display("Python")
print(z1)
'''

'''
d=[1,2,3,4]
try:
    print(d[100])
except:
    print("error Handling")
'''

'''
class PalindromeError(BaseException):
    pass
def Display(r):
    if r==r[::-1]:
        print("its a palindrome")
    else:
        raise PalindromeError
try:
    Display("Python")
except:
    print("error Handling")

'''



#assert format


"""
assert:-->
syntax:--> assert condition message

x=10
assert x>0
print("working")

print()

x=-10
assert x>0
print("working")

l=[1,2,3,4]
assert len(l)>0
print("list have some element")

l=[]
assert len(l)>0
print("list have some element")


marks=int(input("enter the number"))
assert 0<=marks<=85
print("good marks")

"""