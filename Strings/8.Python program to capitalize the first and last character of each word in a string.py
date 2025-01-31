#Python program to capitalize the first and last character of each word in a string
str_1=list(map(str,input("enter a sentence:").split()))
#print(str_1)
capitalized_string=""
for i in str_1:
    each_word=i[0].upper()+i[1:-1].lower()+i[-1].upper()
    capitalized_string+=each_word+" "
print(capitalized_string)
