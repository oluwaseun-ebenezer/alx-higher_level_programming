#!/usr/bin/python3
def islower(c):
    if ord(c) == 99:
        return True
    else:
        False

islower = __import__('7-islower').islower

print("c is {}".format("lower" if islower("c") else "upper"))
