"""
Functions

def fun_name(para1, para2, ...) :
    statements

    return # optional
"""

# # this function will print hello world
def hello_world() :
    print('hello, world')

# hello_world() # to call a function 
# hello_world()
# hello_world()

# Function to welcome a user
def hello_user(username) :
    print("hello " + username)

# function called multiple times with different username
# hello_user('abc') 
# hello_user('amy') 
# hello_user('xyz') 

# def factorial(n) :
#     fact = 1
#     for i in range(1, n+1) :
#         fact *= i
#     print(fact)

# # Function call
# factorial(2)
# factorial(4)
# factorial(6)

# Factorial with a return statement 
def factorial(n) :
    fact = 1
    for i in range(1, n+1) :
        fact *= i
    return fact # it return the value from where it is called

# fact2 = factorial(2)
# print(fact2)
# fact3 = factorial(3)
# print(fact3)
# fact5 = factorial(5)
# print(fact5)

# n = int(input())
# r = int(input())

# fact_n = factorial(n)
# fact_r = factorial(r)
# fact_nr = factorial(n-r)

# ans = fact_n/(fact_nr*fact_r)
# print(ans)

# # 1. Find the sum of n natural numbers
# def sumUpTon(n) :
#     sum = 0
#     # to find the sum
#     for i in range(1, n+1) :
#         sum += i

#     return sum # returning the calculated sum

# print(sumUpTon(10))
# print(sumUpTon(5))

# 2. Reverse a number
# 123 --> 321

def rev_num(num) :
    rev = 0

    while num > 0 :
        digit = num % 10
        rev = rev*10 + digit
        num = num // 10
    
    return rev


# print(rev_num(54321))

# 3. Function to print upto n natural number
# def upto_N(n) :

#     for i in range(1, n+1) :
#         print(i)

# upto_N(5)

"""
Recursion

def func_name(para1, para2, ...) :
    # base case ---> where you want rec to stop

    recursive call

    #  return 
"""

# # print unto n
# def upto_N(n) :
#     # base case
#     if n < 1 :
#         return

#     # rec
#     print(n)
#     upto_N(n-1) # assuming that it is going to print from 1 to n-1 
#     print(n)

#     # return
#     return # when you are returning nothing, None is return by default

# upto_N(5)

# # 1. factorial using recursion 

# def factorial_rec(n) :
#     # base case
#     if n == 0 or n == 1 :
#         return 1

#     # statements
#     fact_n1 = factorial_rec(n-1) # calling rec to find factorial of n-1
#     fact = n*fact_n1

#     # return statement
#     return fact

# print(factorial_rec(6))


# fibonacci
# 1, 1, 2, 3, 5, 8, 13, ...
# fn = fn_1 + fn_2

# def fibo(n) :
#     # base case
#     if n == 0 or n == 1 :
#         return 1
    
#     fn_1 = fibo(n-1)
#     fn_2 = fibo(n-2)

#     ans = fn_1 + fn_2

#     return ans

# print(fibo(7))

# pow x^y

# def power(x, y) :
#     # base case 
#     if y == 0 :
#         return 1

#     print(y)
#     ans = x*power(x, y-1)

#     return ans

# x = int(input())
# y = int(input())


# def power_opti(x, y) :
#     # base case 
#     if y == 0 :
#         return 1

#     print(y)
#     powerx_y_2 = power_opti(x, y//2)

#     ans = powerx_y_2 * powerx_y_2
#     if y%2 != 0 :
#         ans  = ans * x

#     return ans

# print(power_opti(2, 10))


"""
In - Built functions
"""

print(max(1,2,300,4,5,6,7))
print(min(10,2,300,4,5,6,7))

# import math

from math import ceil, floor

print(ceil(5.56))
print(floor(5.56))