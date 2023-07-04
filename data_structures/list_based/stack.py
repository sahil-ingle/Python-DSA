class stack:
    def __init__(self):
        self.stack = []

    def add_item(self, item):
        self.stack.append(item)

    def is_empty(self):
        return not self.stack

    def remove_item(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def show_stack(self):
        print(self.stack)


x = stack()

x.add_item(1)
x.add_item(2)
x.add_item(3)

x.show_stack()

x.remove_item()

x.show_stack()
