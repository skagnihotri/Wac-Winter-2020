# While Loop

# i = 0 # start 

# while i < 5 : # condition
#     print(i)
#     i += 1 # i = i + 1 # increament

# print(i)

# for i in range(0, 5, 1) :
#     print(i)

# odd numbers in range 1 - 20 
# for i in range(1, 20, 2) :
#     print(i)

# odd numbers in reverse order
# for i in range(19, 0, -2) :
#     print(i)

# 1. sum of n natural numbers
# n = int(input())
# n = int(input())

# sum = 0
# for i in range(1, n+1) :
#     sum += i

# print("Sum is :", sum)

# 2. Factorial
# n = int(input())

# fact = 1
# for i in range(1, n+1) :
#     fact = fact*i

# print("Factorial is :", fact)

# to swap to number
# a, b = 5, 10
# print(a)
# print(b)
# a, b = b, a
"""
temp = a
a = b
b = temp
"""
# print(a)
# print(b)

# nested loops
# for i in range(5) :
#     for j in range(5) :
#         print(i, end = ' ')
#     print()

# 1. star patter
"""
n = 5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# n = int(input())

# for i in range(n) :
#     for j in range(n) :
#         print('* ', end = ' ')
#     print()

# using string manipulation
# for i in range(n) :
#     print('* '*n)

"""
n = 4
*
* *
* * *
* * * *
"""
# n = int(input())

# for i in range(n) :
#     for j in range(i+1) :
#         print('*', end = ' ')
#     print()

# for i in range(n) :
#     print('* '*(i+1))
    
"""
Break and Continue statements
"""

# for i in range(10) :
#     # print(i)
#     if i%2 == 0 :
#         continue # loop skiping statement

#     if i == 7 :
#         break # loop exiting statement

#     print(i)

# print(i)

# 1. check a number is prime or not

# n = int(input())

# # temp = int(n**0.5)
# is_prime = True
# for i in range(2, n) : # [2, n-1], [2, n//2 +1], [2, sqrt(n)+1]
#     if n%i == 0 : # n is multiple of i
#         is_prime = False
#         break

# if is_prime :
#     print("It is a Prime Number")
# else :
#     print('Not a Prime Number')


# nCr




"""
strip() :- It removes the starting and ending white spaces
split() :- It splits the string on the basis of character provided
"""
s = '   today is a good day!!    '
print(s)
print(s.strip())
print(s.strip().split('y'))

