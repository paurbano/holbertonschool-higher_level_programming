#!/usr/bin/python3
class LockedClass:
    """ Class with no attributes """
    def __setattr__(self, name, value):
        """ Called when an attribute assignment is attempted."""
        if name == "first_name":
            self.__dict__[name] = value
        else:
            msg = "'LockedClass' object has no attribute '" + name + "'"
            raise AttributeError(msg)
