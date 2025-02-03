nums = list(map(int, input("Enter a list of numbers to get sum: ").split(",")))
#print(nums)
print(f" total sum of {nums} is ",sum(nums))
def totalsum(nums):
    total = 0
    for i in nums:
        total+=i
    return total
print(totalsum(nums))
