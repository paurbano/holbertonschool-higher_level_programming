#!/usr/bin/python3
"""
MyList that inherits from list
"""


class MyList(list):
    """
    MyList
    """
    def print_sorted(self):
        """
        prints the list, but sorted
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
