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
        def insert_node(self,data):
             n = self.head
             while n.nref is not None:
                 n = n.nref
             new_node = node(data)
             n.nref = new_node
             new_node.pref = n
             print(f"{new_node.data}", end=" ---> ")
                  

ragu = doubly_linked_list()
ragu.insert_empty(10)
ragu.insert_node(22)
ragu.insert_node(24)
ragu.insert_node(25)
ragu.insert_node(26)

