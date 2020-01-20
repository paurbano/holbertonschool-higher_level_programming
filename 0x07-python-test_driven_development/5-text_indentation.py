#!/usr/bin/python3
""" Module Text indentation  """


def text_indentation(text):
    """  prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in ".?:":
        text = text.replace(i, i + "\n\n")

    print("\n".join(t.strip() for t in text.split('\n')), end="")
