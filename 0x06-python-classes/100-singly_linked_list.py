#!/usr/bin/python3
"""This method implements a class Node that defines a node of a singly
linked list."""


class Node:
    """This class Node does nothing."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None:
            self.__next_node = None
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        tail = self.__head
        while tail:
            string += str(tail.data)
            if tail.next_node:
                string += "\n"
            tail = tail.next_node
        return string

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        else:
            tail = self.__head
            if value < tail.data:
                self.__head = Node(value, tail)
                return
            while tail and tail.next_node:
                tail = tail.next_node
            tail.next_node = Node(value)
