# First, we define the building block: the Node
class Node:
   
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None    # A pointer to the left child node
        self.right = None   # A pointer to the right child node

    def __str__(self):
        # This helps in printing the node's value for debugging
        return f"Node({self.value})"
    
class BinarySearchTree:
    """
    A class that represents the entire Binary Search Tree.
    """
    def __init__(self):
        # The root is the top-most node of the tree. It starts as None for an empty tree.
        self.root = None

    # --- INSERTION ---
    def insert(self, value):
        """
        Public method to insert a new value into the tree.
        """
        new_node = Node(value)
        # If the tree is empty, the new node becomes the root
        if self.root is None:
            self.root = new_node
            return True

        # Otherwise, find the correct spot for the new node
        temp = self.root
        while True:
            # If the new value is the same as the current node's value, do nothing
            # (no duplicates allowed)
            if new_node.value == temp.value:
                return False

            # If the new value is less than the current node's value, go left
            if new_node.value < temp.value:
                # If there is no left child, insert the new node here
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Otherwise, move to the left child and continue
                temp = temp.left
            # If the new value is greater than the current node's value, go right
            else: # new_node.value > temp.value
                # If there is no right child, insert the new node here
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Otherwise, move to the right child and continue
                temp = temp.right

    # --- SEARCHING ---
    def contains(self, value):
        """
        Public method to check if a value exists in the tree.
        """
        if self.root is None:
            return False

        temp = self.root
        # Traverse the tree until we find the value or hit a dead end (None)
        while temp is not None:
            # If the value is less than the current node's value, go left
            if value < temp.value:
                temp = temp.left
            # If the value is greater than the current node's value, go right
            elif value > temp.value:
                temp = temp.right
            # If the value is found, return True
            else: # value == temp.value
                return True
        
        # If the loop finishes, the value was not found
        return False


# Create a new Binary Search Tree
my_bst = BinarySearchTree()

# Insert some values
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)

# After these insertions, our tree looks like this:
#
#       (47)
#      /    \
#    (21)   (76)
#   /   \   /   \
# (18) (27)(52) (82)
#

# Let's test our 'contains' method
print("Does the tree contain 27?", my_bst.contains(27)) # Expected: True
print("Does the tree contain 18?", my_bst.contains(18)) # Expected: True
print("Does the tree contain 99?", my_bst.contains(99)) # Expected: False