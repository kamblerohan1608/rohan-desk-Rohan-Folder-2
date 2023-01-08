
# practice questions

# Q.1  add 3 dictionaries to be one

# d1 = {10:23,50:56}
# d2 = {78:51,56:96}
# d3 = {12:74,36:47}

# d4 = {}

# for i in d1,d2,d3:
#     d4.update(i)
# print(d4)

# Q.2  find whether key already exists


# d1 = {"name" : "Rohan", "age" : 54, "location" : "Kurla"}

# def key_present(x):
#     for i in d1:
#         if x == i:
#             print("key already present.")
# key_present("age")


# Q.3  itterate keys and values

# d1 = {"name" : "Rohan", "age" : 54, "location" : "Kurla"}

# print(d1.items())

# for d1_keys,d1_values in d1.items():
#     print(d1_keys, "-" ,d1_values)

# Q..
# Method 1

# ls = [1,2,3,4,5,6]
# ls1 = ["a","b","c","d","e","f"]
# d={}
# for i in range(len(ls1)):
#     d[ls1[i]] = ls[i]

# print(d)

# # Method 2 :

# ls = [1,2,3,4,5,6]
# ls1 = ["a","b","c","d","e","f"]

# z = list(zip(ls1,ls))
# print(z)
# d1 = {}
# for i,j in list(zip(ls1,ls)):
#     d1[i] = j
# print(d1)

# # comprehension :

# d3 = { i:j for i,j in list(zip(ls1,ls))}
# print(d3)

# z1 = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]

# a,b = zip(* z1)
# print(a,b)

ls = [1,2,3,4,5,6]
ls1 = ["a","b","c","d","e","f"]


d = { "name" : "Rohan" , "age" : 23 , "location" : "Mumbai"}


for i,j in d.items():
    print(i,":", j)

print(d.keys())
print(d.values())

d1 = zip(d)
