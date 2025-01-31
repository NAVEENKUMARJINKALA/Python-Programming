#Ways to remove i’th character from string in Python
str1="Hellodear"
output=""
for i in range(len(str1)):
    if i==2:
        pass
    else:
        output+=str1[i]
print(output)
outpu1=str1[:4]+str1[5:]
print(outpu1)
print(f"the removed index after ith {str1} is {output}")
print("The removed index after ith ",str1,"is",output)

for i in range(1,5):
    print(f" the {i} table is :")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
