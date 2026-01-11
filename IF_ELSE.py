#if_else condition:
#                  if the given condition satisfied it will execute the true state block or in if block,
#                  if the condition is not satisfied it will execute the false state block or in else block.
#Here if and else both are keywords.
#Conditional statements are those who control the flow of program execution based on condition.
#Drawback:Here we can only check two conditions.


"""#1)waptc the given number is  divisible by 7.
x=eval(input('Enter a element: '))
if x%7==0:
    print(f'The given number {x} is divisible by 7')
else:
    print(f'The given number {x} is not divisible by 7')

#2)waptc the given element is iterable or single value data type
x=eval(input('Enter a datatype: '))
if type(x) in (str,list,tuple,dict,set):
    print(f'The given element {x} is iterable')
else:
    print(f'The given element is single value datatype')

#3)waptc the given number is even convert to complex datatype else print as it is.
a=eval(input('Enter the number: '))
if a%2==0:
  print(complex(a))
else:
  print(a)

#4)waptc if the male and female are eligible for wedding or not
a=eval(input('Enter the age of male: '))
b=eval(input('Enter the age of female: '))
if a>=21 and b>=18:
    print(f'The Male and Female are eligible for wedding')
else:
    print(f'The Male and Female are not eligible for wedding')

#5)waptc greater number among two numbers.
a=eval(input('Enter the value 1: '))
b=eval(input('Enter the value 2: '))
if a>b:
    print(f'The value {a} is greater than the value {b}')
else:
    print(f'The value {b} is greater than the value {a}')

#6)waptc if the given number is even or not if it is not even add+1 and make it even.
a=eval(input('Enter the number: '))
if a%2==0:
    print(a)
else:
    print(a+1)

#7)waptc whether the first character in the given string is starting with uppercase or not if not then capitalize it
s=eval(input('Enter a string: '))
if s[0].isupper():
    print('The first letter is uppercase')
else:
    print(s.capitalize())

#8)wap to check if the given number is even if so make it half else make exponent
a=eval(input('Enter a number: '))
if a%2==0:
    print(a/2)
else:
    print(a**2)

#9)waptc the number should be divisible by both 3 and 7
a=eval(input('Enter a number: '))
if a%3==0 and a%7==0:
    print(f'The number {a} is divisible by 3 and 7')
else:
    print(f'The number {a} is not divisible by 3 and 7')

#10)wap if the length of string is even then reverse else convert into uppercase
a=eval(input('Enter a string: '))
if len(a)%2==0:
    print(a[::-1])
else:
    print(a.upper())

#11)wap to check a number is positive or negative number.
a=eval(input('Enter the number: '))
if a<1:
    print(f'The number {a} is negative')
else:
    print(f'The number {a} is positive')

#12)waptc if the specified character is present in the string
a='Python'
x=eval(input('Enter a character: '))
if x in a  :
    print(f'The character {x} is in the string')
else:
    print(f'The character {x} is not in the string')

#13)wap to check the length  of dict if the length of dict is not even add a item and make it even
s={'a':'apple','b':'ball','c':'cat'}
if len(s)%2==0:
    print(s)
else :
    s.update({'d':'dog'})
    print(s)

#14)wap to check if the given number is greater than 5 if it is greater convert into neg number if not print as it is
a=eval(input('Enter a number: '))
if a>5:
    print(-abs(a))
else:
    print(a)

#15)wap to check if the given character is not vowel then print next character if it is print as it is
a=eval(input('Enter a character: '))
if a not in 'aeiouAEIOU':
    a=ord(a)+1
    print(chr(a))
else:
    print(a)

#16)wap to check if the given character is not vowel then print previous character if it is print as it is
a=eval(input('Enter a character: '))
if a not in 'aeiouAEIOU':
    a=ord(a)-1
    print(chr(a))
else:
    print(a)

#17)wap to print the given string is even length reverse the string else print its middle character
x=eval(input('Enter a string: '))
if len(x)%2==0:
    print(x[::-1])
else:
    print(x[len(x)//2])

#18)wap to check whether a given value is a list and first and last value should be integer,
# if condition is satisfied  divide the first value by 5 and perform the bitwise not for the last value
# and value are stored in same position in the list
# or else to power length  of the collection and  display it
a=[1,2,3,4,5,6]
if type(a)==list and type(a[1])==int and type(a[-1]==int):
    a[0]=(a[1]//5)
    a[-1]=(~a[-1])
    print(a)
else:
    print(len(a)**2)

#19)waptc if the given character is alpha or not if it is create its replica for 2 times
a=eval(input('Enter a character: '))
if a.isalpha():
    print(a*2)
else:
    print(f'The character {a} is not alphabet')

#20)Write a program to check whether a given number is greater than 10 or not.
# if it is greater than 10 print message as greater or else print that number with not a greater than.
a=eval(input('Enter a number: '))
if a>10:
    print(f'The number {a} is greater than 10')
else:
    print(f'The number {a} is less than 10')

#21)WAP to check whether the given two input numbers are divisible by 3 and 5.
# If it is divisible, print “Good Morning”, if it is not divisible print “Good Evening”.
a=eval(input('Enter a number 1: '))
b=eval(input('Enter a number 1: '))
if a%5==0 and a%3==0 and b%3==0 and b%5==0:
    print(f'Good morning')
else:
    print(f'Good evening')

#22)WAP to accept two integers and check whether those two values are equal or not.
# If equal, multiply to value or else to display the quotation value.
a=int(input('Enter a number 1: '))
b=int(input('Enter a number 2: '))
if a==b:
    print(a*b)
else:
    print(a/b)

#23)WAP to the given number integer, if n is greater than 21,
# print the absolute difference between n and 21 otherwise print twice the absolute difference
a=int(input('Enter a number: '))
if a>21:
    print(abs(21-a))
else:
    print(2*abs(21-a))

#24)WAP to check whether the given number is divisible by 3 or not if yes,
# print the number or else print the cube of the numbers.
a=eval(input('Enter a number: '))
if a%3==0:
    print(a)
else:
    print(a**3)

#25)WAP to check whether the given input is divisible by 3 and 5.
#If yes print the actual number or else print string of that number.
a = int(input('Enter a number: '))

if a % 3 == 0 and a % 5 == 0:
    print(a)
else:
    print(str(a))

#26)WAP to check whether the given number lies between 1 to 19,
# if it is true square that number or else false cube that number  and display the number.
a=eval(input('Enter a number: '))
if 1<a<19:
    print(a**2)
else:
    print(a**3)

#27)WAP to check whether the student has passed or failed. If the student got more than 40 marks,
# print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along with those marks
a=int(input('Enter the marks: '))
if a>40:
    print(f'{a}-Pass')
else:
    print(f'{a}-Fail')

#28)WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or odd.
# if condition is True, to perform display the ascii character.
# or else to perform floor division with 5 and display it.
a=eval(input('Enter a number: '))
if 47<a<58 and a%2==0 and a!=0:
    print(chr(a))
else:
    print(a//5)

#29)WAP to check whether a given value is less than 125 and in between 47 to 125 or not. if condition is True,
# to perform store the given value as key and value as a character into the dict or else to append the value in list and display it.
a=eval(input('Enter a number: '))
b={}
c=[]
if 47<a<125:
    b[a]=chr(a)
    print(b)
else:
    c.append(a)
    print(c)

#30)WAP to check whether a given character is uppercase or other character.
# if uppercase, display the uppercase with character or else display the other character with character.
a=eval(input('Enter a character: '))
if a.isupper():
    print(f'{a}-Uppercase character')
else:
    print(f'{a}-other character')

#31)WAP to check whether a given character is lowercase or other character.
#if lowercase, display the lowercase with character or else display the other character with character.
a=eval(input('Enter a character: '))
if a.islower():
    print(f'{a}-Lowercase character')
else:
    print(f'{a}-other character')

#32)WAP to check whether a given character is uppercase or other character.
# if uppercase, convert to lowercase .or else display the ascii number
a=eval(input('Enter a character: '))
if a.isupper():
    print(a.lower())
else:
    print(ord(a))

#33)WAP to check whether the given character is in lowercase or uppercase. If it is in lowercase,
# convert it into uppercase, or else it is in uppercase and convert it into lowercase. Display the value.
a=eval(input('Enter a character: '))
if a.isupper():
    print(a.lower())
else:
    print(a.upper())


#34)WAP to check whether the given string of the first character is a special symbol or not. If a special symbol,
# to extract and display the middle character or else to reverse the string and display the half of the string.
a='@HelloWorld'
if not a[0].isalnum():
    b=len(a)//2
    print(a[b])
else:
    c=a[::-1]
    x=len(c)//2
    print(c[:x])

#35)WAP to check whether the input character is a vowel or not.
# If it is vowel print ‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’.
a=eval(input('Enter a character: '))
if a in ('aeiouAEIOU'):
    print(f'{a}-VOWEL')
else:
    print(f'{a}-CONSONANT')

#36)WAP to check whether a given string of first character is alphabet or not,
#if the alphabet prints reverse the string
#or else print the middle character.
a=eval(input('Enter a string: '))
if a[0].isalpha():
    print(a[::-1])
else:
    print(a[len(a)//2])

#37)WAP to check whether a given string is less than 3 characters,
# to print the entire string otherwise to print after third positions to the remaining string.
a=eval(input('Enter a string: '))
if len(a)==3:
    print(a)
else:
    print(a[3::])

#38)WAP to check whether a given length of the string is even or not.
# if even, to append the new string called "bye" or else print the first and last characters.
a=eval(input('Enter a string: '))
if len(a)%2==0:
    print(a+ 'bye')
else:
    print((a[0]),(a[-1]))

#39)WAP to check whether a given length of the string is odd or not.
# if odd, to append the new string("Haii") from the starting of the given string,
# or else to avoid the starting character and ending character of the given  string and to display the remaining characters.
a=eval(input('Enter a string: '))
if len(a)%2==1:
    print('Haii'+a)
else:
    print(a[1:-1])

#40)WAP to check whether the last of the given string is a special character or not,
# if the special character prints reverse the string except the last character
# or else to check if the length of the string is odd or not,
# if odd to extract the middle character to the end of the string.
a=eval(input('Enter a string: '))
if not a[-1].isalnum():
    print(a[:-1][::-1])
else:
   if len(a)%2==1:
        print(a[len(a)//2])

#41)WAP to check whether the given value is present inside the given collection or not.
# if value is present, display the value is available or else the value is not present.
a=input('Enter a collection: ')
b=input('Enter a value: ')
if b in a:
    print(f'{b}-Value is available')
else:
    print(f'{b}-Value is not available')

#42)WAP whether a given string, if string length is more than 2,
# then it displays a new string with the first and last characters switched,
# otherwise the display the 3 copies of given string.
a=eval(input('Enter a string: '))
if len(a)>2:
    print(a[-1]+a[1:-1]+a[0])
else:
    print(a*3)

#43)WAP to check whether a given value is a string or not and length of the value should be more than 7,
# if condition is satisfied to append the new string in the middle of the given string
# or else to perform the replications with 3 and display the result.
a=eval(input('Enter a value: '))
if type(a)==str and len(a)>7:
    new_str= eval(input('Enter a new string: '))
    mid=len(a)//2
    print(a[:mid]+new_str+a[mid:])
else:
    print(a*3)

#44)WAP to check if the given string of first and second character should be sequence or not.
# if the sequence prints the first, second and last two characters,
# or else the first half string is reversed and the remaining half string should be normal and display it.
a=eval(input('Enter a string: '))
if ord(a[1])==1+ord(a[0]):
    print(a[0]+a[1]+a[-2]+a[-1])
else:
    mid=len(a)//2
    print((a[:mid][::-1])+a[mid:])

#45)WAP to check if the given character in vowel or consonant
# if vowel print the next character if other print the previous character
a=eval(input('Enter a character: '))
if a in "aeiouAEIOU":
    b=ord(a)+1
    print(chr(b))
else:
    c=ord(a)-1
    print(chr(c))

#46)WAP to check whether a given key is present in the dict or not.
# if key is present: display the value or else add key and new value inside the dict.
a=eval(input('Enter a dictionary: '))
b=eval(input('Enter a key: '))
if b in a:
    print(a[b])
else:
    a.update({5:50})
    print(a)

#47)WAP to check whether a given collection is set or not. if set, append the new value,
# or else eliminate the duplicate values in collection. final results should be set type
a=eval(input('Enter a collection: '))
if type(a)==set:
    a.add(eval(input('Enter a value: ')))
    print(a)
else:
    b=set(a)
    print(b)

#48)WAP to read the age of a candidate and determine whether it is eligible for his/her own vote or not.
# it eligible print age and eligible messages or else print not eligible
age=eval(input('Enter age: '))
if age>=18:
    print(f'{age} - ELIGIBLE')
else:
    print(f'{age} - NOT ELIGIBLE')

#49)WAP to check whether the given string is palindrome or not
# if it is a palindrome print palindrome along with the string if it is not a palindrome print not palindrome
a=eval(input('Enter a string: '))
if a==a[::-1]:
    print(f'{a}-Palindrome')
else:
    print(f'{a}-Not Palindrome')

#50)WAP to check whether a given number is palindrome or not.
# If palindrome, display the given value as a palindrome or else not a palindrome
a=eval(input('Enter a number: '))
b=str(a)
if b==b[::-1]:
    print(f'{a}-Palindrome')
else:
    print(f'{a}-Not Palindrome')

#51)WAP to check length of both string collections are equal or not.
# if both are equal print the concat the two strings and display,
# or else if any one of the collection not equal print both the collections with lengths
a=eval(input('Enter a first string: '))
b=eval(input('Enter a second string: '))
if len(a)==len(b):
    print(a+b)
else:
    print(f'{a}:{len(a)} , {b}:{len(b)}')

#52)WAP to check whether both given values point to the same memory location or not.
# if it is true print the middle item of the second collection,
# or else if it is false print the first item and last item of the first collection along with the memory address.
a=eval(input('Enter a collection 1: '))
b=eval(input('Enter a collection 2: '))
if id(a)==id(b):
    print({b[len(b)//2]})
else:
    print(a[0],a[1],id(a))

#53)WAP to  check whether a given string collection is more than ten,
# and the first + last character of the ascii values should be divisible by 5,
# if condition is satisfied print first, middle, last characters ASCII values
# or else print the string three times.
a=eval(input('Enter a string: '))
if len(a)>10 and (ord(a[0]) + ord(a[-1])) % 5 == 0:
    print(ord(a[0]), ord(a[len(a)//2]),ord(a[-1]))
else:
    print(a*3)

#54)WAP to check whether the middle of the item present in the list is string data type or not if it is string print
# that list or else if it is not string  then print that middle item.
a=eval(input('Enter a list: '))
if isinstance(a[len(a)//2], str):
    print(a)
else:
    print(a[len(a)//2])

#55)WAP Given a string, return a new string where the first and last characters have been exchanged.
a=eval(input('Enter a string: '))
if len(a)<=1:
    print(a)
else:
    print(a[-1] + a[1:-1] + a[0])


#56)Write a program to find out such numbers which are divisible by 7 but are not a multiple of 5.
# Both the conditional is satisfied and print actual value.
# if one condition is not satisfied actual number is multiply by 4 and print result
a=eval(input('Enter a number: '))
if a%7==0 and a%5!=0:
    print(a)
else:
    print(a*4)

#57)WAP to check whether two values are pointing to the same memory address or not.
# If the same memory displays the address or else displays the two values addresses.
a=eval(input('Enter a value 1: '))
b=eval(input('Enter a value 2: '))
if id(a)==id(b):
    print(id(a))
else:
    print(id(a),id(b))

#58)WAP to check whether a given input character is a special symbol or not
# if it is a special symbol then print that character three times and tell or else print that character 5 times.
char=input('Enter a character: ')
if not char.isalnum():
    print(f'{char*3}-Special Character')
else:
    print(char*5)"""

#59)WAP to check length of both string collections equal or not
# if it is equal print the connection of any one of the collections if it is not equal print both the collection.


