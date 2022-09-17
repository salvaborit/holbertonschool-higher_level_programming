#!/usr/bin/python3


from unittest.mock import NonCallableMagicMock


def best_score(a_dictionary):
    if a_dictionary is not None:
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None
