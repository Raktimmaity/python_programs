# 4) Python Program for simple interest
# Method 1
def simpleInterest(p, t, r):
    print("The Principle is:", p)
    print("The time is:", t)
    print("The rate of interest is:", r)
    si = (p * t * r) / 100
    print("Simple Interest is: ", si)
simpleInterest(10000, 5, 5)
# Output:
# The Principle is: 10000
# The time is: 5
# The rate of interest is: 5
# Simple Interest is:  2500.0

# Method 2
def simpleInterest(p, t, r):
    print("The Principle is:", p)
    print("The time is:", t)
    print("The rate of interest is:", r)
    si = (p * t * r) / 100
    print("Simple Interest is: ", si)
P = int(input("Enter Principle: "))
T = int(input("Enter Time: "))
R = int(input("Enter rate of Interest: "))
simpleInterest(P, T, R)
# Output:
# Enter Principle: 10000
# Enter Time: 5
# Enter rate of Interest: 5
# The Principle is: 10000
# The time is: 5
# The rate of interest is: 5
# Simple Interest is:  2500.0