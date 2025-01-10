# Sample student records stored in a dictionary
students = {
    "John": {"age": 20, "grade": "A", "major": "Computer Science"},
    "Alice": {"age": 22, "grade": "B", "major": "Mathematics"},
    "Bob": {"age": 21, "grade": "C", "major": "Physics"},
}

# Search for a student
search_name = input("Enter the student's name to search: ")

# Check if the student exists in the dictionary
if search_name in students:
    # Display the student record
    print(f"Record of {search_name}:")
    print(f"Age: {students[search_name]['age']}")
    print(f"Grade: {students[search_name]['grade']}")
    print(f"Major: {students[search_name]['major']}")
else:
    print(f"Student {search_name} not found.")
