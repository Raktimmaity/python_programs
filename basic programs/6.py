# 6) Python Program for Program to find area of a circle.
# Method 1
def areaOfCircle(r):
    PI = 3.142
    return PI * (r * r)
print("Area of a circle is:", areaOfCircle(5))
# Output:
# Area of a circle is: 78.55

# Method 2
import math
def areaOfCircle(r):
    return math.pi * (pow(r, 2))
print("Area of a circle is:", areaOfCircle(5))
# Output:
# Area of a circle is: 78.53981633974483