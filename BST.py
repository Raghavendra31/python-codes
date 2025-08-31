class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.root:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value > self.root:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)    
mroot = BST(10)
for i in [5, 15, 2, 5, 13, 22, 1, 14]:
    mroot.insert(i) 
print(mroot.root)