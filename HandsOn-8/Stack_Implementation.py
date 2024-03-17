# Implementation of Stack Data strucure 

class Stack_Implementation:
    # Initializing the stack with a fixed array size and set top to -1
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
    # Checking if the stack is empty
         return self.top == -1

    def is_full(self):
    # Checking if the stack is full
        return self.top == self.size - 1

    def push_ele(self, item):
     # Push an item onto the stack

        if self.is_full():
            print("Stack Overflow if exceeds the array size")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop_ele(self):
    # Pop an item from the stack

        if self.is_empty():
            print("Stack Underflow if array is empty")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek_ele(self):
    # Peek at the top item of the stack

        if self.is_empty():
            return None
        return self.stack[self.top]

# Example:
# Performing stack operations on the array
stack = Stack_Implementation(5)
# pushing elements onto the stack
stack.push_ele(5)
stack.push_ele(9)
stack.push_ele(2)
stack.push_ele(6)
print("Top of the stack element:", stack.peek_ele())
print("Popped item from the stack:", stack.pop_ele())
print("Popped item from the stack:", stack.pop_ele())
print("Top of the stack element:", stack.peek_ele())

# Output:
# Top of the stack element: 6
# Popped item from the stack: 6
# Popped item from the stack: 2
# Top of the stack element: 9