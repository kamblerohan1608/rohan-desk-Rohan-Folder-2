
# Dictionary : {} 

# It is built-in data structure in python. 
# It is an unordered collection of data. 
# It does not follow any positioning system.
# It is a mutable data type.
# It consists of key and value.
# it is used for mapping (finding/locating) using keys.
# Dictionary allows us to store all data in a single object. 

# e.g.

#                               school
#                                 |
#                                 |
#        -----------------------------------------------------
#        |                        |                          |
#       8th                      9th                        10th
#        |                        |                          |
#    1st - 12                 1st - 37                    1st - 58
#    2nd - 46                 2nd - 89                    2nd - 10
#    3rd - 78                 3rd - 22                    3rd - 6

school = {"8th" : [12,46,78], "9th" : (37,89,22), "10th" : [58,10,6,(12,56,48)]}

# no of keys : 

k = len(school)
print(k)

# no of columns : 

v = len(school["8th"])
print(v)

# # accessing elements in a dictionary :

# 1. It is a kind of process :

# data = school["8th"][1]
# print(data)

# data1 = school["10th"][3][1]
# print(data1)

# 2. get()

# data2 = school.get("9th")
# print(data2)

# # adding elements in a dictionary

# 1. direct 

# school["11th"] = [1,2,3]
# print(school)


# 2. update()

# school.update({"12" : (34,48,73)})
# print(school)

# # Deleting elements :

# 1. pop() :

# deleting element from the the dictionary 

school.pop("9th")   # It will not delete last element by default as dtctionary is not an unordered collection 
print(school)

# 2. popiteam():

school.popitem()
print(school)

# 3. del 

del school["8th"][2]

print(school)

del school["8th"]
print(school)