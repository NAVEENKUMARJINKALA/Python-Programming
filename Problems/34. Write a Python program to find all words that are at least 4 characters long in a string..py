#34. Write a Python program to find all words that are at least 4 characters long in a string.
string_1="naveen","kumar","jinkala","hello","hai","how"
#print(string_1)
slength=4
lengthfour=list(filter(lambda s:len(s)>=4,string_1))
print(lengthfour)




for s in string_1:
     if len(s)>=slength:
         print(s)