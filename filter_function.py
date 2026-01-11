"""
#Filter:
-It is an inbuilt function
-Syntax:
        new=filter(function_name,iterable)
-Here it will only consider elements which satisfies the conditions and the rest of the element are ignored.
-Here it won't accept multiple iterables it will raise the error if we pass multiple elements.
-Here we don't need to use map function as filter will pass the element from iterable to function.
-Here it will show filter object address to avoid it we can use typecasting or looping.

"""
"""
a=[1,2,3,4,5,6]
def even(i):
    return i%2==0
a=filter(even,a)
print(list(a))       #--------->[2, 4, 6]


a=[11,-129,-8,234,-292,2222]
def pos(i):
    return i>0
a=filter(pos,a)
print(list(a))        #------>[11, 234, 2222]

a=[11,-129,-8,234,-292,2222]
z=lambda i:i>0
print(list(filter(z,a)))          #-------->[11, 234, 2222]
print(list(map(lambda x:x>0,a)))     #---->[True, False, False, True, False, True]

s=['ABC','abc','XYZ','xyz','MNO','mno']
def upp(s):
    for i in s:
        if i.isupper():
            print(i)
upp(['ABC','abc','XYZ','xyz','MNO','mno'])


def upper(s):
    return s.isupper()
a=filter(upper,s)
print(list(a))     #------->['ABC', 'XYZ', 'MNO']

a=lambda x:x.isupper()
print(list(filter(a,s)))    #---------->['ABC', 'XYZ', 'MNO']
print(list(map(a,s)))      #---->[True, False, True, False, True, False]

a='asdfgh23456780miuytdsxcvbn'
s=lambda x:x.isdigit()
print(list(filter(s,a)))        #----------->['2', '3', '4', '5', '6', '7', '8', '0']

#1)keep number is range 10-20
nums=[5,10,15,20,25]
a=lambda x:10<=x<=20
print(list(filter(a,nums)))         #---------->[11, 13]

#2)filter emails containing "@gmail.com
a=['abc@gmail.com','xyz@yahoo.com','test@gmail.com']
s=lambda x:x.endswith('@gmail.com')
print(list(filter(s,a)))          #---------->['abc@gmail.com', 'test@gmail.com']

#3)keep tuples whose sum is greater than 10
x=[(1,2),(5,6),(3,4),(7,8)]
s=lambda i:sum(i)>10
print(list(filter(s,x)))       #----------->[(5, 6), (7, 8)]

#11.Keep words longer than 4 letters
words = ["cat", "elephant", "dog", "tiger"]
a=lambda x:len(x)>4
print(list(filter(a,words)))          #-------->['elephant', 'tiger']

#12.Keep palindromes
words = ["madam", "python", "level", "world"]
a=lambda x:x==x[::-1]
print(list(filter(a,words)))     #---------->['madam', 'level']

#13.Keep uppercase words
words = ["HELLO", "world", "PYTHON", "code"]
a=lambda x:x.isupper()
print(list(filter(a,words)))             #------->['HELLO', 'PYTHON']

#14.Filter names that end with “n”
names = ["Arun", "Kiran", "Deepak", "Sohan"]
a=lambda x:x.endswith('n')
print(list(filter(a,names)))          #------>['Arun', 'Kiran', 'Sohan']

#7.Keep only digits from a string
s="a1b2c3d4"
a=lambda x:x.isdigit()
print(list(filter(a,s)))         #-------->['1', '2', '3', '4']

#8.Keep only alphabets from a string
s1= "p3y4t5h6o7n"
a=lambda s:s.isalpha()
print(list(filter(a,s1)))      #----------->['p', 'y', 't', 'h', 'o', 'n']

#9.Filter students who passed (marks ≥ 50)
marks = {"Ann": 45, "Ben": 70, "Cat": 55}
a=lambda i:marks[i]>=50
print(list(filter(a,marks)))        #----------->['Ben', 'Cat']

#10.Keep numbers divisible by 3
nums = [3, 6, 8, 10, 12, 15]
a=lambda i:i%3==0
print(list(filter(a,nums)))          #------->[3, 6, 12, 15]

#2.filter odd numbers
y=[10,11,12,13,14]
a=lambda x:x%2==1
print(list(filter(a,y)))          #---------->[11, 13]

#3.Remove empty strings
data=["apple","","banana","","cherry"]
a=lambda x:x!=""
print(list(filter(a,data)))         #---------->['apple', 'banana', 'cherry']

#5.Filter Truthy values
s=[0,False,"",None,"Hii",6]
q=lambda i:bool(i)
print(list(filter(q,s)))      #---------->['Hii', 6]

#6.Keep strings starting with “a”
words = ["apple", "banana", "avocado", "cherry"]
a=lambda x:x.startswith('a')
print(list(filter(a,words)))       #---------->['apple', 'avocado']"""



a='yellow'
a.replace('l','*',2)