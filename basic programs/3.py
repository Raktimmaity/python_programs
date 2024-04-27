# 3) Python Program for factorial of a number.
# Method 1
def factorial(n):
    return 1 if(n == 0 or n == 1) else n * factorial(n - 1)
num = 5
print("Factorial of", num, "is:", factorial(num))
# Output:
# Factorial of 5 is: 120

# Method 2
import math
def factorial(n):
    return (math.factorial(n))
num = 5
print("Factorial of", num, "is:", factorial(num))
# Output:
# Factorial of 5 is: 120