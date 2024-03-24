# Implementation of Hash Table Using Doubly Linked List

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class UsingDoublyLinkedListImplementation:
    def __init__(self):
        self.head = None
        self.tail = None

# Inserting  a new node at the end of the doubly linked list
        
    def insert_node(self, key, val):
        new_node = Node(key, val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

# Searching for a node for the given key in the list
            
    def search_node(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

# Removing the node of the given key from the list
    
    def remove_node(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

   # HashTable Implementation
            
class HashTableImplementation:
    def __init__(self, initial_capacity):
        self.size = 0
        self.capacity = initial_capacity
        self.table = [None] * initial_capacity

    # Defining the Generic hash function

    def generic_hash_function(self, key):

        return (key * 2786612445) % self.capacity
    
    # Resizing the hash table and rehashing all the elements

    def resize_table(self, new_capacity):
        new_table = [None] * new_capacity
        for i in range(self.capacity):
            if self.table[i]:
                current = self.table[i].head
                while current:
                    index = self.hash_function(current.key)
                    if not new_table[index]:
                        new_table[index] = UsingDoublyLinkedListImplementation()
                    new_table[index].insert(current.key, current.val)
                    current = current.next
        self.table = new_table
        self.capacity = new_capacity


    # Inserting a key-value pair into the hash table


    def insert_key(self, key, val):
        if self.size >= self.capacity:
            self.resize(2 * self.capacity)
        index = self.generic_hash_function(key)
        if not self.table[index]:
            self.table[index] = UsingDoublyLinkedListImplementation()
        self.table[index].insert_node(key, val)
        self.size += 1

# Searching for a key in the hash table and returns its value
        
    def search_key(self, key):
        index = self.generic_hash_function(key)
        if self.table[index]:
            result = self.table[index].search_node(key)
            if result:
                return result.val
        return None

# Removes a key-value pair from the hash table
    
    def remove_key(self, key):
        index = self.generic_hash_function(key)
        if self.table[index]:
            self.table[index].remove_node(key)
            self.size -= 1
            if self.size <= self.capacity // 4:
                self.resize(self.capacity // 2)

# Example
htg = HashTableImplementation(9)
htg.insert_key(6, 70)
htg.insert_key(34, 59)
htg.insert_key(2, 45)
htg.insert_key(1, 25)
htg.insert_key(25, 200)
htg.insert_key(89, 33)
htg.insert_key(120, 240)
htg.insert_key(11, 150)
htg.insert_key(10, 500)

print("value for the key 34:", htg.search_key(34))
print("value for the key 89:", htg.search_key(89))
print("value for the key 11:", htg.search_key(11))

htg.remove_key(1)
htg.remove_key(2)

print("value for the key 1 after removal of the key:", htg.search_key(1))
print("value for the key 2 after removal of the key:", htg.search_key(2))



# Output:
# value for the key 34: 59
# value for the key 89: 33
# value for the key 11: 150
# value for the key 1 after removal of the key: None
# value for the key 2 after removal of the key: None