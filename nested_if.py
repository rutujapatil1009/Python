#Nested if_else condition:

"""#waptc if the given number is even and greater than 5.
a=int(input('Enter a number: '))
if a%2==0:
    print('The number is even')
    if a>5:
        print(f'The given number {a} is greater than 5.')
    else:
        print(f'The given number {a} is smaller than 5')
else:
    print('The number is odd')

#waptc if the given number is odd and divisible by 7
a=int(input('Enter a number: '))
if a%2==1:
    print('The number is odd')
    if a%7==0:
        print(f'The given number {a} is divisible by 7')
    else:
        print(f'The given number {a} is not divisible by 7')
else:
    print('The number is even')

#wap to book a ticket in book my show

print('Welcome to book my show')
Theatre=['PVR','Moviemax','cinepolis','city pride','INOX']
user=input('Enter your theatre name: ')

if user in Theatre:
    print(f'User one selected the theatre is {user} ')

    movies=['RRR','KGF','Animal','Kingdom']

    user2=input('Enter your movie name: ')
    if user2 in movies:
        print(f'User one selected the movie is {user}  \n'
              f'User two selected the movie is {user2} ')

        price=[200,400,600]
        amt=int(input('Enter your ticket price: '))
        if amt==price[0]:
            print(f'User one selected the movie is {user}  \n'
                  f'User two selected the movie is {user2} \n'
                  f'Total amt of the ticket is {amt} ')
        elif amt==price[1]:
            print(f'User one selected the movie is {user}  \n'
                  f'User two selected the movie is {user2} \n'
                  f'Total amt of the ticket is {amt} ')
        elif amt==price[2]:
            print(f'User one selected the movie is {user}  \n'
                  f'User two selected the movie is {user2} \n'
                  f'Total amt of the ticket is {amt} ')
        else:
            print(f'Price is too high')
    else:
        print(f'Wrong movie selected')
else:
    print(f'Wrong theater selected')

#wap to perform only list operation if I click first option we have to perform pop()
#and second option sort() and third option clear() else invalid datatype.
a=eval(input('Enter a list: '))
if type(a)==list:
    options=eval(input('Enter a options: '))
    if options==1:
        print(a.pop())
        print(a)
    elif options==2:
        a.sort()
        print(a)
    elif options==3:
        a.clear()
        print(a)
    else:
        print('Invalid option')
else:
    print('Invalid datatype')

#wap to validate facebook username and password condition is username:'Python' and password:'python-master'
name=input('Enter your name: ')
password=input('Enter your password: ')

if name=='Python':
        print('valid username')
        if password=='python-master':
            print('valid password')
        else:
            print('invalid password')
else:
        print('Invalid username')

#wap  to find middle element is even or odd.
s=[3,4,6,7,9,1,5]

if s[len(s)//2]:
    print(f'The  element {s[len(s)//2]} is middle element')
    if s[len(s)//2]%2==0:
        print(f'The  element {s[len(s)//2]} is even')
    else:
        print(f'The  element {s[len(s)//2]} is odd')
else:
    print(f'The element {s[len(s)//2]} is not middle element')


#Check number is divisible by 2, 3, and 5
a=int(input('Enter a number: '))
if a%2==0:
    print('The number is divisible by 2')
    if a%3==0:
        print('The number is divisible by 3')
        if a%5==0:
            print('The number is divisible by 5')
        else:
            print('The number is not divisible by 5')
    else:
        print('The number is not divisible by 3')
else:
    print('The number is not divisible by 2')

#Check eligibility for voting and issuing a driving license
#condition---> 18 eligibility for vote and more than 21 driving license
a=int(input('Enter a age: '))
if a>=18:
    print('The person is eligible for voting')
    if a>=21:
        print('The person is eligible for issuing driving license')
    else:
        print('The person is not eligible for issuing driving license')
else:
    print('The person is not eligible for voting')

#Largest among three numbers(take user input)
a=int(input('Enter a number 1: '))
b=int(input('Enter a number 2: '))
c=int(input('Enter a number 3: '))
if a>b and a>c:
    print(f'{a} is greater')
elif b>a and b>c:
    print(f'{b} is greater')
else:
    print(f'{c} is greater')"""







