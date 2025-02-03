#Develop a function that takes a list of words as input and returns the longest word.
words=list(map(str,input("Enter words separated by commas").split()))
# print(words)
def longest_word(words):
    if not words:
        return None

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print("Longest word:", longest_word(words))
