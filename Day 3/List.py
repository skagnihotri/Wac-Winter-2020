# ord() -->  it is used to find the ascii value
# print(ord('a'))
# print(chr(97))


"""
List Data structure
"""

# list defination
# student = ['abc', 'xyz', 'wxy', '23']

# print(student)
# print(type(student))

# a = [1, 'abc', True, 10.1] # list containing all the data types
# print(a)
# len() --> it returns the length of list
# print(len(a)) 

# a = [1,2,3,4,5,6]

# print(a[5])
# print(a[-3])

"""
for i in name_list :
    statements
"""
# a = [1, True, "abc", 2,3,4,5,6]
# # for loop to print a list
# for i in a :
#     print(i)

# # for loop using indexing
# for i in range(len(a)) :
#     print(a[i])

# # while loop
# i = 0
# while i < len(a) :
#     print(a[i])

#     i += 1


"""
Taking input
"""
# s = input().strip().split()

# print(s)
# print(type(s))

# for i in range(len(s)) :
#     s[i] = int(s[i])

# print(s)

"""
List comprehension
"""
# a = list(range(1, 11))
# print(a)

# a = [i+10 for i in a if i%2 == 0]
# print(a)

# a = [9*i for i in a] # each value gets multiplied by 9
# a = [i+5 for i in a] # each value gets increased by 5
# a = [i*i for i in a] # list comprehension each value gets multiplied by itself
# print(a)


# n = [int(i) for i in input().strip().split()]

# print(n)

# print(max(n))
# print(min(n))
# print(sum(n))

# list slicing 
"""
list_name[start_index : end_index]
"""

# a = [1,2, 34,4,5,6,7,8] # 0-7 indexing

# # print(a[:]) # by default start index is 0 and end index is last index
# print(a[3:5])

# print(a[::-1]) # it is going to reverse the list

# inbuilt functions
a = [1,1,1]

# inserts elements at last
a.append(10)
a.append(100)
a.append(50)
print(a)

# insert at a position
a.insert(0, 4) # insert(pos, value)
print(a)

# deleting at last
a.pop()
print(a)

# to remove the first occurance
a.remove(1)
print(a)

# sorting a list
print(sorted(a, reverse= True))


# code

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first = -1e10
    second = -1e10
    
    # print(first, second)
    for i in arr :
        
        if i > first :
            second = first
            first = i
        elif i > second and i < first:
            second = i
            
    print(second)