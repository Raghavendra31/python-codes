class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = node(value)

        if self.root is None:
            self.root = new_node
            return
        temp = self.root

        while True:
            if new_node.data == temp.data:
                print("node already exists")
                return
            elif new_node.data < temp.data :
                temp.left = new_node
                
                return
            
            elif new_node.data > temp.data:
                temp.right = new_node
                return
            
            