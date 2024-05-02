# 7) Python Program to Print all Prime numbers in an Interval
# Method 1
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
for num in range(lower, upper):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)