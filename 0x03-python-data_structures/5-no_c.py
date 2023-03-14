#!/usr/bin/python3

""" a function that removes all characters c and C from a string.   By Caleb
    
    arg: the string

    return: a modified string without 'c' or 'C'
"""

def no_c(my_string):
    string = ""

    for char in my_string:
        if char not in ['C', 'c']:
            string += char
    return string
