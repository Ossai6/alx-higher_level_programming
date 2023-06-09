#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that is inherited (directly or indirectly) from the specified class.

    Parameters:
    obj (object): An object to be checked.
    a_class (class): A class that is supposed to be inherited from (directly or indirectly).

    Returns:
    bool: True if the given obj is an instance of a class that is inherited (directly or indirectly) from the a_class, otherwise False.
    """


    return type(obj) != a_class and issubclass(type(obj), a_class)
