class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None

class sLL:
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

    def prin(self):
        temp = self.head
        while temp:
            print(temp.data, end= "->")
            temp = temp.nref
        print("None")  



r = sLL()

r.insert(1)
r.insert(2)
r.insert(3)

r.prin()