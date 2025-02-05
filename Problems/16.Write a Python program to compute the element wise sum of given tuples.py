# #Write a Python program to compute the element  -wise sum of given tuples. Original lists: (1, 2, 3, 4)(3, 5, 2, 1)(2, 2, 3, 1) Element-wise sum of the said
# tuples: (6, 9, 8, 6)
tuples_1=[(1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1) ]
new=list(zip(*tuples_1))
print(new)
def element_wise_sum(*tuples):
    return tuple(map(sum, zip(*tuples)))

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

result = element_wise_sum(tuple1, tuple2, tuple3)
print("Element-wise sum of the said tuples:", result)