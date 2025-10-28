class Queue:

    def __init__ (self):
        self.items = []

    def enqueue(self, input_value):
        self.items.append(input_value)

    def dequeue(self):
        return self.items.pop(0)


    def empty(self):
        return True if self.items else False

    def look(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def contains(self, input):
        x = False
        for i in range(self.size()):
            temp = self.dequeue()
            self.enqueue(temp)
            if temp == input:
                x = True
        return x

    def __str__(self):
        elements = []
        for i in range(self.size()):
            temp = self.dequeue()
            self.enqueue(temp)
            elements.append(str(temp))
        return ''.join(elements)



    def __add__(self, other):
        new_queue = Queue()
        new_queue.items = self.items + other.items
        return new_queue