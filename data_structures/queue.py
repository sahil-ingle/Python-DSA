class queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, item):
        self.queue = [item] + self.queue

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop()

    def show_queue(self):
        print(self.queue)


x = queue()

x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)

x.show_queue()

x.dequeue()

x.show_queue()
