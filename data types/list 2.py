
# Some extra methods of list


# copy()                   # makes an exact copy of a list

# ls = [1,2,3,4,5,6,7,8,9]
# ls1 = ls.copy()
# print(ls1)

# index()                  # returns the index of the mentioned data

# ls = ['a','b','c','k','l']

# ls1 = ls.index('k')
# print(ls1)

# count()

# ls = ['a','b','c','k','l','a','b','k','a','b','c','k','l']
# ls1 = ls.count('k')
# print(ls1)

# sort()

# ls = ['a','b','c','k','l','m','n','g']
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# clear()

# ls = ['a','b','c','k','l']
# ls.clear()
# print(ls)

# # Comprehension :

# This is the technique to compress the logic of list 
# This is done on existing list to form a new list.

# Problem 1 :

# form a list reverse of list ls without using any direct function.

ls = [1,2,3,4,5,6,7]
ls1 = []
for i in range (len(ls)-1 , -1, -1 ):
    ls1.append(ls[i])

print(ls1)

# In comprihension we can write it as :

ls1 = [ls[i] for i in range (len(ls)-1 , -1 , -1)]
print(ls1)

# Problem 2 :

# find positive and negetive from the list : 

ls = [1,56,-56,-45,-415,-465,-42,-656,23,48,9546,356,47,6,4]
pos = []
neg = []

for i in ls:
    if i<0 :
        neg.append(i)
    else :
        pos.append(i)

print(pos)
print(neg)

# In comprihension we can write it as :

# when only if is used :

pos = [i for i in ls if i>0]
print(pos)

# when if and lese both are being used :

neg = []
pos = [i if i>0 else neg.append(i) for i in ls]
print(pos)
print(neg)

# for handling none situation we have to use filter : 

# filter(function,itterable data)
# function can be normal function on a lambda function

def fil(data):
    return data != None

pos1 = list(filter(fil,pos))

print(pos1)
