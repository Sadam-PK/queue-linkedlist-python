class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty.")
            return None
        dequeued = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return dequeued

    def display(self):
        if self.is_empty():
            print("Error: Queue is empty.")
            return None
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # outputs 1 2 3
print(queue.dequeue())  # outputs 1
print(queue.dequeue())  # outputs 2
queue.display()  # outputs 3
print(queue.dequeue())  # outputs 3
print(queue.dequeue())  # outputs Error: Queue is empty.
queue.display()  # outputs Error: Queue is empty.
