"""
Dict --> it is a data structure which stores key - value pairs.

"""

# phone book 
# name : phone no

# a = {"rohan" : 1234, 
#     'abc' : 2456,
#     'yusda' : 12456, 
#     456 : ['a', 'b', 'c', {'a' : 0, 'b' : 1}]}

# print(a)
# print(type(a))

# print(a.keys()) # returns the keys of the dict

# print(a.values()) # returns values from the dict

# print(a.items()) # it returns key value pairs

# specific element access
# print(a[456]) # dict_name[key]
# print(a['rohan'])

# # Loops 
# for key in a.keys() :
#     print(f"{key} --> {a[key]}")

# print('--------------------')
# for key, value in a.items() :
#     print(f"{key} --> {value}")

# print(a[456][3].values())

# updating dict

# adding new key value pair
# a['qwerty'] = 100

# # update
# a['rohan'] = 78945
# a.update({'abc' : 45689})
# print(a)

# # to delete a key - value pair
# del(a['qwerty'])

# print(a)

# # to delete all key - value pairs from dict
# a.clear()
# print(a)

# def count_freq(s) :
#     freq_dict = {} # empty dict

#     for i in s :
#         if freq_dict.get(i) == None :
#             freq_dict[i] = 1
#         else :
#             freq_dict[i] += 1
    
#     # print(freq_dict)
#     for k, v in freq_dict.items() :
#         print(f"{k} --> {v}")
#     return

# count_freq('asdasdcbsakdadf')

# sets 

# a = [1,2,3,45,1,2,3,4,5,6,7,3,4,5,6,7]
# print(a)

# b = set(a) # set() is a function to make a set

# print(b)
# print(type(b))

# for i in b :
#     print(i)

# # tuples

# a = (1,2,3,4,5,6,7, 2,3,4,5,1)

# print(a)

# print(type(a))

# # a[2] = 10 # error immutable

# print(a[2])

# print(len(a))

# for i in a :
#     print(i)

# create a tuple with a single value 1
# a = (1,)

# print(a)
# print(type(a))


# def fun(s):
#     # return True if s is a valid email, else return False
#     if len(s) < 5 :
#         return False
        
#     if '@' not in s :
#         return False
    
#     if '.' not in s :
#         return False
    
#     flag1 = s.find('@')
#     flag2 = s.find('.')
    
#     if flag1 > flag2 :
#         return False
    
#     if flag1 == 0 or flag2 == len(s)-1 :
#         return False
        
#     count1 = list(s).count('@')
#     count2 = list(s).count('.')
#     if count1 > 1 or count2 > 1 :
#         return False
    
#     # 'username'  'websitename' 'extension'
#     temp = s.split('@')
#     user_name = temp[0]
    
#     temp1 = temp[1].split('.')
#     website = temp1[0]
#     extension = temp1[1]
    
#     if len(extension) > 3 :
#         return False
    
#     for i in website :
#         if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9') :
#             continue
#         else :
#             return False
    

#     for i in user_name :
#         if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9') or i == '-' or i == '_':
#             continue
        
#         return False
    
#     return True