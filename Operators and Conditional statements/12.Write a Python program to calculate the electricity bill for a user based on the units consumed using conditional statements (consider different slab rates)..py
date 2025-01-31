
units_consumed=float(input("Enter the number of Units consumed:"))

def cat_A(units):
    return units*3.0
def cat_B(units):
    return units*3.5
def cat_C(units):
    return units*4.5
def commercial(units):
    return units*10

if units_consumed <500:
    print(f"Belongs to Cat_A, and Bill is {cat_A(units_consumed)} ")
elif (units_consumed >500) and (units_consumed<800):
    print(f"Belongs to Cat_B, and Bill is {cat_B(units_consumed)}")
elif (units_consumed >800) and (units_consumed<1000):
    print(f"Belongs to Cat_C, and Bill is {cat_C(units_consumed)}")
else:
    print(f" Belongs to Commercial category {commercial(units_consumed)}")
