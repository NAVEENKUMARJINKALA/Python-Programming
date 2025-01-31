#Write a Python program to check if a character entered by the user is a vowel, consonant, or neither using conditional statements.

# character=input("Enter a character")
#
# vowels={'a','e','i','o','u'}
# if character in vowels:
#     print(f" {character} is a vowel")
# else:
#     print("not a vowel")
#
def check_char(char):
    vowels="aeiou"
    if char.isalpha():
        if char in vowels:
            print(f"{char} is in vowels")
        else:
            print(f"{char} is a consonent")
    else:
        print(f"{char} is neither vowel or consonent")
char=input("Enter a character")
#print(check_char(char))


if len(char)==1:
    print(f"char {char} is ",check_char(char),)
else:
    print("out of range")