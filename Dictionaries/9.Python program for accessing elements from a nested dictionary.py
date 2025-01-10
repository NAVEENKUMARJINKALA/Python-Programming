students = {
    "John": {"age": 20, "grade": "A",
             "Courses":
                 {
        "CSE": "Computer Science",
        "DATA":"Data science",
        "EEE":"electrical"
                 }
        },
    "Alice": {"age": 22, "grade": "B",
              "Courses":
                 {
        "CSE": "Computer Science",
        "DATA":"Data science",
        "EEE":"electrical"
                 }
        },
    "Bob": {"age": 21, "grade": "C",
            "Courses":
                 {
        "CSE": "Computer Science",
        "DATA":"Data science",
        "EEE":"electrical"
                 }
        }
}
#print(students)
print(students["John"].values())
print(students["John"].keys())
print(students.keys())
print(students.values())


