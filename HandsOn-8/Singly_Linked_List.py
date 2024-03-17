# Implementation of Singly Linked List

class Node:
    def __init__(self, data):
        # Initializing a node with data and next pointer
        self.data = data
        self.next = None

class SinglyLinkedList_Implementation:
    def __init__(self):
        # Initializing the singly linked list with head and tail pointers
        self.head = None
        self.tail = None

    def is_empty(self):
        # Checking if the linked list is empty
        return self.head is None

    def insert_front_node(self, data):
        # Insert a new node at the front of the list
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_front_node(self):
        # Delete the node at the front of the list
        if self.is_empty():
            print("List is empty if List has no elements")
            return None
        deleted_item = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return deleted_item

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
llist = SinglyLinkedList_Implementation()
llist.insert_front_node(6)
llist.insert_front_node(9)
llist.insert_front_node(7)
print("Linked list:")
llist.display()
print("Deleted item from list:", llist.delete_front_node())
print("Linked list after deletion:")
llist.display()

# Output:
# Linked list:
# 7 -> 9 -> 6 -> None
# Deleted item from list: 7
# Linked list after deletion: 9 -> 6 -> None