# 12) print ascii value of a given character
def ascii(c):
    result = ord(c)
    return result
character = str(input("Enter an alphabet: "))
print(ascii(character))
# Output:
# Enter an alphabet: g
# 103