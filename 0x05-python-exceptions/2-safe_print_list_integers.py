#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cont = 0
        while cont < x:
            print("{:d}".format(my_list[cont]), end="")
            cont = cont + 1
    except (TypeError, ValueError):
        pass
    print("")
    return cont
