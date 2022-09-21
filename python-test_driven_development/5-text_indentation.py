#!/usr/bin/python3
"""Python interpreter"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
        ".", "?" and ":"
     """

    if type(text) is not str:
        raise TypeError('text must be a string')

    new_text = ""
    new_text = text.replace(". ", ".\n")
    new_text = new_text.replace(".", ".\n")
    new_text = new_text.replace("? ", "?\n")
    new_text = new_text.replace("?", "?\n")
    new_text = new_text.replace(": ", ":\n")
    new_text = new_text.replace(":", ":\n")



    print(new_text, end='')
