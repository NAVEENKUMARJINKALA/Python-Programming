#38. Write a program to find uncommon words from two strings.
def uncommon(string1,string2):
    set1=set(string1.split())
    set2=set(string2.split())
    newset=set1.symmetric_difference(set2)
    return newset

string_1=input("Enter a string")
string_2=input("Enter a second string")
print(uncommon(string_1,string_2))