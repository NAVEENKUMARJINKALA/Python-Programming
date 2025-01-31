#Find length of a string in python (4 ways)
str1="Naveenkumar"

print(len(str1))


lent=0
#22d way
for i in str1:
    lent+=1
print(lent)
#3rd way
print(str1.__len__())


