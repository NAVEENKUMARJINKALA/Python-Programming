list_1=list(map(str,input("Enter a list separated by comma :").split(",")))
#print(list_1)
def revlist(list):
    return list[::-1]
print(revlist(list_1))


def rev(list1):
    list1.reverse()
    return list1

print(rev(list_1))