
# User defined exceptions:

# In user defined errors we have to handle the error that we have made.

# Example 1:

# class LargeError(Exception):
#     pass
# class SmallError(Exception):
#     pass
# import random
# try:
#     guess = random.randint(1,6)
#     print(guess)
#     n=int(input("Enter the number : "))
#     if n > guess:
#         raise LargeError
#     elif n < guess:
#         raise SmallError
#     else:
#         print("Correct Guess")
# except LargeError :
#     print("The number is larger.")
# except SmallError:
#     print("The number is smaller.")

# print("Program finished")



# Example 3

# import random


# class LargeError(Exception):
#     def __init__(self,msg,level):
#         self.msg = msg
#         self.level = level
# class SmallError(Exception):
#     def __init__(self,msg,level):
#         self.msg = msg
#         self.level = level
# guess = random.randint(1,6)
# print(guess)
# n=int(input("Enter the number : "))
# if n > guess:
#     raise LargeError("Entered number is larger.","level = 2")
# elif n < guess:
#     raise SmallError("Entered number is smaller.","level = 3")
# else:
#     print("Correct Guess")



# class LargeError(Exception):
#     pass
# class SmallError(Exception):
#     pass
# while True:
#     try:
#         x = int(input("Enter The Number : "))
#         if x>3:
#             raise LargeError
#         elif x<3:
#             raise SmallError
#     except LargeError:
#         print("Large error")

#     except SmallError:
#         print("small error")

#     else:
#         print("Corrcet number.") 
#         break