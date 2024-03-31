# Implementation of AVL Tree

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # To get Height of the node in the tree
        self.height = 1

class AVLTreeImplementation:
     
    # Inserting a key into the AVL tree
     
     def insert_key(self, root, key):
        if not root:
            return AVLTreeNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert_key(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bal = self.get_bal(root)
        if bal > 1 and key < root.left.key:
            return self.right_rotation(root)
        if bal < -1 and key > root.right.key:
            return self.left_rotation(root)
        if bal > 1 and key > root.left.key:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        if bal < -1 and key < root.right.key:
            root.right = self.right_rotation(root.right)
            return self.rotate_left(root)
        return root

     def insert(self, node, key):
        if not node:
            return AVLTreeNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node
     
     # Deleting a key from the AVL tree

     def delete_key(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete_key(root.left, key)
        elif key > root.key:
            root.right = self.delete_key(root.right, key)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = None
                return temp
            temp = self.get_minimum_val_node(root.right)
            root.key = temp.key
            root.right = self.delete_key(root.right, temp.key)
        if not root:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        bal = self.get_bal(root)
        if bal > 1 and self.get_bal(root.left) >= 0:
            return self.right_rotation(root)
        if bal < -1 and self.get_bal(root.right) <= 0:
            return self.left_rotation(root)
        if bal > 1 and self.get_bal(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.right_rotation(root)
        if bal < -1 and self.get_bal(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.left_rotation(root)
        return root
     
    #  Searching/Querying for a key in the AVL tree
     
     def search_key(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search_key(root.left, key)
        return self.search_key(root.right, key)

    # To Get the height of a node in the AVL tree
     def get_height(self, root):
        if not root:
            return 0
        return root.height
     
    # Get the balance factor of a node in the AVL tree
     
     def get_bal(self, root):
      if not root:
        return 0
      return self.get_height(root.left) - self.get_height(root.right)
     
     # For Right rotation of a node in the AVL tree

     def right_rotation(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # For Left rotation of a node in the AVL tree
     
     def left_rotation(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # To Get the node with the minimum value in the AVL tree
     
     def get_minimum_val_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

     def inorder_traversal_root(self, root):
        result = []
        if root:
            result = self.inorder_traversal_root(root.left)
            result.append(root.key)
            result = result + self.inorder_traversal_root(root.right)
        return result

avl_tree = AVLTreeImplementation()
root = None
keys = [5, 2,45, 13, 21, 67, 99, 18, 54]

# Inserting the keys into the AVL Tree
for key in keys:
    root = avl_tree.insert_key(root, key)
    print("Key inserted is:", key)

print("The Inorder traversal is:", avl_tree.inorder_traversal_root(root))

# Testing the search operation
print("Searching for the key 21:", avl_tree.search_key(root, 21))
print("Searching for the key 18:", avl_tree.search_key(root, 18))

# Testing the delete operation
root = avl_tree.delete_key(root,54)
print("Key 54 is deleted")

# Testing the inorder traversal after deletion
print("The Inorder traversal after deletion the keys:", avl_tree.inorder_traversal_root(root))

'''
# Output:

Key inserted is: 5
Key inserted is: 2
Key inserted is: 45
Key inserted is: 13
Key inserted is: 21
Key inserted is: 67
Key inserted is: 99
Key inserted is: 18
Key inserted is: 54
The Inorder traversal is: [2, 5, 13, 18, 21, 45, 54, 67, 99]
Searching for the key 21: <__main__.AVLTreeNode object at 0x00000150BFC03950>
Searching for the key 18: <__main__.AVLTreeNode object at 0x00000150BFC039E0>
Key 54 is deleted
The Inorder traversal after deletion the keys: [2, 5, 13, 18, 21, 45, 67, 99] '''