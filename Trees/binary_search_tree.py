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
                self.recursive_append(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.recursive_append(current_node.right, new_node)

    def in_order_print(self):
        if self.is_empty():
            return "its empty"
        self.in_recursive_print(self.root)

    def in_recursive_print(self,current_node):
        if current_node:
            self.in_recursive_print(current_node.left)
            print(current_node.data, " - ", end="")
            self.in_recursive_print(current_node.right)

    def pre_order_print(self):
        if self.is_empty():
            return "its empty"
        self.pre_recursive_print(self.root)

    def pre_recursive_print(self,current_node):
        if current_node:
            print(current_node.data, "/" , end="")
            self.pre_recursive_print(current_node.left)
            self.pre_recursive_print(current_node.right)

    def post_order_print(self):
        if self.is_empty():
            return "its empty"
        self.post_recursive_print(self.root)

    def post_recursive_print(self,current_node):
        if current_node:
            self.post_recursive_print(current_node.left)
            self.post_recursive_print(current_node.right)
            print(current_node.data)



obj = binary_tree()

obj.append(5)
obj.append(2)
obj.append(10)
obj.append(7)
obj.append(15)
obj.append(12)
obj.append(20)
obj.append(30)
obj.append(6)
obj.append(8)

obj.in_order_print()
obj.pre_order_print()
obj.post_order_print()