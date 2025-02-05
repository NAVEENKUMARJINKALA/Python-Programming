#29. Write a Python program to square and cube every number in a given list of integers using
#Lambda.
list_1=list(map(int,input("Enter a list of integers to get square :").split()))
def getsquare(list):
    squares=[]
    cubes=[]
    for i in list:
       square=i**2
       cube=i**3
       squares.append(square)
       cubes.append(cube)

    return squares,cubes
print(getsquare(list_1))

# using lamnda
def getcubes(lst):
    return list(map(lambda x: x**2,lst)),list(map(lambda x:x**3,lst))
print(getcubes(list_1))
