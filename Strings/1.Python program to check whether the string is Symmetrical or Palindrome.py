str=input("Enter a string as input")
length=len(str)
strrev=str[::-1]
print(strrev)
if str==strrev:
    print("the string is a palindrome")
else:
    print("String is not palindrome")

def is_symmetric(str):
    value = str  # Convert to string for comparison
    return value == value[::-1]

print(is_symmetric(str))
