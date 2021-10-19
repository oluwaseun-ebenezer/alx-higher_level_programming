#!/usr/bin/python3

"""  3. Integers division with debug """


def safe_print_division(a,b):
    """ safe_print_division """

    try:
        print("Inside result: {}".format(a/b))
    except ValueError:
        print("Inside result: None")
    finally:
        print("{} / {} = {}".format(a,b, a/b))
