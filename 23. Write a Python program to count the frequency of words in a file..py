#   words = content.replace('\n', ' ').replace('\t', ' ').split()
from random import sample

wordcounts={}
def word_count(filename):
    try:

        with open("C:\\Users\\poola sai kiran\\python\\sample.txt","r") as file:
            content=file.read()
            words = content.replace('\n', ' ').replace('\t', ' ').split()
            print(words)
            for word in words:
                word=word.lower()
                if word in wordcounts:
                    wordcounts[word]+=1
                else:
                    wordcounts[word]=1


        return wordcounts
    except FileNotFoundError:
        print("file not found")
print(word_count(sample))
for word,count in wordcounts.items():
    print({word},"is",{count})