#Implement a function to convert a temperature from Celsius to Fahrenheit.

celsius=float(input("Enter the celsius value:"))
fahrren=float(input("Enter the fahren heat value:"))

def cel_fah(cel):
    if cel<0:
        print("Negative value given")
    return (celsius*9/5)+32
def fah_cell(fahrren):
    if fahrren<0:
        print("Negative value given")
    return (fahrren-32)*5/9
print(f" Fahren heat to celsius is {fah_cell(fahrren)}")
print(f"Celsius to fahren heat is {cel_fah(celsius)}")