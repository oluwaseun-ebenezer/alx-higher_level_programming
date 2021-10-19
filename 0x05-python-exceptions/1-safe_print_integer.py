#!/usr/bin/python3

""" 1-safe_print_integer """


def safe_print_integer(value):
    """ safe_print_integer """

    try:
        print("{:d}".format(value))

    except TypeError:
        return False

    return True
