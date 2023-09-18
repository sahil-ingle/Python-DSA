class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return not self.head

    def append(self,data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def printa(self):
        if self.is_empty():
            return -1
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next


obj = link_list()

obj.append(1)
obj.append(2)
obj.append(1)
obj.append(2)
obj.append(1)
obj.append(2)

obj.printa()