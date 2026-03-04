class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

class Dll:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.nref:
            temp = temp.nref
        temp.nref = new_node
        new_node.pref = temp

        return
    
    def printing(self):
        temp = self.head

        while temp:
            
            print(temp.data,"---->",end = " ")
            if temp.nref is None:
                print("None")
            temp = temp.nref
            
        return
        

r = Dll()

r.insert(1)
r.insert(2)
r.insert(3)
r.insert(4)

r.printing()