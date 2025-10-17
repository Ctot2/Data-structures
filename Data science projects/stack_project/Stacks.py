from idlelib.sidebar import temp_enable_text_widget
from operator import truediv


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

    def contains(self, thing_maybe_in_stack):
        items_copy = self.items

        for i in range(len(items_copy)):
            thing_in_stack_checker = items_copy.pop()

            if thing_maybe_in_stack == thing_in_stack_checker:
                return True

        return False