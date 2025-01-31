#Python program to print even length words in a string
nstr="hello what are you doing?"
newstr=nstr.split()
print(newstr)
for i in newstr:
    if len(i)%2==0:
        print(f" Even words string is {i}")
    else:
        print(f" odd words {i}")
