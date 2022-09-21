#!/usr/bin/python3
"""Python interpreter"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
        ".", "?" and ":"
     """

    if type(text) is not str:
        raise TypeError('text must be a string')

    delim_found = False
    start = 0
    for idx in range(len(text)):
        if text[idx] in ".:?":
            delim_found = True
            end = idx + 1
            print(text[start:end].lstrip(), end='\n\n')
            start = end
        if delim_found is True and idx == len(text) - 1:
            print(text[start:].lstrip(), end='')

    if delim_found is False:
        print(text.lstrip(), end='')
