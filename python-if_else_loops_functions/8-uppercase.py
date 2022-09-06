#!/usr/bin/python3
# prints a string in uppercase


def uppercase(str):
    strlen = len(str)
    for i in range(0, strlen):
        i_ascii = ord(str[i])
        if i_ascii > 96 and i_ascii < 123:
            print("{}".format(chr(i_ascii - 32)),
                  end=("\n" if i == strlen - 1 else ""))
        else:
            print("{}".format(str[i]), end=("\n" if i == strlen - 1 else ""))
