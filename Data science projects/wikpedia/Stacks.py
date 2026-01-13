class Stack:

    def __init__ (self):
        self.items = []

    def push(self, input_value):
        self.items.append(input_value)
        print(self.items)

    def pop(self):
        n = len(self.items)
        return(self.items.pop(n-1))

    def empty(self):
        if self.items == []:
            return True
        else:
            return False

    def top(self):
        temp_remove = self.pop()
        self.push(temp_remove)
        return temp_remove

    def size(self):
        return len(self.items)

    def contains(self, value):
        temp = Stack()
        result = False
        for i in range(self.size()):

            b = self.pop()
            temp.push(b)

            if value == b:
                result = True
                break
        for i in range(temp.size()):
            self.push(temp.pop())
        return result