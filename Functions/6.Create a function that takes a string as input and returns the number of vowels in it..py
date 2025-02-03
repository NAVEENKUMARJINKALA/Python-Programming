#Create a function that takes a string as input and returns the number of vowels in it.
str1=input("Enter a string to get vowels:")
vowels={'a','e','i','o','u'}
vcount=0
for char in str1:
    if char.isalpha():
        if char in vowels:
            vcount+=1
    else:
        print("Not contains vowels")
print(vcount)

