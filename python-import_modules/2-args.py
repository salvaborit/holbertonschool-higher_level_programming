#!/usr/bin/python3


from platform import python_branch


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) > 2:
        print(f"{len(sys.argv) - 1} arguments:")
    x = 1
    for arg in sys.argv[1:]:
        print(f"{x}: {arg}")
        x += 1
