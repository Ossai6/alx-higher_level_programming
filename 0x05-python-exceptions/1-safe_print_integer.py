#!/usr/bin/python3

""" a function that prjnts a value

    args: any value

    returns: prints the value

    by Akpe Caleb

"""


def safe_print_integer(value):
    try:
        value = int(value)
        print("{:d}".format(value))
    except(ValueError, TypeError):
        return False
    else:
        return True
