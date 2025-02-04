#24. Write a Python program to combine each line from first file with the corresponding line in
# #second file.
file1=open("C:\\Users\\poola sai kiran\\python\\first.txt")
file2=open("C:\\Users\\poola sai kiran\\python\\second.txt")
# firstfilelines=file1.read()
# secondfilelines=file2.read()
# #print(firstfilelines)
# #print(secondfilelines)
# words={}
# def filecombine(file1,file2):
#     for line in firstfilelines:
#         for line2 in secondfilelines:
#             final=line+line2
#             return final
# print(filecombine(file1,file2))
#

def combine_files(file1, file2, output_file):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out:
            for line1, line2 in zip(f1, f2):  # Read both files line by line
                out.write(line1.strip() + " " + line2)  # Combine and write to output file
        print(f"Combined content written to {output_file}")

    except FileNotFoundError:
        print("Error: One of the files was not found.")

combine_files("C:\\Users\\poola sai kiran\\python\\first.txt", "C:\\Users\\poola sai kiran\\python\\second.txt", "C:\\Users\\poola sai kiran\\python\\output.txt")