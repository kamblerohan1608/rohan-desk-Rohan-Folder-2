
# zip :

# compressing lists into a single object.


ls1 = ["Rohan",25,"Kurla"]
ls2 = ["Sargam",36,"Vashi"]
ls3 = ["Seema",26,"Wadala"]
ls4 = ["Jakkie",45,"Sion"]

data = list(zip(ls1,ls2,ls3,ls4))
print(data)

data1 = [('Rohan', 'Sargam', 'Seema', 'Jakkie'), (25, 36, 26, 45), ('Kurla', 'Vashi', 'Kurla', 'Kurla')]

# no. of columns :

print(len(data1))

# no. of rows :

print(len(data1[0]))

# To unzip the data :

a,b,c,d = zip(*data1)

print(a)
print(b)
print(c)
print(d)