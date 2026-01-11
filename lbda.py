"""
#Lambda:

-Lambda is also known as anonymous function.
-Anonymous function means we can execute the program without using the function name.
-They are also known as single line function.
-Here we can't write multiple code lines.

-DRAWBACKS:

>Here we can't use elif program(nested if)
>Here we can't use nested if else statements
>We can't use here while and for loop.We can use for loop,but it will act like a comprehension.
>It does not support transfer statement(break,pass,continue)
>Here we can't use return and yield keywords.
>It doesn't support increment and decrement.

-Syntax:
new_vn=lambda argument1, argument2,argument3:expression
"""
"""
x=lambda a,b:a*b
print(x(2,3))

z1=lambda x,y:(x**3,x+y,x-y,y**2)
print(z1(3,4))

y=lambda x: f'the given number {x} is even' if x%2==0 else f'the given number {x} is odd'
print(y(20))
print(y(21))

y=lambda a,b:f'{a} is greater' if a>b else f'{b} is greater'
print(y(100,56))"""


""""
#WAPTC if the given string is palindrome or not
w=lambda z:z==z[::-1]
print(w('MOM'))

w=lambda z:f'The given word {z} is palindrome' if z==z[::-1] else f'The given word {z} is not palindrome'
print(w('MOM'))
print(w('Python'))

#WAPTP length and its word
w=lambda z:f'Length:{len(z)},Word:{z}'
print(w('python class'))

#waptp the squares of the numbers
a=lambda z:[i**2 for i in z]
print(a([1,2,3,4]))

#waptp only values in the given dictionary
q={'abc':700,88:99,"bcv":45678}
a=lambda q:q.values()
print(a(q))

#waptc if the number is divisible by 3 and 5 or not
a=lambda q:f'{q} is divisible 'if q%3==0 and  q%5==0 else f'{q} is not divisible'
print(a(15))
print(a(10))

#wapt convert negative number to positive number
a=lambda y:abs(y)
print(a(-99))

#wap which return the first letter of the sequence
a=lambda y:y[0]
print(a('Python'))
"""
#waptp the number present in the list with their corresponding indices
#l=[100,200,300,400,500]

