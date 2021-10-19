#!/usr/bin/python3

"""  3. Integers division with debug """


def safe_print_division(a, b):
    """ safe_print_division """

    print("Inside result: ", end="")

    try:
        div_result = a/b
    except (ValueError, ZeroDivisionError):
        div_result = "None"
    finally:
        print("{}".format(div_result))

    return div_result
