#!/usr/bin/python3

"""  4. Divide a list  """


def list_division(my_list_1=[10, 0, 4], my_list_2=[2, 4, 0], list_length=3):
    """ list_division """

    div_result = []
    for i in range(list_length):
        try:
            div_result.append(my_list_1[i] / my_list_2[i])
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

print(list_division())