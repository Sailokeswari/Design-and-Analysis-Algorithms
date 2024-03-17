# Implementation of queue Data structure

class Queue_Implementation:
    def __init__(self, size):
        # Initializing the queue with a fixed size, front, rear, and count
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        # Checking if the queue is empty
        return self.count == 0

    def is_full(self):
        # Checking if the queue is full
        return self.count == self.size

    def enqueue_item(self, item):
        # Enqueue an item into the queue
        if self.is_full():
            print("Queue is full if queue is full")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        self.count += 1

    def dequeue_item(self):
        # Dequeue an item from the queue
        if self.is_empty():
            print("Queue is empty if no elements in queue")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek_item(self):
        # Peek at the front item of the queue
        if self.is_empty():
            return None
        return self.queue[self.front]

# Example usage:
# Performing Operations on Queue
queue = Queue_Implementation(5)
# Adding items to the Queue
queue.enqueue_item(7)
queue.enqueue_item(3)
queue.enqueue_item(9)
queue.enqueue_item(1)
print("Front of the queue:", queue.peek_item())
print("Dequeued item from the queue:", queue.dequeue_item())
print("Dequeued item from the queue:", queue.dequeue_item())
print("Front of the queue:", queue.peek_item())

# Output:
# Front of the queue: 7
# Dequeued item from the queue: 7
# Dequeued item from the queue: 3
# Front of the queue: 9
