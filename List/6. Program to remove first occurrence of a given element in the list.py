my_list = [10, 20, 30, 40, 50, 20, 60, 70]
element_to_remove = 20
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"List after removing the first occurrence of {element_to_remove}:", my_list)
else:
    print(f"{element_to_remove} is not in the list.")