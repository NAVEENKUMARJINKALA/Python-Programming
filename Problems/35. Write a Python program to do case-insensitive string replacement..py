#35. Write a Python program to do case-insensitive string replacement.
string_1=input("Enter input")
old=input("Enter word to replace")
new=input("Enter new word to replace with")
def stringreplace(string1,old,new):
    s=string1.lower().replace(old,new)
    return s
print(stringreplace(string_1,old,new))