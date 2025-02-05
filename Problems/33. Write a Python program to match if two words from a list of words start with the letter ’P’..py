#33. Write a Python program to match if two words from a list of words start with the letter ’P’.
words = input("Enter a list of words separated by spaces: ").split()

p_words = list(filter(lambda x: x.lower().startswith('p'), words))
if len(p_words) >= 2:
    print(f"Matching words: {p_words[:2]}")
else:
    print("Less than two words start with 'P'")