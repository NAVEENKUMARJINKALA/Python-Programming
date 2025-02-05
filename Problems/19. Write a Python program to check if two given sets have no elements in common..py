#19. Write a Python program to check if two given sets have no elements in common.

set_1={'naveen','kumar','thundersoft'}
set_2={'Trinadh','reddy','thundersoft'}

def tocheckset(set1,set2):
    #return set_1.intersection(set_2)
    return set_1.isdisjoint(set_2)
print(tocheckset(set_1,set_2))

def tocheck(set1,set2):
    return len(set_1&set_2)
print(tocheck(set_1,set_2))