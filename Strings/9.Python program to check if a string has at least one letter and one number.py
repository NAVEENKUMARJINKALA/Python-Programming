#Python program to check if a string has at least one letter and one number
# str_1="aaaabbccccdd0011"
# pairs={}
# for i in str_1:
#     if i in pairs:
#         pairs[i]+=1
#     else:
#         pairs[i]=1
# output=""
# print(pairs)
# for key,value in pairs.items():
#     print(f"{value}{key}")
digit_count=0
char_count=0
str1=input("ENter a sentence:")
for i in str1:
    if i.isalpha():
        char_count+=1
    elif i.isdigit():
        digit_count+=1
#print(char_count)
#print(digit_count)
if char_count & digit_count >1:
    print("Sentence have char and digit more than one")
elif char_count==0:
    print("enter atleast one character")
elif digit_count==0:
    print("enter atleast one digit")
