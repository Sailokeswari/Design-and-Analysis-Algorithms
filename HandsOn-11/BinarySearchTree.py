# Implementation of Binary Search Tree

class BinarySearchTreeNode:
    def __init__(self, key):
        self.key = key
        self.left_node = None
        self.right_node = None

class BinarySearchTreeImplementation:
    def __init__(self):
        self.root = None

# Inserting a key into the binary search tree
        
    def insert_key(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return BinarySearchTreeNode(key)
        if key < root.key:
            root.left_node = self._insert(root.left_node, key)
        elif key > root.key:
            root.right_node = self._insert(root.right_node, key)
        return root

 # Searching/Querying for the key in the binary search tree
    
    def query_key(self, key):
        return self._query(self.root, key)

    def _query(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._query(root.left, key)
        return self._query(root.right, key)
    
    # To Delete a key from the binary search tree

    def delete_key(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left_node, key)
        elif key > root.key:
            root.right = self._delete(root.right_node, key)
        else:
            if root.left_node is None:
                return root.right_node
            elif root.right is None:
                return root.left
            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self._delete(root.right, min_node.key)
        return root

 # To Find the minimum key in a subtree
    
    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
# To Perform an in-order traversal of the binary search tree
    
    def inorder_traversal_result(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left_node, result)
            result.append(root.key)
            self._inorder_traversal(root.right_node, result)


binsearchtree = BinarySearchTreeImplementation()
keys = [4, 7, 1, 2, 18, 21, 45, 99, 32]
for key in keys:
    binsearchtree.insert_key(key)

print("The Inorder traversal result is :", binsearchtree.inorder_traversal_result())

binsearchtree.delete_key(5)
print("Inorder traversal after deleting key 21:", binsearchtree.inorder_traversal_result())

search_result = binsearchtree.query_key(7)
print("Searching for the key 7:", search_result.key if search_result else None)

'''
# Output:

# The Inorder traversal result is : [1, 2, 4, 7, 18, 21, 32, 45, 99]
# Inorder traversal after deleting key 21: [1, 2, 4, 7, 18, 21, 32, 45, 99]
# Searching for the key 7: 7 '''

