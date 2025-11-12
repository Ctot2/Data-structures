from types import new_class


class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

    def get_value(self):
        return self.value

    def set_next(self, n):
        self.next = n
    def get_next(self):
        return self.next

class LinkedList:


    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        s = "["
        n = self.head
        while n != None:
            if type(n.get_value()) == str:
                s += '"' + n.get_value() + '", '
            else:
                s += str(n.get_value()) + ", "
            n = n.get_next()
        if s != "[":
            s = s[:-2]
        s = s + "]"
        return s

    def insert_at_start(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
            new_node.set_next(None)

    def insert_at_end(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node


    def empty(self):
        if self.tail is None:
            return True
        else:
            return False

