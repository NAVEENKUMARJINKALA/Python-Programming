#Write a Python program to determine the grade of a student based on their percentage score (A for 90% or above, B for 80% to 89%, etc.).

score=float(input("Enter the score of a student:"))
if score>100 or score<0:
    print("Out of percentage please check")
elif score>90 and score<100:
    print("The student belongs to category A")
elif score>80 and score<90:
    print("The student belongs to category B")
else:
    print("The student belongs to Fail category")
