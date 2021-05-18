#!/usr/bin/python3
class Node:

    __data = 0
    __next_node = None

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        return

    @property
    def data(self):
        return(self.__data)

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    __head = None

    def __init__(self):
        return

    def sorted_insert(self, value):
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
        current_node = self.__head
        while current_node is not None and current_node.next_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return str(current_node.data)
