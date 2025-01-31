#Write a Python program to determine the type of triangle based on the lengths of its sides (equilateral, isosceles, or scalene).

first_side=float(input("Enter the first side length"))
second_side=float(input("Enter the second side length"))
third_side=float(input("Enter the third side length"))
print(f" The Triangle sides are {first_side},{second_side},{third_side}")
if first_side==second_side==third_side:
    print("sides are same")
elif first_side==second_side or second_side==third_side or first_side==third_side:
    print("isosceles")
else:
    print("Scalene ")