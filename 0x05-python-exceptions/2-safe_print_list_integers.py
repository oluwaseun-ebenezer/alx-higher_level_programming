#!/usr/bin/python3

""" 1-safe_print_integer """


def safe_print_list_integers(my_list=[], _x=0):
    """ safe_print_list_integers """

    counter = 0
    for i in range(_x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except ValueError or TypeError:
            continue
        except IndexError:
            break

    print()

    return counter
