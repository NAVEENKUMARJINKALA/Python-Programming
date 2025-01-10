from PIL.ImageChops import difference

original_list = [10, 20, 30, 40, 50]

duplicated_list = [30, 40, 40, 50, 60, 70, 70]

set1=set(original_list)
set2=set(duplicated_list)

difference=set1-set2
print(difference)

result=[item for item in duplicated_list if duplicated_list.count(item)>1]
print(result)
