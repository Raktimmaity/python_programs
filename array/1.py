# 1) Python Program to Find Sum of Array
# Method 1
def Sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

arr = [1, 2, 3]
res = Sum(arr)
print("Sum of array is: ",res)
# Output:
# Sum of array is:  6

# Method 2
arr = [1, 2, 3]
print("Sum of Array is: ", sum(arr))
# Output:
# Sum of Array is:  6
