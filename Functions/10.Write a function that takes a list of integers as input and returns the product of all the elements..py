#Write a function that takes a list of integers as input and returns the product of all the elements.
nums=list(map(int,(input("Enter the numbers to get product:").split(","))))
def allproduct(nums):
    product=1
    for num in nums:
        product*=num
    return product
print(allproduct(nums))