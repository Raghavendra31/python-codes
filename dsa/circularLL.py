import math as m


class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.lref = None

class cLL:
    def __init__(self):
        self.head = None

    def append(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            