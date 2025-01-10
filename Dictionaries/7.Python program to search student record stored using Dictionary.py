#Student={"Name":"Naveen","Age":25,"City":"Hyderabad","Office Name":"Thundersoft"}
#print(Student)

Students={
    "Naveen":{"sno":1,"Nickname":"Naveen","age":25,"Location":"Hyderabad"},
    "Sai":{"sno":2,"Nickname":"tammudu","age":24,"Location":"Secunderabad"},
    "Saikiran": {"sno": 3, "Nickname": "Bro", "age": 23, "Location": "Secunderabad"}

}
#print(Students)
print("Student details are",Students["Naveen"])
sname=input("Enter students name")
# for i in Students:
#     print(i)
for key,value in Students.items():
    if key==sname:
        print(f"{key} Student Sno is ",Students[sname]["sno"])
        print("Student name is ",Students[sname]["Nickname"])
        print("Student age is ",Students[sname]["age"])
        print("Student Location is ",Students[sname]["Location"])

else:
    print("student name",sname ,"is not found")