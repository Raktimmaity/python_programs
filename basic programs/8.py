# 8) Check wheather a number is prime or not
# Method 1
num = int(input("Enter a number: "))
if num == 1:
    print("This is not a prime number")
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")
# Output:
# Enter a number: 6
# This is not a prime number

# Enter a number: 11
# This is a prime number

# Method 2
