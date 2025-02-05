# #15. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple: ((10, 10, 10, 12),(30, 45, 56, 45),(81, 80, 39, 32),(1, 2, 3, 4)) Average value of the
# numbers of the said tuple of tuples: [30.5, 34.25, 27.0, 23.25]
Original_Tuple=((10, 10, 10, 12),(30, 45, 56, 45),(81, 80, 39, 32),(1, 2, 3, 4))
transposed = list(zip(*Original_Tuple))
print(transposed)
def tuple_average(tuple):
    update= [t[0] for t in tuple]
    return  sum(update)/len(Original_Tuple)

def tupleaverage(tupleaa):
    print(tuple_average(Original_Tuple))
    averages = [sum(col) / len(col) for col in transposed]

    return averages
print(tupleaverage(Original_Tuple))
print(tuple_average(Original_Tuple))

#Write a Python program to compute the element wise sum of given tuples. Original lists: (1, 2, 3, 4)(3, 5, 2, 1)(2, 2, 3, 1) Element-wise sum of the said
tuples: (6, 9, 8, 6)