# Python Program to add two numbers
# Method 1
a = 2
b = 3
sum = a + b
print("Result of", a, "and", b, "is:", sum)
# Output:-
# Result of 2 and 3 is: 5

# Method 2
a = int(input("Enter your first Number: "))
b = int(input("Enter your second Number: "))
result = a + b
print("Sum of", a, "and", b, "is:", result)
# Output:-
# Enter your first Number: 2
# Enter your second Number: 3
# Sum of 2 and 3 is: 5

# Method 3
def sum(a ,b):
    return a + b
num1 = 5
num2 = 3
result = sum(num1, num2)
print("Sum of {0} and {1} is: {2}" .format(num1, num2, result))
# Output:-
# Sum of 5 and 3 is: 8

# Method 4
import operator
num1 = 5
num2 = 5
result = operator.add(num1, num2)
print("Sum of {0} and {1} is: {2}" .format(num1, num2, result))
# Output:-
# Sum of 5 and 5 is: 1

# Method 5
sum = lambda x, y : x + y
num1 = 5
num2 = 3
result = sum(num1, num2)
print("Sum of {0} and {1} is: {2}" .format(num1, num2, result))
# Output:-
# Sum of 5 and 3 is: 8
