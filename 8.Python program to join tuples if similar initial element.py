
# output=[]
# for i in range(len(tlist)):
#     print(i)
#     for j in range(i+1,len(tlist)):
#         if tlist[i][0]==tlist[j][0]:
#             output.append(tuple(tlist[i]+tlist[j][1:]))
# print(output)
#
# Initialize a list of tuples
tuple_list = [(1, 2), (1, 3), (2, 4), (1, 5), (2, 6), (3, 7)]
joined_tuples = {}

for tup in tuple_list:
    key = tup[0]
    if key in joined_tuples:
        joined_tuples[key] += tup[1:]
    else:
        joined_tuples[key] = list(tup)

# Convert the values in the dictionary back to tuples and print the result
print(joined_tuples)
result = [tuple(val) for val in joined_tuples.values()]
print("Joined tuples with similar initial elements:", result)
