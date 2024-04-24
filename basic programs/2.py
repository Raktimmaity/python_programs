# Maximum of two numbers
# Method 1
num1 = 5
num2 = 4
print("Maximum number is: ", max(num1, num2))
# Output
# Maximum number is:  5

# Method 2
num1 = 5
num2 = 7
if num1 >= num2:
    print(num1, "is maximum number")
else:
    print(num2, "is minimum number")
# Output:
# 7 is minimum number

# Method 3
def maximum(a, b):
    if(a >= b):
        return a
    else:
        return b
num1 = 5
num2 = 4
result = maximum(num1, num2)
print("Maximum number is: {0}" .format(result))
# Output:
# Maximum number is: 5

# Method 4
maximum = lambda a, b : a if a > b else b
print(f'{maximum(5, 4)} is the maximum number')
# Output:
# 5 is the maximum number

# Method 5
a = 2
b = 3
print(a if a > b else b)
# Output:
# 3