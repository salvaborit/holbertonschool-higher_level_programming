#!/usr/bin/python3
"""Python interpreter"""


class Node:
    """class: Node (of a singly linked list)"""

    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError('data must be an integer')
        if type(next_node) is not Node and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self, value):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """class: Single linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            node = self.__head
            while node.__data < value:
                node = node.__next_node
            new_node.__next_node = node.__next_node
            node.__next_node = new_node

    def __str__(self):
        string = ""
        node = self.__head
        while node:
            string += node.__data
