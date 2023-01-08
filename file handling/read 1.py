
# read permission  :  
# read()  , readline()   , readlines()


# read()

# Two ways to write file handling program  :

# 1. direct :

# file = open( "test1.txt","r")
# data = file.read()                             # read ()  : allows all data to be read in string form
# print(data)

# file.close()


# # 2. professional :

# with open("test1.txt","r") as file :
#     data = file.read()
#     print(data)

# readline()

# readline()

# 1. direct 


# file = open("test1.txt","r")
# data = file.readline()
# print(data)

# file.close()

# # 2. professional

# with open("test1.txt","r") as file :
#     data = file.readline()
#     print(data)

# readlines()

# 1. direct

# file = open("test1.txt","r")
# data = file.readlines()
# print(data)


# file.close()


# # 2. professional

# with open("test1.txt","r") as file:
#     data = file.readlines()
#     print(data)
