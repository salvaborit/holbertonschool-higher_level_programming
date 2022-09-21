#!/usr/bin/python3
"""Python interpreter"""


def text_indentation(text):
    # delims = [".", "?", ":"]
    # for i in delims:
    #     text.replace(i, f"{i}\n")
    new_text = ""
    new_text += text.replace(".", ".\n\n")
    new_text += text.replace("?", "?\n\n")
    new_text += text.replace(":", ":\n\n")

    print(new_text)
