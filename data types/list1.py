
# list data type : 


# # ways to create a list

# 1.

# ls = []
# print(type(ls))


# 2.

# ls = list()
# print(type(ls))


# # adding element into a list 


# append() :

# ls = []
# name = "rohan"
# age  = 25
# location = "Vashi"
# ls.append(name)
# print(ls)
# ls.append(age)
# print(ls)
# ls.append(location)
# print(ls)


# insert() :

# ls = ["Rohan",25,"kurla"]
# ls.insert(0,"sion")
# print(ls)

# ls.insert(2,"sagar")
# print(ls)


# extend() :


# ls = ["rohan",22,"Suman"]
# name = ["Kira","light",5656]
# ls.extend(name)
# print(ls)

# ls = ["rohan",22,"Suman"]
# ls.extend("ROHAN")
# print(ls)



# # accessing element from a list 


# list follows index positioning system
# Two ways to mention position of element in index positioning system

# forward index
# (0,1,2,3,4)
#(left - right)

# reverse index
#(-5,-4,-3,-2,-1)
#(right - left)

# accessing a single element :

# forward index

# ls = ["rohan",22,"Suman","Kira","light",5656]
# ls1 = ls[3]
# print(ls1)

# reverse index

# ls2 = ls[-4]
# print(ls2)

# accessing multiple elements  / list slicing

# forward index

# ls = ["rohan",22,"Suman","Kira","light",5656]
# ls1 = ls[0:3]
# print(ls1)

# reverse index 

# ls2 = ls[-5:-1]     # for accessing till -2 have to mention -1 as system adds -1 in it 
# print(ls2)

 
# # deleting element from list 



# remove():              # takes one argument (name)

# ls = ["rohan",22,"Suman","Kira","light",5656]

# ls.remove("Kira")
# print(ls)


# pop()                  # takes one argument (position)


# ls = ["rohan",22,"Suman","Kira","light",5656]
# ls.pop()                                        # by default delets last element
# print(ls)

# ls.pop(3)
# print(ls)

# ls.pop(-1)
# print(ls)


# del                         # it is a key word and can be used anywhere in whole program


# ls = ["rohan",22,"Suman","Kira","light",5656]
# del ls[1]
# print(ls)

# del ls[1:3]
# print(ls)

# del ls
# print(ls)

ls = [1,2,3,4]
ls1 = ls.copy()
print(ls1)









