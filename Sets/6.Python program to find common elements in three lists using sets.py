list1=[1,2,3,4,5,6,7,8,9,0]
list2=[10,20,3,0,40,6,0,50,6,70]
list3=[97,67,8,7,0,5,1,22,33,665,789]

set1=set(list1)
set2=set(list2)
set3=set(list3)

#print(set1," ",set2," ",set3)
common_in_three=set1.intersection(set2,set3)
common_in_three1=set1.intersection_update(set2,set3)
print(common_in_three1)
common_in_three3=set1.union(set2,set3)
print(common_in_three3)
