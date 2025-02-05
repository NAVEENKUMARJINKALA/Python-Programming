#28. Write a Python function that takes a list and returns a new list with distinct elements from the
#first list.

def checkuniquelist(list):
    uniquelist=[]
    j=[l for l in list if not (l in uniquelist or uniquelist.append(l))]
    return uniquelist
#     for l in list:
#         if l not in uniquelist:
#             uniquelist.append(l)
#     return uniquelist
#

list1=list(map(str,input("ENter a list :").split()))
print(checkuniquelist(list1))



