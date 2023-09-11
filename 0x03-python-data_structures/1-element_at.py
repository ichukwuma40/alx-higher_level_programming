#!/usr/bin/python3
# welcome to 1-element

def element_at(my_list, idx):
    """This retrive the element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
