#36. Write a program to remove the i th character in the string.

string_1=input("Enter a string")
def removechar(string,n):
    return string[:n]+string[n+1:]

print(removechar(string_1,2))