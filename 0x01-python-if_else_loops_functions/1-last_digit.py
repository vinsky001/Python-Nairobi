#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    print("The last digit {:d} is {:d} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("The last digit {:d} is {:d} and is 0".format(number, last_digit))
else:
    print("The last digit {:d} is {:d} and is less than 6 and not 0".format(number, last_digit))
