# 27. Write a Python function that accepts a string and counts the number of upper and lower case
# letters.
from Assignments.tables import lcount


#print(string_1)

def stringcount(string):
    lcount = 0
    ucount = 0
    for s in string:
        if s.isupper():
            ucount+=1
        elif s.islower():
            lcount+=1
    return f"upper case count is {ucount},lowercase count is {lcount}"
string_1=list(map(str,input("Enter a string with upper and lower case letters:")))
print(stringcount(string_1))


def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    return {"Uppercase": upper_count, "Lowercase": lower_count}