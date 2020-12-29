# st = "python"

# print(st)
# print(type(st))
# print(len(st)) # it is used to find the length of the string

# # loop 
# for i in st:
#     print(i) 

# print('--------------------')
# for i in range(len(st)) :
#     print(st[i])

# print('------------')
# i = 0
# while i < len(st) :
#     print(st[i])

#     i += 1

# # 1. count freq of vowels
# def count_vowels(s) :
#     count = 0

#     for i in s :
#         if i in ['a', 'e', 'i', 'o', 'u'] :
#             count += 1
    
#     return count

# print(count_vowels('hello'))
# print(count_vowels('python'))

# # 2. count freq of each character
# def count_freq(s) :
#     # intialize
#     freq_list = [] # empty list
#     for i in range(26) :
#         freq_list.append(0)
    
#     # loop for counting freq
#     for i in s :
#         ascii = ord(i) - 97 # ord() is a function to find ascii value of a char
#         freq_list[ascii] += 1
    
#     print(freq_list)

#     # loop for printing freq
#     for i in range(len(freq_list)) :
#         if freq_list[i] != 0 :
#             print(chr(i+97), '-->' , freq_list[i]) # chr() fun which print char from ascii


# count_freq('python')
# count_freq('aababcdz')

"""
Indexing in python string

same as in list
"""

# s = "abcd"
# print(s)

# print(s[3])
# print(s[-2])

# 1. to check a string is pallindrome or not
# def pallin(s) :
#     start = 0
#     end = len(s) - 1

#     while start < end :
#         if s[start] != s[end] :
#             return False

#         start += 1
#         end -= 1

#     return True

# print(pallin('python'))
# print(pallin('wow'))
# print(pallin('racecar'))

"""
string formating

using f strings
"""

# for i in range(1, 6) :
#     print(f"cur number is {i}")

# a = ['abc', 'ram', 'xyz', 'shyam'] # list is according to rollNo
# for i in range(len(a)) :
#     print(f"roll no is {i+1} and name is {a[i]}.")

"""
Sclicing in strings

same as in list
"""
# s = "winter"

# print(s[:])
# print(s[1:3])
# print(s[:4])
# print(s[3:])
# print(s[::-1])

# 1. pallindrome

# def pallindrome(s) :
#     return s == s[::-1] # string is equal to reverse string

# print(pallindrome('python'))
# print(pallindrome('wow'))
# print(pallindrome('racecar'))

"""
inbuilt functions

strip() --> removes starting and ending spaces
split() --> splits the string on a particular char
len() --> length of the string
upper() --> lower to upper
lower() --> upper to lower
isupper() --> checks wheather upper case or not
islower() --> checks wheather lower case or not
find() --> index of the char to be find
 + --> it is used for concatenation
"""

# s = '   abcdXYZ   '
# s = s.strip()
# print(s)

# print(s.upper())

# print(s.lower())

# print(s.isupper())

# print(s.islower())

# print(s.find('cd'))

# print('asdf' + 'XCV')

"""
Imutability
"""

a = [1, 10, 100] # list are mutable
a[1] = 50
print(a)

b = 'abcd' # strings are immutable
# b[2] = 'z' # error
b = list(b)
b[2] = 'z'
b = ''.join(b)
print(b)

