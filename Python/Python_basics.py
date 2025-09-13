# print('Hello World!')

### This is a single line comment in python

"""
and this is a mutli line
comment in python
"""

#-----------------------------------------------------Variables and data types-------------------------

### Variables and data types in python 
### Variables are the containers to store the data, whereas, there are 4 data types in python
### the rest are derived data types

# a = 5,
# b = 6.45,
# c = True
# d = False,
# name = 'Developer dairies'

# print(f"{a} : {type(a)} :: {b} : {type(b)} :: {c} : {type(c)} :: {d} :: {type(d)} :: {name} :: {type(name)}")


#------------------------------------------------Taking the user input in python--------------------------


### By default input is a string or a character but to change it, we have to change it's type
### the process of changing the type of the data type of one variable to another variable is called type casting

# name = input('Enter your name : ')
# age = int(input('Enter your age : '))

# print(f"Hello {name}, you are {age} years old")
# print(type(name), type(age))


#------------------------------------Conditional programming in python---------------------------------------

### conditional programming contains if-else statement, and
### nested if else statement 

### example : 1

# age = 21

# if age < 18 : 
#     print('You are not an adult yet :( ')
# else : 
#     print('congrats you are adult, so start programming now :) ')

### example : 2

# age = int(input('enter your age : '))

# if age > 18 :
#     if age < 65 :
#         print('Sorry you are not eligible for the retirement')
#     else :
#         print('Yes! finally you can enjoy and stop working now ')
# else : 
#     print('You better be at school kid :) ')


#-------------------------------------String in python--------------------------

### string is a data type in python to hold individual characters and the long sentences
### strings offer various operations, they can be accesed by typing the string and (.) in the end and a whole 
### bunch of operations are gonna showup

# intro = "Hello my name is Developer"

# intro = intro.lower()
# len = intro.__len__()

# print(intro, len)


#----------------------------------------Loops in python----------------------------

### in python mainly there are 2 types of loops
### for loop, which has an initiator, stooper and index all in the begining
### while loop, which has the controller in the end
### loops can also be nested like the if-else statements

### while loop
### if we forget to set the controller in a correct way then it might run an infinite loop which might never end,

# i = 0

# while(i < 5) : 
#     print('Hello, I am learning python and I like it')
#     i += 1

### for loop

# for i in range(0, 5) :
#     print('I wanna become a data scientist')

# for i in range(10, 0, -1) : 
#     print(i)
# print('Happy new year lol!')

# for i in range(0, 5) : 
#     for j in range(10, 0, -1):
#         print(j)
#     print(i)


#-----------------------functions in python------------------------------

### functions in python are the block of code that can be reused over and over again,
### depending on the types functions may or may not return a value

# a = int(input('enter first number : '))
# b = int(input('enter second number please : '))

# def add(a, b) : 
#     c = a+b
#     return c

# add(a, b)

# a = int(input('enter first number : '))
# b = int(input('enter second number please : '))

# def add(a, b) : 
#     c = a+b
#     print('the sum is  : ', c)

# add(a, b)