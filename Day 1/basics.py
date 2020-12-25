# single line comment

'''
   this 
   is multi
   line comment. 
'''

# first code
# print("Hello World!")

# print(statement, end = '\n', sep = ' ')
# print("hello", end='\n')
# print("everyone!!")

# print('today', 'is', 'the', 'first', 'class', sep= ',')


# string --> '' or  ""
# print(python) # python is not defined

# Taking input in python
# n = input("Enter your name :") 
# print("your name is", n)


"""
Variables and Datatypes

# boolean    - bool (True or False)
# integer    - int (1, 2 ,3)
# real       - float(1.2, 5.56)
# string     - str    group of character ("xyz")
"""
# a = 15 # int
# print(a)
# print(type(a)) # type function is used to print the type of a variable

# b = 10.2 # float
# print(b)
# print(type(b))

# c = True # bool
# print(c)
# print(type(c))

# d = "today is a sunny day." # string
# print(d)
# print(type(d))


'''
Type Casting
'''
# n = input() # by default it reads input as a string
# n = int(input()) # Explicit type casting
# n = float(input())
# print(n)
# print(type(n))

"""
Operators 
# Arithmatic operator:
# add   -  +  
# sub   -   -
# mul   -   *
# divide   -    /
# integer divide    -   //
# modulo    -   %  --- gives us remainder
# power  - **
    
# Logical operators:
# OR
# AND
# NOT

# Comparison Operators
# >, <, ==(equal), >=, <=, != (not equal)
"""

# a = 20
# b = 3

# print("sum is :",a+b)
# print("sub is :",a-b)
# print("mul is :",a*b)
# print("div is :",a/b) # float
# print("remaider is :",a%b)
# print("int div is :", a//b) # integer

# print("pow : ", 2**3) # 2^3

# print("sqrt 25 is ", 25**0.5) # for finding sq root

# s = "Today"
# print(s+s) # + concatenate
# print(5*(s + " ")) # today will be printed 5 times

# Logical operators
# print(True and True)


"""
Conditional Statements

if condition :
    statements
elif condition :
    statement
else :
    statements (consider)
statmenets (not consider)
"""

# n = 18

# if n > 10 :
#     print("larger")
# else :
#     print("smaller")
# print("out of else ")

# 4 spaces or 1 tab indendation


# ques

# 1. odd even
# n = int(input("Enter a number :"))
# if n%2 == 0 :
#     print("even")
# else :
#     print("odd")


# 2. Remainder by 3
# n = int(input("Enter a Number :"))
# if n%3 == 0 :
#     print('zero')
# elif n%3 == 1 :
#     print('one')
# else :
#     print('two')


# = assigment operator and == comparison
# a = b it will make a equal to b
# a == b compare 

# 3. Fizz Buzz (multiple of 3 --> Fizz, multiple of 5 --> Buzz, both then --> FizzBuzz)
# n = int(input("Enter a number :"))

# if n%3 == 0 and n%5 == 0 :
#     print('FizzBuzz')
# elif n%3 == 0 :
#     print('Fizz')
# elif n%5 == 0 :
#     print('Buzz')
# else :
#     print(n)

# 4. Calculator
# n = int(input("Enter first Number :"))
# m = int(input("Enter second Number :"))
# op = input("Enter operator :")

# if op == '+' :
#     print(n+m)
# elif op == '-' :
#     print(n-m)
# elif op == '*' :
#     print(n*m)
# elif op == '/' :
#     print(n/m)
# elif op == '**' :
#     print(n**m)
# else :
#     print("Wrong operator")

# 4. Leap year
#  year is divisible 400 ---> leap year
#  year divisible 100 and not by 400 --> not a leap year
#  year divisible by 4 --> leap year
#  else not a leap year

# n = int(input("Enter a year :"))

# if n % 400 == 0:
#     print('Leap Year')
# else :
#     if n % 100 == 0 :
#         print("Not a Leap Year")
#     elif n % 4 == 0:
#         print('Leap Year')
#     else :
#         print('Not a Leap Year')

"""
# Loops

# For
# while
"""

# i = 0 # counter
# while i < 10 : # condition
#     print('Hello')
#     # i = i+1 # step size
#     i += 1
#     print('world')

# range(start, stop, end)
# for i in range(2, 10, 2) :
#     print(i)

# 1. Table
# n = int(input("Enter a Number :"))

# for i in range(1, 11) :
#     print(n*i)