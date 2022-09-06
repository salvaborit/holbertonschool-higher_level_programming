#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz", end=(" " if i < 101 else ""))
        elif i % 3 == 0:
            print(f"Fizz", end=(" " if i < 101 else ""))
        elif i % 5 == 0:
            print(f"Buzz", end=(" " if i < 101 else ""))
        else:
            print(f"{i}", end=(" " if i < 101 else ""))
