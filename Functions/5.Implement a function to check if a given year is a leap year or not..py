#Implement a function to check if a given year is a leap year or not.
year=int(input("Enter a year to check :"))
def leapyear(year):
    # if (year%4==0 and year%100!=0) or (year%400==0):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f" {year} is a leap year")
        else:
            print(f"{year} is a not leap year")

print(leapyear(year))