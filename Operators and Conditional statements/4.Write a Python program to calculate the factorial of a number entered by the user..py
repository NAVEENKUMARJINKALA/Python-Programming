# num=int(input("Enter a number: "))
# # def fact(n):
# #     return n*n-1
# # print(fact(num))
# for i in range(num):
#     fact=i
#     factorial=(fact*fact-1)
# print(factorial)

# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)
#
# # Input from user
# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial_recursive(num)}")
n=int(input("enter a num"))
def factn(n):
    if n==1 or n==0:
        return 1
    return n*factn(n-1)
#print(factn(5))

print(f"factorial of {n} is {factn(n)}")