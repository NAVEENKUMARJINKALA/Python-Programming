str1="Naveen"
output=""
for i in range(len(str1)-1,-1,-1):
    #print(str1[i])
    output+=str1[i]
print(output)
if str1==output:
    print("strrev")
else:
    print("not same")