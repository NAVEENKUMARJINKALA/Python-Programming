# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))
input_num=int(input())
temp=1
if input_num==1 or input_num==0:
    print(1)
else:
    for i in range(1,input_num+1):
        temp*=i
print(temp)

