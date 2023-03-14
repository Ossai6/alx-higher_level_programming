#!/usr/bin/python3

""" a function that adds two tuples

    args: two tuples tuple_a and tuple_b

    returns: a modified or added tuples

    by Akpe Caleb

"""


def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    # Checking the length of tuple_a
    if len_tuple_a < 1:
        tuple_a = (0, 0)
    elif len_tuple_a < 2:
        tuple_a = (tuple_a[0], 0)

    # Checking the length of tuple_b
    if len_tuple_b < 1:
        tuple_b = (0, 0)
    elif len_tuple_b < 2:
        tuple_b = (tuple_b[0], 0)

    # Adding the index of the the two tuples
    modified_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return modified_tuple
