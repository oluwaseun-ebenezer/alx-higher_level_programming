#!/usr/bin/python3

"""  3. Integers division with debug """


def safe_print_division(a,b):
    """ safe_print_division """

    try:
        div_result = a/b
        print("Inside result: {}".format(div_result))
    except (ValueError, ZeroDivisionError):
        div_result = "None"
        print("Inside result: None")
    finally:
        return div_result
