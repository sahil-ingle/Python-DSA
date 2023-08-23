# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class linked_list:
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         return not self.head
#
#     def append(self, data):
#         new_node = node(data)
#         if self.is_empty():
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node
#
#     def print_list(self):
#         if self.is_empty():
#             print("list is empty")
#         else:
#             current_node = self.head
#             while current_node:
#                 print(current_node.data, end=" -> ")
#                 current_node = current_node.next
#             print("none")
#
#     def remove_item(self, item):
#         if self.is_empty():
#             print("list is empty")
#         if self.head.data == item:
#             self.head = self.head.next
#         else:
#             current_node = self.head
#             while current_node.next:
#                 if current_node.next.data == item:
#                     current_node.next = current_node.next.next
#                     return
#                 current_node = current_node.next
#             print("item not in list")
#             return
#     def insert(self, position, item):
#         new_node = node(item)
#         if self.is_empty():
#             print("list is empty")
#         else:
#             current_node = self.head
#             while current_node:
#                 if current_node.data == position:
#                     new_node.next = current_node.next
#                     current_node.next = new_node
#                     return
#                 current_node = current_node.next
#             return print("item not present in the list")
#
#     def is_present(self,item):
#         if self.is_empty():
#             print("list is empty")
#         else:
#             current_node = self.head
#             while current_node:
#                 if current_node.data == item:
#                     return print("item is present")
#                 current_node = current_node.next
#             return print("item is not present")
#
#
#
#
# x = linked_list()
#
# x.append(1)
# x.append(2)
# x.append(3)
#
#
# x.append(4)
# x.insert(1, 3.5)
#
# x.remove_item(3)
#
# x.print_list()
#
# x.is_present(2)


