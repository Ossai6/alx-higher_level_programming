#!/usr/bin/python3
class MyList(list):
    """
        This is a class "MyList" that inherits from list
    """

    def print_sorted(self):
        """
            prints the list in a sorted order
        """
        print(sorted(self))
