#Develop a function to calculate the area of a circle given its radius.
pi=3.14159
def area_circle(radius):
    if radius<0:
        return "radius cannot be negative"
    elif radius>0:
        return pi*radius**2
print(area_circle(-5))