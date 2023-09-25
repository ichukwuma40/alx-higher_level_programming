#!/usr/bin/python3
#3-print_reversed_list_integer

def print_reversed_list_integer(my_list=[]):
    """3-print all the integers of a list in a reversed order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
