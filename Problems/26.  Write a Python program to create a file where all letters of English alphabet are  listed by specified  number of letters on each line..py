# #26.
# Write a Python program to create a file where all letters of English alphabet are  listed by specified
# number of letters on each line.
def write_alphabet_file(filename, letters_per_line):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    with open(filename, "w") as file:
        for i in range(0, len(alphabet), letters_per_line):
            file.write(alphabet[i:i + letters_per_line] + "\n")
write_alphabet_file("alphabet.txt", 13)

print("File 'alphabet.txt' created successfully!")
