
# 1. OverflowError:
# When result is too large to be represented.

import math

# a = math.exp(1000)
# print(a)

try:
    n = int(input("Enter the number for exponent : "))
    m = math.exp(n)
except OverflowError:
    print("Enter number less than 710")
except ValueError:
    print("Enter number only not alphabet")
except:
    print("Unknown error")

print("Program end")

# 2. KeyError:
# when kew is not present in the dictionary.

# d= {"name":"Rohan","age":25,"location":"Chembur"}
# print(d["name"])
# print(d["salary"])



# 3. NameError
# if name or object of that name is not present or defined

# a=20
# print(b)



# 4. ModuleNotFoundError

# import cycle



# 5. UnboundLocalError   m=m+1
# trying to add or modify global veriable from inside of a function

# m=10
# def modify():
#     m=m+1
#     print(m)
# m=50
# modify()




# 6. AttributeError
# Mentioned attribute does not found in a class 

# class A:
#     def exp(self):
#         self.a = "rohan"
#         self.b = "Mumbai"
# obj = A()
# obj.exp()
# print(obj.a)
# print(obj.b)
# print(obj.c)


# 7. FileNotFoundError
#  file does not found in given path

# with open("a.txt","r")as file:
#     file.read()




# 8. ImportError
# file is imported but module is not ptesent in the file.

# from package import simple_calc

# from package import difficult



# 9. NotADirectoryError: 
# when operating for a directory but mentioning a file insted of directory

# import os
# os.listdir(r"C:\Users\admin\Desktop\Rohan\function vscode\exception handling\package\complex_calc.py")



# 10. RecursionError :

# import sys
# print(sys.getrecursionlimit())

# def a():
#     print("Rohan")
#     a()

# a()
