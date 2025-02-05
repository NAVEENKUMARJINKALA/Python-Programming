#37. Write a program to find all matches of input strings from a list.
string_1=list(map(str,input("Enter a strings").split()))
inputstring="india"
matchcount=0
for word in string_1:
    if word==inputstring:
        matchcount+=1
print(matchcount)

