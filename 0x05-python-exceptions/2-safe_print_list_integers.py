#!/usr/bin/python3

""" a function that prjnts a value

    args: any value

    returns: prints the value

    by Akpe Caleb

"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            count += 1
        except(ValueError, TypeError):
            continue
    print()
    return count
