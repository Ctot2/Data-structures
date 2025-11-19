
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
        self.length += 1
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
            new_node.set_next(None)

    def insert_at_end(self, val):
        new_node = Node(val)
        self.length += 1
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def delete_at_start(self):
        self.length -= 1
        if self.head.get_next:
            self.head = self.head.get_next()
        else:
            self.head = None
            self.tail = None


    def empty(self):
        return self.tail is None

    def set_next(self, n):
        self.next = n

    def get_next(self):
        return self.next

    def set_value(self):
        return self.value

    def __len__(self):
        return self.length

    def __getitem__(self, ind):
        if ind < 0 or ind >= self.length:
            raise IndexError("Index out of range")
        temp  = self.head

        for i in range(ind):
            temp = temp.get_next()

        return temp.get_value()

    def get_node(self, ind):
        temp = self.head

        for i in range(ind):
            temp = temp.get_next()

        return temp

    def insert(self, ind, val):
        if ind == 0:
            self.insert_at_start(val)
        elif ind == len(self):
            self.insert_at_end(val)
        else:
            new_node = Node(val)
            self.length += 1
            new_node.set_next(self.get_node(ind))
            self.get_node(ind-1).set_next(new_node)

    def delete_at_end(self):
        if self.empty():
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.get_node(len(self) - 2)
            temp.set_next(None)
            self.tail = temp
            self.length -= 1

    def delete(self, ind):
        if ind == 0:
            self.delete_at_start()
        elif ind == len(self) - 1:
            self.delete_at_end()
        elif ind >= len(self) or ind < 0:
            raise IndexError
        else:
            temp = self.get_node(ind-1)
            temp2 = self.get_node(ind +1)
            temp3 = self.get_node(ind)
            temp3.set_next(None)
            temp.set_next(temp2)
            self.length -= 1

    def __contains__(self, item):
        temp = self.head
        if temp.get_value() == item:
            return True
        else:
            for i in range(len(self)-1):
                temp = temp.get_next()
                if temp.get_value() == item:
                    return True
        return False