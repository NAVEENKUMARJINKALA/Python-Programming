# #Write a Python program to print the Fibonacci series up to n terms using a while loop.
# n=int((input("ENter a number")))
# a,b=0,1
# i=0
# count=a+b
# while i<n:
#     i+=1
n = int(input("Enter the number of terms: ")) #5

a=0
b=1
count = 0

while count < n: #0<5
    print(a, end=" ")  # Print the current number
    a, b = b, a + b  # Update values
    count += 1
