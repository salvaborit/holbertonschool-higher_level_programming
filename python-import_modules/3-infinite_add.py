#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    sum = 0
    for addend in sys.argv[1:]:
        sum += int(addend)
    print(sum)
