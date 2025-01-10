
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
list1.sort()
list2.sort()
set1=set(list1)
set2=set(list2)

print(set1)
print(set2)
missingvalue=set1-set2
addvalue=set2-set1
print(missingvalue)
print(addvalue)
