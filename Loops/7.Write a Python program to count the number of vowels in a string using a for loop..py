#Write a Python program to count the number of vowels in a string using a for loop.
string_1="Welcome to Thundersoft"
vowels={'a','e','i','o','u'}
vcount=0
for i in string_1:
    if  i in vowels:
        vcount+=1
print(vcount)
