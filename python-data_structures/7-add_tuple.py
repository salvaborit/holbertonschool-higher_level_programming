#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + ((0,) * (2 - len(tuple_a)))
    tuple_b = tuple_b + ((0,) * (2 - len(tuple_b)))
    zipped = zip(tuple_a[:2], tuple_b[:2])
    mapped = map(sum, zipped)
    return tuple(mapped)
