#!/usr/bin/python3
read_lines = __import__('2-read_lines').read_lines

print("1 line:")
read_lines("my_file_0.txt", 0)
print("--")
print("3 lines:")
read_lines("my_file_0.txt", 3)
print("--")
print("Full content:")
read_lines("my_file_0.txt")
print("--")
print("mayor o menor num lineas:")
read_lines("my_file_0.txt", 4)
