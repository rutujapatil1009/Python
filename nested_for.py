"""#wap to print all the number in the given list
d=[[1,2,3],[4,5,6],[7,8,9]]
for i in d:
    print(i)
    for j in i:
       print(j)

#wap to print only odd number in the given list
r=[[10,20,30,7],[40,50,70,1]]
for i in r:
    print(i)
    for j in i:
        if j%2==1:
            print(j)

#wap to print which number is divisible by 5
e=[[10,25,45,67,98,11,13]]
for i in e:
    print(i)
    for j in i:
        if j%5==0:
            print(j)

#wap to print below output
s="AB"
s1="12"
for i in s:
    print(i)
    for j in s1:
        print(i,j)

#wap to print 2 to 5 multiplication table
for i in range(2,6):
    print(f'Table name:{i}')
    for j in range (1,11):
        print(f'{i}*{j}={i*j}')


#wap to print which words is start with vowels
q=[["morning","evening","afternoon","noon"]]
for i in q:
    print(i)
    for j in i:
        if j[0] in 'aeiouAEIOU':
            print(j)"""

#BACKUP

# s='tomorrow is weekend  and non-veg special'
# y={}
# x=s.split()
# for i,j  in enumerate(x):
#     y.update({i:j})
# print(y)

# s='sunday'
# d={}
# for i in s:
#     d.update({i:i.upper()})  #{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}
# print(d)


# l=[89,51,111,77,108,120]
# a={}
# for i in l:
#     a.update({i:chr(i)})
#     a[i]=chr(i)
# print(a)

# s='sunday'
# a=[]
# for i in s:
#     a.append((i,ord(i)))
# print(a)  #[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]





#{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}


# s='tomorrow is weekend  and non-veg special'
# x=s.split()
# a={}
# for i in x:
#     a.update({i:i[::-1]})
# print(a)

# s='hii hello good morning welcome to python session'
# a={}
# for i in s.split():
#     if i[0] not in a:
#         a[i[0]]=[i]
#     else:
#       # a[i[0]]+=[i]
#       # a[i[0]].append(i)  #not recommended
# print(a)


# s='hello python'
# a={}

# for i in range(len(s)):
#         if s[i] not in a:
#             a[s[i]]=[i]
#         else:
#             a[s[i]]+=[i]
# print(a) #{'h': [0, 9], 'e': [1], 'l': [2, 3], 'o': [4, 10], ' ': [5], 'p': [6], 'y': [7], 't': [8], 'n': [11]}

# a='wel123come to 456 the class789'
# s=0
# for i in a:
#     if i.isdigit():
#         s=s+int(i)
# print(s)


#backup

'''
syntax:
for outer in iterable:
    statement
    for inner in outer:
       statement
       

'''

# s='welcome to all'
# for i in s.split():
#     for j in i:
#         print(j,end=' ')   #w e l c o m e t o a l l


# x=[1,2,3,4,5,6]
# y=[1,2,4,5,7,6]
# for i in x:
#     for j in y:
#       if i==j:
#           print(i,'Matching element')


# y=['mom','level','python','word','pen']
# for i in y:
#     a=''
#     for j in i:
#         a=j+a
#         if i==a:
#             print(i)


# for i in y:
#     rev=''
#     for j in reversed(i):
#         rev=rev+j
#         if i==rev:
#             print(i)

# for i in y:
#     rev=''
#     for j in range(-1,-len(i)-1,-1):
#         rev=rev+i[j]
#     if rev==i:
#         print(i)


# x=['python','java','hello']
# for i in x:
#     a=''
#     for j in i:
#         a=j+a
#     print(i,a)


# for i in x:
#     a=''
#     for j in reversed(i):
#         a=a+j
#     print(a,j)



'''
Transfer statement:

1)break
2)pass
3)continue

1)break:
-If we want to terminate the code  or stop the execution,once your condition is satisfied then we have to go for break statement.
-And here it will only print previous data                

2)continue:
-it will skip current iteration where the condition is satisfied and move forward in execution.

3)pass:
-Pass means no operation.
-It is used to avoid errors which can occur when we miss any statement.
-We can either use pass or ...  


'''












