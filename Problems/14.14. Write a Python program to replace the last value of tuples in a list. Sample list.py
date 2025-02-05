# #14. Write a Python program to replace the last value of tuples in a list. Sample list: [(10, 20, 40),(40,
# 50, 60),(70, 80, 90)] Expected Output:[(10, 20, 100),(40, 50, 100),(70, 80, 100)]
sample_list=[(10, 20, 40),(40,50, 60),(70, 80, 90)]
#Expected Output:[(10, 20, 100),(40, 50, 100),(70, 80, 100)]
def replace_last_value(lst, new_value):
    updated_list = []
    for t in lst:
        updated_tuple = t[:-1] + (new_value,)
        updated_list.append(updated_tuple)
    return updated_list

def replacelist(lst,new_value):
    updatedlist=[]
    for t in list:
        updatedlist=t[:-1]+ new_value



def replace_last_value(lst, new_value):
    return [t[:-1] + (new_value,) for t in lst]
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
updated_list = replace_last_value(sample_list, new_value)
print(updated_list)
def rplc(lst,newvalue):
    return [t[:-1]+ (newvalue,) for t in lst]

print(rplc(sample_list,500))