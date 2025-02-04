def extractfiles(file1, file2):
    char_list = []

    try:
        with open(file1, 'r', encoding='utf-8') as f1:
            #print(f1.read())
            char_list.extend(f1.read())
        with open(file2, 'r', encoding='utf-8') as f2:
            char_list.extend(f2.read())
            #print(f2.read())

    except FileNotFoundError:
        print("Error: One or both files not found.")

    return char_list  # Returns a list of characters

file1_path = "C:\\Users\\poola sai kiran\\python\\first.txt"
file2_path = "C:\\Users\\poola sai kiran\\python\\second.txt"

print(extractfiles(file1_path, file2_path))
