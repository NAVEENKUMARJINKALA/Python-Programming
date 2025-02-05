# #17. Write a Python program to compute the sum of all the elements of each tuple stored inside a list
# of tuples.
tuple_1=[(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 20, 30)]
def sumoftuple(tuple):
    return [sum(t) for t in tuple_1]

print(sumoftuple(tuple_1))


