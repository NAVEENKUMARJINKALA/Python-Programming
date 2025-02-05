#40. Write a program to print the simple diamond star pattern in the python.
n=int(input("enter the input"))
for i in range(1,n+1):
    print(" "* (n-i)+ "@"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "* (n-i)+ "j"*(2*i-1))

for i in range(1,n+1):
    print(" "*(n-1) + "#"*(2*i-1))