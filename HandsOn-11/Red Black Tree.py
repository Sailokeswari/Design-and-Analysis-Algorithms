# Implementation of Red Black Tree

class TreeNode:
    def __init__(self, key, color="RED"):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RedBlackTreeImplementation:
    def __init__(self):
        self.NIL = Node(None)
        self.root = self.NIL

    def insert_key(self, key):
        new_node = Node(key)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "RED"
        parent = None
        cur = self.root
        while cur != self.NIL:
            parent = cur
            if new_node.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self.insert_fixup(new_node)

    def insert_node(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        if node is not None:
            node.color = "BLACK"



    def delete_key(self, key):
        node = self.search(key)
        if node is not None:
            self.delete_node(node)

    def delete_node_1(self, node):
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = self.NIL
            else:
                node.parent.right = self.NIL
        else:
            self.root = self.NIL

    def delete_node_2(self, node):
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
            if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
            else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color

    def rotation_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotation_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search_key(self, key):
        cur = self.root
        while cur != self.NIL and key != cur.key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return cur if cur != self.NIL else None

    def inorder_traversal_implementation(self, node, result):
        if node != self.NIL:
            self.inorder_traversal_implementation(node.left, result)
            result.append(node.key)
            self.inorder_traversal_implementation(node.right, result)

    def get_inorder_traversal(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

# Insertion Operation
rb_tree = RedBlackTreeImplementation()
keys = [5, 9, 2, 55, 99, 12, 45, 53, 90, 1, 3]
for key in keys:
    rb_tree.insert(key)

print("The Inorder traversal of the Red-Black Tree:")
result = []
rb_tree.inorder_traversal(rb_tree.root, result)
print(result)
print()

# search/query operation
search_key = 4
result = rb_tree.search(search_key)
if result != rb_tree.NIL:
    print(f"The Key searching for is  {search_key} found")
else:
    print(f"The Key searching is  {search_key} not found")

# deletion operation
delete_key = 12
print(f"\n The deleted key is {delete_key} from the tree")
rb_tree.delete(delete_key)

print("The Inorder traversal after deletion of the key:")
result = []
rb_tree.inorder_traversal(rb_tree.root, result)
print(result)
print()

'''
# Output:
Inorder traversal of the Red-Black Tree:
[1, 2, 3, 5, 9, 12, 45, 53, 55, 90, 99]

The Key searching for is  4 found

 The deleted key is 12 from the tree
 
 The Inorder traversal after deletion of the key:
 [1, 2, 3, 5, 9, 45, 53, 55, 90, 99] '''