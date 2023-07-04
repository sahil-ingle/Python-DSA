class array:
    def __init__(self):
        self.arr = []

    def add_item(self, item):
        self.arr.append(item)

    def show_list(self):
        print(self.arr)

    def is_empty(self):
        return not self.arr

    def remove_item(self, item):
        if self.is_empty():
            return None
        return self.arr.remove(item)

    def remove_index(self, index):
        if self.is_empty():
            return None
        return self.arr.pop(index)

    def insert_item(self, index, item):
        self.arr.insert(index, item)


x = array()

x.add_item(1)
x.add_item(2)
x.add_item(3)

x.show_list()

x.insert_item(2, 5)
x.show_list()
