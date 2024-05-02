# 9) Fibbonacci series
def Fibbo(num):
    if num <= 0:
        print("Incorrect Input")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return Fibbo(num - 1) + Fibbo(num - 2)

num = int(input("Enter a number: "))
print(Fibbo(num))
# Output:
# Enter a number: 10
# 34