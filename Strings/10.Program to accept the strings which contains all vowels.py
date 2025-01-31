# string_1=input("Enter a string:")
# vowels={'a','e','i','o','u'}
# for i in string_1:
#     if i in vowels:
#         print(f"{i} in vowels")
#     else:
#         print(f"{i} is not there in vowels")
#


string_1=input("Enter a string:")
vowels={'a','e','i','o','u'}
char_count={}
for i in string_1:
    if i in char_count:
        char_count[i]+=1
    else:

       char_count[i]=1
for key,value in char_count.items():
    for key in vowels:
        if value>=1:
            print(True)



#print(char_count)
