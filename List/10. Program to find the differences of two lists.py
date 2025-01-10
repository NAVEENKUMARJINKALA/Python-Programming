list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
print(list1)
print(list2)
difference1= [item for item in list1 if item not in list2]
print(difference1)

difference2=[item for item in list2 if item not in list1]
print(difference2)

set1=set(list1)
set2=set(list2)
#print(set1,set2)
symmetric=list(set1 ^ set2)
print(symmetric)
S=sorted(symmetric)
print(S)
