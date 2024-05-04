# 2) Python Program to Find Largest Element in an Array.
# Method 1
def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [20, 10, 20, 4, 100]
n = len(arr)
result = largest(arr, n)
print("Largest element in the array is: ", result)
# Output:
# Largest element in the array is:  100

# Method 2
arr = [20, 10, 20, 4, 100]
print("Largest element in the array is: ", max(arr))
# Output:
# Largest element in the array is:  100

# Method 3
import operator
arr = [20, 10, 20, 4, 100]
max = 0
for i in arr:
    if operator.gt(i, max):
        max = i
print("Largest element in the array is: ", max)
# Output:
# Largest element in the array is:  100