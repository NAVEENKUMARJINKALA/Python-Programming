#31. Write a Python program to filter a given list to determine if the values in the list have a length of
#6 using Lambda.
list_1=list(map(str,input("ËNter a list").split()))
def getlegth(lst):
    length=list(filter(lambda x: len(x)>=6,lst))
    return length
print(getlegth(list_1))