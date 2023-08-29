#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None

    length = len(my_list)
    if idx > length - 1:
        #checks if the given index is greater than the maximum valid index.
        return (None)

    print(my_list(idx))
