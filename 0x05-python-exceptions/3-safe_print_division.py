#!/usr/bin/python3

""" a function that divides 2 integers and prints the result.

    args: any value

    returns: prints the result

    by Akpe Caleb

"""


def safe_print_division(a, b):

    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
