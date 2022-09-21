#!/usr/bin/python3
"""Python interpreter"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
        ".", "?" and ":"
     """

    if type(text) is not str:
        raise TypeError('text must be a string')

    # new_text = ""
    # new_text = text.replace(". ", ".\n")
    # new_text = new_text.replace(".", ".\n")
    # new_text = new_text.replace("? ", "?\n")
    # new_text = new_text.replace("?", "?\n")
    # new_text = new_text.replace(": ", ":\n")
    # new_text = new_text.replace(":", ":\n")

    start = 0
    end = len(text)
    for idx in range(len(text)):
        if text[idx] in ".:?":
            end = idx + 1
            print(text[start:end].lstrip(), end='\n\n')
            start = end
