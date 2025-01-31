#Write a Python program to find the maximum of three numbers entered by the user.

def maximum(a,b,c):
    return max(a,b,c)

print(maximum(10,5,3))


a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value"))

if a>b and a>c:
    print(f" {a} is big")
elif b>a and b>c:
    print(f"{c} is big")
else:
    print(f" {c} is big")