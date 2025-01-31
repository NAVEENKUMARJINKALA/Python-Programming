a=input("Enter a number:")
b=input("Enter a number:")
a,b=b,a
print(a)
print(b)

temporary_var=a
a=b
b=temporary_var
print(a)
print(b)