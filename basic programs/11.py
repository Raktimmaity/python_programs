# 11) cube of n natural numbers
def natural(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i * i)
    return sm

num = int(input("Enter a number: "))
print(natural(num))