class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


    def insert(self, value):
        print(self.root)
        if value < self.root:
            if self.left is None:
                self.left = BST(value)
                print(self.root)
                print(self.left)
            else:
                self.left.insert(value)
        elif value > self.root:
            if self.right is None:
                self.right = BST(value)
                print(self.root)
                print(self.right)
            else:
                self.right.insert(value)    
mroot = BST(10)
for i in [5, 15, 2, 5, 13, 22, 1, 14]:
    mroot.insert(i) 
print(mroot.root)
