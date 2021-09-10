#!/usr/bin/python3
islower = __import__('7-islower').islower

print("c is {}".format("lower" if islower("c") else "upper"))
