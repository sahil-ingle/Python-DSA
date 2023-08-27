class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class D_linked_list:
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
            new_node.prev = current_node

    def print(self):
        if self.is_empty():
            return None
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end="")
                print(" -> ",end="")
                current_node = current_node.next
            print("None")

    def insert(self,position,data):
        new_node = node(data)
        if self.is_empty():
            return None
        else:
            current_node = self.head
            while current_node:
                if current_node.data == position:
                    current_node.prev.next = new_node
                    new_node.next = current_node
                    new_node.prev = current_node.prev
                    current_node.prev = new_node
                    break
                current_node = current_node.next

    def delete(self,data):
        if self.is_empty():
            return None
        else:
            current_node = self.head
            while current_node:
                if current_node.data == data:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    break
                current_node = current_node.next




node1 = D_linked_list()

node1.append(2)
node1.append(3)
node1.append(7)
node1.insert(3,6)
node1.append(9)
node1.delete(7)
node1.print()
