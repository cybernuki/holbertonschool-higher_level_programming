#!/usr/bin/python3
class Node:
    """ A node classs """

    def __init__(self, data, next_node=None):
        """Initialize a Node.

        arg:
            data (int): is the information that the node will save
            next_node (Node or None): is a reference to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data Setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node Setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Single linked list class"""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Add a new node in a sorted way

        arg:
            value (Int): is the new value to add
        """
        new_node = Node(value)

        if not self.__head:
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp:
                if not tmp.next_node or new_node.data < tmp.next_node.data:
                    new_node.next_node = tmp.next_node
                    tmp.next_node = new_node
                    break
                tmp = tmp.next_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        tmp = self.__head
        result = []
        while tmp:
            result.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(result))
