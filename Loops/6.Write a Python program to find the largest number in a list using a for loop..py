#Write a Python program to find the largest number in a list using a for loop.
list_1=[96,10,20,30,40,50,95]
init=list_1[0]
for i in list_1:
    if i>init:
        init=i
print(init)