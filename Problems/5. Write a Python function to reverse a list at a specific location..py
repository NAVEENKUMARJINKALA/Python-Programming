list1=[1, 2, 3, 4, 5, 6]
print(type(list))
def reverse1(list,index):

    if index==0 or index>=len(list):
        raise ValueError("Index out of range.")
    return list[:index]+list[index:][::-1]


print(reverse1(list1,4))