#from test import value

students = {
    "Alice": {"height": 165, "weight": 55,"marks":809},
    "Bob": {"height": 150, "weight": 48,"marks":988},
    "Charlie": {"height": 170, "weight": 65,"marks":250},
    "David": {"height": 155, "weight": 50,"marks":150},
}

fs={}
for name,details in students.items():
    if details["height"] > 0 and details["marks"] > 0:
        fs[name]=details

print(fs)
