class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binary_tree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root

    def append(self,data):
        new_node = node(data)
        if self.is_empty():
            self.root = new_node
        else:
            self.recursive_append(self.root,new_node)

    def recursive_append(self,current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.recursive_append(current_node.left,new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.recursive_append(current_node.right,new_node)

    def show(self):
        if self.is_empty():
            return None
        else:
            current_node = self.root
            self.recursive_show(current_node)

    def recursive_show(self, current_node):
        if current_node:
            self.recursive_show(current_node.left)
            print(current_node.data, end="")
            self.recursive_show(current_node.right)


tree = binary_tree()

tree.append(5)
tree.append(3)
tree.append(7)

tree.show()