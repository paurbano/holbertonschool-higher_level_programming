#!/usr/bin/python3
def pascal_triangle(n):
    pascal_list = []
    if n <= 0:
        return pascal_list

    for line in range(1, n + 1):
        num = 1
        p_list = []
        for i in range(1, line + 1):
            p_list.append(str(num))
            num = int(num * (line - i) / i)
        pascal_list.append(p_list)
    return pascal_list
