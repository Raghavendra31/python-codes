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
                return False
            
            elif new_node.data < temp.data :
                if temp.left is None:

                    temp.left = new_node
                    return True 
                temp = temp.left
            
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    

    def checkNode(self,value):

        if self.root is None:
            return False
        
        temp = self.root

        while temp is not None :
            if value <temp.data:
                temp = temp.left
                
            
            elif value > temp.data:
                temp = temp.right
                
            
            else:
                return True

        return False




r = bst()

r.insert(26)
r.insert(65)
r.insert(15)
r.insert(75)
r.insert(46)


print(r.checkNode(2))
print(r.checkNode(43))
print(r.checkNode(23))
print(r.checkNode(26))
print(r.checkNode(15))