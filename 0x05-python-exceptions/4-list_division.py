#!/usr/bin/python3

"""  4. Divide a list  """


def list_division(my_list_1, my_list_2, list_length):
    """ list_division """

    div_result = []
    for i in range(list_length):
        try:
            div_result.append(my_list_1[i] / my_list_2)
        except ValueError:
            div_result.append(0)
        except TypeError:
            div_result.append(0)
            print ("wrong type")
        except ZeroDivisionError:
            div_result.append(0)
            print("division by 0")
        except IndexError:
            div_result.append(0)
            print("out of range")
        finally:
            pass

    return div_result
