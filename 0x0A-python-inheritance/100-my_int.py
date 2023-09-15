#!/usr/bin/python3
""" This module contains MyInt class """


class MyInt(int):
    """ This represents MyInt class """

    def __eq__(self, other):
        """ Redefines the equality of MyInt """
        return False

    def __ne__(self, value):
        """ Redefines the inequality of MyInt """
        return False
