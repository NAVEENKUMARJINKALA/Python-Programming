# 18. Write a Python program to check if a specified element appears in a tuple of tuples. Original list:
# ((0Red0 , 0 W hite0 , 0 Blue0 ),( 0Green0 , 0 P ink0 , 0 P urple0 ),( 0Orange0 , 0 Y ellow0 , 0 Lime0 ))
# Check if White presenet in said tuple of tuples! True Check if White presenet in said tuple of tuples!
# True Check if Olive presenet in said tuple of tuples! False
original_list=(('Red','White','Blue'),('Green','Pink','Purple'),('Orange','Yellow','Lime'))
def tupoftuple(tuples,element):
    for t in tuples:
        for item in t:
            if item==element:
                return True
    return False

elements_to_check = ["White", "Olive"]

print(tupoftuple(original_list,'Purple'))
for elem in elements_to_check:
    print(f" {elem} is present in the tuple of tuples! {tupoftuple(original_list, elem)}")