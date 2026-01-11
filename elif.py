#elif:Whenever we have multiple conditions that time we go for elif condition.
#In elif it will check one by one condition it won't check all the conditions ata a time
#ELSE BLOCK IS NOT MANDATORY


#WAP to check if the given number is positive or negative or neutral
"""a=eval(input('Enter the number: '))
if a>0:
    print(f'The given number {a} is positive')
elif a==0:
    print(f'The given number {a} is Neutral')
elif a<0:
    print(f'The given number {a} is negative')

#waptc if the given element is alphabet or digit or special character
a=eval(input('Enter the element: '))
if a.isalpha():
    print(f'The given element {a} is alphabet')
elif a.isdigit():
    print(f'The given element {a} is digit')
else:
    print(f'The given element {a} is special character')

#without using inbuilt function 
a=eval(input('Enter the element: '))
if ord('A')<=ord(a)<=ord('Z') or ord('a')<=ord(a)<=ord('Z'):
    print(f'The given element {a} is alphabet')
elif ord('0')<=ord(a)<=ord('9'):
    print(f'The given element {a} is digit')
else:
    print(f'The given element {a} is special character')  #here we cannot pass unlimited characters.

#waptc the given datatype is single,collection or sequence datatype
a=eval(input('Enter the element: '))
if type(a) in [int,float,bool,complex]:
    print(f'The given datatype {a} is single value datatype')
elif type(a) in [set,dict]:
    print(f'The given datatype {a} is collection datatype')
elif type(a) in [str,list,tuple]:
    print(f'The given datatype {a} is sequence datatype')

#using is instance
a=eval(input('Enter the element: '))
if isinstance(a,(int,float,bool,complex)):
  print(f'The given element {a} is single value datatype')
elif isinstance(a,(set,dict)):
    print(f'The given element {a} is collection datatype')
elif isinstance(a,(str,list,tuple)):
    print(f'The given element {a} is sequence datatype')

#waptc the given is string if yes return its length,
# if it is list pop its last element
# else if it is tuple reverse the tuple
# else invalid datatype
a=eval(input('Enter the element: '))
if type(a)==str:
    print(len(a))
elif type(a)==list:
    print(a.pop())
elif type(a)==tuple:
    print(a[::-1])
else:
    print(f'Invalid datatype')

#wap to check marriage data.
a=eval(input('Enter the age: '))
if 0<a<18:
    print(f'Child marriage')
elif a==18:
    print(f'Perfect age for marriage ^^')
elif 18<a<24:
    print(f'Arrange marriage :|')
elif 24<a<30:
    print(f'Love marriage :)')
elif 30<a<40:
    print(f'Breakup :(')
elif a>40:
    print(f'GO TO THE HELL!!!')

#waptc largest number among three variables
a=10
b=20
c=9
if a>b and a>c:
    print(f'{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater than {a} and {c}')
elif c>a and c>b:
    print(f'{c} is greater than {b} and {a}')

#user input
a = eval(input('Enter num 1: '))
b = eval(input('Enter num 2: '))
c = eval(input('Enter num 3: '))
if a > b and a > c:
    print(f'{a} is greater than {b} and {c}')
elif b > a and b > c:
    print(f'{b} is greater than {a} and {c}')
elif c > a and c > b:
    print(f'{c} is greater than {b} and {a}')"""

#waptc smallest number among three variables
a = eval(input('Enter num 1: '))
b = eval(input('Enter num 2: '))
c = eval(input('Enter num 3: '))
if a < b and a < c:
    print(f'{a} is smaller than {b} and {c}')
elif b < a and b < c:
    print(f'{b} is smaller than {a} and {c}')
elif c < a and c < b:
    print(f'{c} is smaller than {b} and {a}')



