#!/usr/bin/python3
"""In this module you will find a class
"Square" at the moment it does nothing"""


class Node:
    """In this class, this is a Node"""

    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        """This is the constructor of the class"""
        self.data = data
        self.next_node = next_node
        return

    @property
    def data(self):
        """This property get data"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """This property set data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This property get next_node"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """This property set next_node"""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """In this class, this is a SinglyLinkedList"""

    __head = None

    def __init__(self):
        """This is the constructor of the class"""
        return

    def sorted_insert(self, value):
        """This function add a new_node"""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            current_node = self.__head
            if current_node.data > new_node.data:
                new_node.next_node = current_node
                self.__head = new_node
                return

            while current_node is not None:
                if current_node.next_node is None:
                    break
                if current_node.next_node.data > new_node.data:
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    return
                current_node = current_node.next_node
            current_node.next_node = new_node
        return

    def __str__(self):
        """This function return print list"""
        current_node = self.__head
        if (current_node is None):
            return ("")
        while current_node is not None and current_node.next_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return str(current_node.data)
