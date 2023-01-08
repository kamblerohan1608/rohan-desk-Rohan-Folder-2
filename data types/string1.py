
# # string datatype : 

# string is a document type data. All texual data is represented as string. defined by ' ' or " ".
# string ia a non mutable data type i.e. we can not change its memory location.
# ( we cannot delete specific data at a perticular position directly without using its own methods e.g. del test(0) will give us error ) 
#  this is the way to show that string is immutable data type.

# types of string : 

# 1.  Normal string :

# a = "i am rohan"

# 2.  Multi line string :

# print('''my name is "Rohan" 

# i am 24 years old''')

# 3.  Raw string :

#os.system(r"desktop\rohsn\null\abc.mp4")

#print("Rohan \n Kamble")

# # Methods in string : 

# string formating :

# a = 10
# b = 20

# print("addition of ",a,"and",b,"is :",a+b)

# 1.  format method :

# Method 1 :

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# print("My name is {} my age is {}".format(name,age))

# Method 2 :

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# print("My name is {1} my age is {0}".format(age,name))
 
# 2.  F string :

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# print(f"My name is {name} my age is {age}")

# 3.  mod string (%):

#%s : string data
#%d : digit data
# %s and %d just defines that in what form data should be present at the mentioned position. 

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# print("My name is %s my age is %d" %(name,age))

# # Escape sequences :
# 
#  \  : 
#       '\' cancels the special characteristics of functions used inside the string just before that.
#       e.g.  \"  in this '\' will cancel out the functionality of  ' " ' inside a string.

# st = "This is \"python\" class."

# print(st)


#  \n , \t   :
#               \n prints in new line
#               \t tab space

# st = "\tHello !!! \n\tThis is python." 
# print(st)

# # replace('old data','new data')   :     relpaces old data with new data


# st = "This is python. python is easy."
# st1 = st.replace("python","Java")
# print(st1)


# # upper ()  :            returns upper case


# st = "python"
# st1 = st.upper()
# print(st1)


# # lower ()  :              returns lower case


# st = "PYTHON"
# st1 = st.lower()
# print(st1)


# # capitalize ()  :           returns as first letter capital


# st = "python"
# st1 = st.capitalize()
# print(st1)


# # center ()  :                retuns with no of spaces added in the string


# st = "python"
# st1 = st.center(100)
# print(st1)


# # strip ()  :                    retuns the string removing the spaces from start and end


# st = "                                 python                               "
# st1 = st.strip()
# print(st1)


# # split ()  :                          splits the string data and returns a list


# st = "Python is a good language."
# st1 = st.split()
# print(type(st1),st1)


# # join ()  :                           returns the string ay joining the data of list


# st = ["Python","is","a","good","language."]
# st1 = ' '.join(st)
# print(type(st1),st1)


# # isupper ()  :                       returns true if data is of upper case                


# st = "PYTHON"
# print(st)
# if st.isupper():
#     print("Upper data.")
# else:
#     print("Mixed data")


# # islower ()  :                           returns true if data is of lower case


# st = "python"
# print(st)
# if st.islower():
#     print("lower data.")
# else:
#     print("Mixed data")


# # isdigit ()  :                            returns true if data in the string is of digit data

# st = "1234"
# print(st)
# if st.isdigit():
#     print("Digit data.")
# else:
#     print("Mixed data")

