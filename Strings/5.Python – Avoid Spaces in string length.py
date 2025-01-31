str1=" #@$%  ^%$^^ Naveenkumar ** "
# print(str1.split())
# print(str1.strip())
#
# output=''
# for i in str1:
#     if i==" ":
#         pass
#     else:
#         output+=i
# print(output)


rd=""
new=""
for i in str1:
    if i.isalpha():
        new+=i
    else:
        rd+=i
print(new)
print(rd)


