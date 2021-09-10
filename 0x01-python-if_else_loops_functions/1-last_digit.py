#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'Last digit of {number} is {str(number)[-1]} {"and is less than 6" if (int(str(number)[-1]) < 6) else "and is greater than 5"} {"and is 0" if (int(str(number)[-1]) == 0) else "and not 0" }')