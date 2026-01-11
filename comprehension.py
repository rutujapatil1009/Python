"""COMPREHENSION:To reduce multiple line code into single line or to reduce loc.

*Types of comprehension*
1)List comprehension:[]
2)set comprehension:{}
3)Dict comprehension:{key:value}

-Drawbacks of comprehension:
1)We can't use while loop bcoz here we have to  mention three statements(start,stop,update).
2)We can't use elif program bcoz we can't process multiple conditions in single line.
3)We can't use nested if_else program bcoz of multiple conditions.
4)In comprehension it won't support transfer statement(break/continue and pass).
5)It won't support increment and decrement operation(+=,-=).
6)It won't support return and yield keyword.

NOTE:
    1)What is comprehension?
    2)What are the types of comprehension?
    3)What are the drawbacks of comprehension?

-If we use str in comprehension it will give us object address therefore it is not suitable for this process.

#LIST COMPREHENSION:
-Syntax_01:without if_else  condition

           v_n=[operation for loop]
           operation-insertion,update,print

-Syntax_02:with simple if condition

           v_n=[TSB for loop if condition]

-Syntax_03:with if_else condition

           v_n=[TSB if condition else block for loop]


#SET COMPREHENSION:
-Syntax_01:without if_else  condition

           v_n={operation for loop}
           operation-insertion,update,print

-Syntax_02:with simple if condition

           v_n={TSB for loop if condition}

-Syntax_03:with if_else condition

           v_n={TSB if condition else block for loop}


#Nested comprehension:
-Syntax:v_n=[operation outer for inner for]

"""

"""#wap to print 1 to 5 numbers into the list
x=[i for i  in range(1,6,1) ]
print(x)

print([i for i  in range(1,6,1)])

#wap to print value as well as position
x='Backspace'
for i in enumerate(x):
    print(i)
#by using comprehension
print([i for i in enumerate(x)])

r=['abc','xyz','ab','pqr']
for i in r:
    print(i)

print([i for i in r])

y=[11,12,13,14]
x='abcd'
for i in zip(y,x):
    print(i)

print([i for i in zip(y,x)])

#waptp first and last char in the given list
t=['hello','python','smart','quick']
for i in t:
    print(i[0],i[-1])

print([(i[0],i[-1]) for i in t])"""

"""t=[1,2,3,4,5,6]
for i in t:
    if i%2==0:
        print(i)

print([i for i in t if i%2==0])

#waptc odd len elements in list
t=['hello','python','smart','quick']
print([i for i in t if len(i)%2==1])

#waptp single value data type
m=['hii',[1,2,3],10,True,{2,3,4}]
for i in m:
    if isinstance(i,(int,float,bool,complex)):
        print(i)

print([i for i in m if isinstance(i,(int,float,bool,complex))]) 

#waptp which number is divisible by both 3 and 5 in 1 to 30
for i in range(1,31,1):
    if i%3==0 and i%5==0:
         print(i)

print([i for i in range(1,31,1) if i%3==0 and i%5==0])"""


"""#waptp if the number is even print it's square and if it is odd print its cube
d=[1,2,3,4,5,6]
for i in d:
    if i%2==0:
        print(i**2)
    else:
        print(i**3)

print([i**2 if i%2==0 else i**3 for i in d])

#waptp single value datatype if it is collection reverse it
m=['hii',[1,2,3],10,True]
for i in m:
    if isinstance(i,(str,list,tuple)):
        print(i[::-1])
    else:
        print(i)

print([i if isinstance(i,(int,float,bool,complex)) else i[::-1] for i in m])

#wap to check even numbers in a list and return a list containing only even numbers
l=[2,32,1,52,31,24,56,75]
a=[]
for i in l:
    if i%2==0:
        a.append(i)
print(a)

print([i for i in l if i%2==0])

#wap to check elements inside the collection are even or odd,if it is even
#make it square of that numbers,if it is odd make it as cube of that numbers
l=[2,3,5,1,7,2,3]
print([i**2 if i%2==0 else i**3 for i in l])

#wap to return a list containing 10 multiples of 2
print([i*2 for i in range(1,11)])

#wap to return a list containing 10 multiples of given value(take user input)
a=int(input('Enter a number: '))
print([i*a for i in range(1,11)])"""

#wap to take two lists as input and add that elements and return a single lists
"""a=list(input('Enter a list 1: '))
b=list(input('Enter a list 2: '))
print([a[i]+b[i] for i in range(2)])"""


"""#wap to create a list containing tuples having two elements that is index and value of list
l=["hey","hello","good","evening","python"]
print([i for i in enumerate(l)])

#.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append

l=("hey","hello","good","evenings","python")
print([i if len(i)%2==0 else i[::-1] for i in l])

#Squares of numbers divisible by 3 (1–30)
print([i*i  for i  in range(1,31) if i%3==0])

# Cube of odd numbers (1–20)
print([i**3  for i  in range(1,21) if i%2==1])"""

#SET COMPREHENSION
"""
#Words with length > 4
words = ["apple", "bat", "banana", "cat", "elephant"]
print([i for i in words if len(i)>4])
print({i for i in words if len(i)>4})

#Remove vowels from a string
text = "list comprehension"
print([i for i in text if i not in 'aeiou'])
print({i for i in text if i not in 'aeiou'})

#Extract only integers from a mixed list
items = [1, "apple", 2.5, 3, "banana", 4]
print([i for i in items if isinstance(i,int)])
print({i for i in items if isinstance(i,int)})

#Reverse words containing the letter ‘a’
words = ["cat", "dog", "apple", "ball"]
print([i[::-1] for i in words if 'a' in i])
print({i[::-1] for i in words if 'a' in i})

#Words converted to title case
words = ["python", "java", "machine learning"]
print([i.title() for i in words ])
print({i.title() for i in words })

#Numbers divisible by 4 but not by 8 (1,51)
print([i for i in range(1,52) if i%4==0 and i%8!=0])
print({i for i in range(1,52) if i%4==0 and i%8!=0})


#wap to take two lists as input and add that elements and return a single lists
a=[1,2,3]
b=[4,5,6]
for i,j in zip(a,b):
    print(i+j)

print([i+j for i,j in zip(a,b)])
print({i+j for i,j in zip(a,b)})

#List of ASCII values of characters
chars = ['A', 'B', 'C', 'a', 'b']
print([ord(i) for i in chars])
print({ord(i) for i in chars})

#Characters from string at even indexes
text = "comprehension"
print([text[i] for i in range(len(text)) if i%2==0])
print({text[i] for i in range(len(text)) if i%2==0})

#Words starting and ending with same letter
words = ["level", "radar", "apple", "deed"]
print([i for i in words if i[0]==i[-1]])
print({i for i in words if i[0]==i[-1]})

#First letter of each word
words = ["apple", "banana", "cherry"]
print([i[0] for i in words])
print({i[0] for i in words})

#.Convert list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
print([i.upper() for i in fruits])
print({i.upper() for i in fruits})

#Extract uppercase letters from a string
text = "PyThOn LiSt Comprehension"
print([i for i in text if i.isupper()])
print({i for i in text if i.isupper()})

#Extract first names from full names
names = ["John Smith", "Alice Brown", "Mark Lee"]
print([names.split()[0] for names in names ])
print({names.split()[0] for names in names })"""


#DICTIONARY COMPREHENSION

"""#1. Number and its square (1–10)
print({i:i**2 for i in range(1,11)})

#2.Number and its cube (1–5)
print({i:i**3 for i in range(1,6)})

#3.Character and ASCII value
y="Master mind"
print({i:ord(i) for i in y})

#4. Word and its length
words = ["apple", "banana", "cherry"]
print({i:len(i) for i in words})

#5.Map string to reversed string
words = ["hello", "world", "python"]
print({i:i[::-1] for i in words})

#6.wap to create a dictionary +ve number as key and convert to -ve number
# as a value
x=[-8,6,8,-5,9,8,4,-67]
print({+abs(i):-abs(i) for i in x }

#7.wap to create a dictionary element and its data type pair only
#element  should be individual data type
l=[10,"hai",9.3,4+4j,(11,22),{2,3},False,[1,3]]
print({i: type(i).__name__ for i in l if isinstance(i, (int, float, complex, bool))})

#8.wap to create a dictionary convert uppercase to lowercase and
#lowercase to uppercase
s="FrIdAy"
print({i:(i.lower() if i.isupper() else i.upper() )for i in s })

#9.wap to create a dictionary characters and its count pair
char=["a","M","i","A","M","I","i","H","a","H"]
print({i:char.count(i) for i in char})

#10.wap to create a dictionary with words and
# its length pair and ends with vowel
s = "Anna is here to enjoy a banana"
#o/p{'Anna': 4, 'to': 2, 'enjoy': 5, 'a': 1, 'banana': 6}
print({i:len(i) for i in s.split() if i[-1] in 'aeiouAEIOU'})"""

