Students={
    "Naveen":{"sno":1,"Nickname":"Naveen","age":25,"Location":"Hyderabad"},
    "Sai":{"sno":2,"Nickname":"tammudu","age":24,"Location":"Secunderabad"},
    "Saikiran": {"sno": 3, "Nickname": "Bro", "age": 23, "Location": "Secunderabad"}

}
#print(Students.keys())
#print(Students.values())
sname=input("Enter a name to search")
for key,value in Students.items():
    if key==sname:
        print("Students",Students[sname]["sno"])
        print("Students",Students[sname]["Location"])
        print("Students",Students[sname]["age"])
else:
    print("No data found")