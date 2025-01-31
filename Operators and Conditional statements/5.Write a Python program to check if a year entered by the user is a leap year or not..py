year = int(input("Enter a year to check if it's a leap year or not: "))

def leapyear(year):
    if (year %4==0 and year%100!=0) or (year%400==0):
        print(f" The year {year} is leap year ")
    else:
        print("not a leap year")
print(leapyear(year))
