#39. Write a program to spilt and join the strings. string_1=input("Enter a string")
string_1=input("Enter a string")
def split_and_join(string,delimiter=" "):
    words=string.split(delimiter)
    splitted_words=words
    joined=delimiter.join(words)
    return splitted_words,joined


print(split_and_join(string_1))