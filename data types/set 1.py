
# set   {} :

# declaration :

s = set()
print(type(s))


# adding element :

# add() :

ls = [1,2,3,4,5,6,7,8,9]

# for i in ls:
#     s.add(i**2)
# print(s)

# comprihension :

# s = { i**2 for i in ls }
# print(s)


# update() :

# s.update('Rohan',"Sangam")
# print(s)

# delete elements :

# # remove() :

# s = {1,2,3,4,5,6,7,8,9}
# s.remove(7)
# print(s)

# # pop()  :

# s.pop()
# print(s)

# # discard () :

# s.discard(4)
# print(s)

# accessing elements :

# Accessing element from a set is not possible directly.
# but can be accessed bt two processes.
#  1. by typecasting       2. by loop


# Q. take a set s = {1,2,3,4,5,6,7,8,9}
# generate an output as a set of square of each element of set s.

s = {1,2,3,4,5,6,7,8,9}
s1 = set()
for i in s:
    s1.add(i**2)
print(s1)

# comprehension :

s2 = {i**2 for i in s}
print(s2)