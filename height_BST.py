class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Height_bst:
    def __init__(self):
        self.root = None

    def createBST(self,data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node

        temp = self.root

        while True:
            
            if data < temp.root:
                if temp.left is None:
                    temp.left = new_node

                
