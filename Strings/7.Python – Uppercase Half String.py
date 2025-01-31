str1=input("enter a string:  ")
#print(str1)
#print(type(str1))
first_half=str1[:len(str1)//2].upper()
second_half=str1[len(str1)//2:].lower()
final_str=first_half+second_half

print(first_half)
print(second_half)
print(final_str)
if first_half==second_half:
    print("strings halfs are equal")
else:
    print("not same")

