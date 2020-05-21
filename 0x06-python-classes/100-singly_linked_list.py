#!/usr/bin/python3
"""This module implements a class Node that defines a node of a singly
linked list."""


class Node:
    """This class Node assigns data and next_node."""

    def __init__(self, data, next_node=None):
        """This function initializes an instance of the Node class and assigns
the public attribute size to the instance if size is the correct int type. It
then assigns the public attribute position once it's validated."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This getter function gets the data attribute of the instance
and returns it"""
        return self.__data

    @data.setter
    def data(self, value):
        """This setter function validates the data argument given at instantiation.
If valid, it sets the private data attribute for the instance."""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """This getter function gets the next_node attribute of the instance
and returns it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This setter function sets the next_node attribute to None, the value
passed to the function, or raises a TypeError if those fail"""
        if value is None:
            self.__next_node = None
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """This class SinglyLinkedList assigns head to None and adds
Node instances through sorted_insert()."""

    def __init__(self):
        """This function initializes an instance of the SinglyLinkedList class and
assigns the private attribute head to None."""
        self.__head = None

    def __str__(self):
        """This function prints the string representation of the SLL"""
        string = ""
        tail = self.__head
        while tail:
            string += str(tail.data)
            if tail.next_node:
                string += "\n"
            tail = tail.next_node
        return string

    def sorted_insert(self, value):
        """This function determines the correct positioning of the new Node
instance and creates it at that position"""
        if self.__head is None:
            self.__head = Node(value)
            return
        else:
            tail = self.__head
            if value < tail.data:
                self.__head = Node(value, tail)
                return
            while tail and tail.next_node:
                temp = tail
                tail = tail.next_node
                if value < tail.data:
                    temp.next_node = Node(value, tail)
                    return
            tail.next_node = Node(value)
