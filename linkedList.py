class Linkedlist:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = None

class LL_node:
    def __init__(self,head = None,tail = None):
        self.head = None


    def print_node(self):
        if self.head is None:
            print("head is empty")
        else:
            n = self.head
            while self is not None:
                print (n.data)
                n = n.ref

    def add(self,data):
        new_node = LL_node()
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.tail is None:
                n = n.tail
            n.tail = new_node


ragu = LL_node()
ragu.add(1)
ragu.add(2)


