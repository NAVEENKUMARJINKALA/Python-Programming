#32. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers
#using Lambda.
def numdiv(nums):
    return list(filter(lambda x:x%19==0 or x%13==0,nums))
nums=list(map(int,input("Enter the numbers:").split()))
print(numdiv(nums))