#!/usr/bin/python3

""" 0-safe_print_list """

def safe_print_list(my_list=[], _x=0):
    """ safe_print_list """

    counter = 0
    for i in range(_x):
        try:
            print (my_list[i], end="")
            counter += 1
        except IndexError:
            break

    print()

    return counter
