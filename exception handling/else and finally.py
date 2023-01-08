
# else block, finally block 

# Example 1

try:
    n = int(input("Enter the number : "))
    m = int(input("Enter the number : "))
    print(f"division is {n/m}")
except ValueError:
    print("only integers allowed.")
else:
    print("Program executed.")
finally:
    print("I am gonna be printed any way !!!")
