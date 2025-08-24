class node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None

class doubly_linked_list:
        def __init__(self):
            self.head = None

        def print_dLL(self,data):
            n = self.head
            if n is None:
                  print("empty")
            else:
                n = self.head
                while n.nref is not None:
                    n = n.nref
                    print (n.data)
        def insert_empty(self,data):
            if self.head is None:
                new_node = node(data)
                self.head = new_node
                print(new_node.data, "--->", end= " ")
            else:
                return
ragu = doubly_linked_list()
ragu.insert_empty(10)
ragu.insert_empty(20)