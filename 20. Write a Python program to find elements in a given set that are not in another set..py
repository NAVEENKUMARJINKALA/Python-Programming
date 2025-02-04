#20. Write a Python program to find elements in a given set that are not in another set.
set_1={'naveen','kumar','thundersoft'}
set_2={'Trinadh','reddy','thundersoft'}
def checkdiff(set1,set2):
    return set1-set2

print(checkdiff(set_1,set_2))
def checkdif(set1,set2):
    return set1.difference(set_2)

print(checkdif(set_1,set_2))