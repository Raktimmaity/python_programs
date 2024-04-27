# 5) Python Program for compound interest
# Method 1
def compoundInterest(p, r, t):
    amount = p*(pow((1 + r/100), t))
    ci = amount - p
    print("Compound Interest is:", ci)
compoundInterest(10000, 10.25, 5)
# Output:
# Compound Interest is: 6288.946267774416

# Method 2
p = 10000
t = 5
r = 10.25
amount = p * (1 + (r / 100)) ** t
ci = amount - p
print("Compound Interest is:", ci)
# Output:
# Compound Interest is: 6288.946267774416

# Method 3
def compoundInterest(p, r, t):
    amount = p*(pow((1 + r/100), t))
    ci = amount - p
    print("Compound Interest is:", ci)
P = int(input("Enter the Principle: "))
R = float(input("Enter rate of Interest: "))
T = int(input("Enter Time: "))
compoundInterest(P, R, T)
# Output:
# Enter the Principle: 10000
# Enter rate of Interest: 10.25
# Enter Time: 5
# Compound Interest is: 6288.946267774416