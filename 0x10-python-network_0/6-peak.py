#!/usr/bin/python3
""" find peak in a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    return peak(list_of_integers, 0, len(list_of_integers)-1)


def peak(array, low, high):
    mid = int((low + high) / 2)
    if (array[mid - 1] <= array[mid]) and (array[mid + 1] <= array[mid]):
        return array[mid]
    elif array[mid] < array[mid + 1]:
        return peak(array, mid + 1, high)
    else:
        return peak(array, low, mid - 1)
