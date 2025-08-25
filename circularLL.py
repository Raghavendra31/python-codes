class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_to_empty(self, data):
        if self.head is not None:
            return self.head
        new_node = Node(data)
        self.head = new_node
        self.head.next = self.head  # circular link
        return self.head

    def add_end(self, data):
        if self.head is None:
            return self.add_to_empty(data)

        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")
cll = CircularLinkedList()
cll.add_to_empty(10)
cll.add_end(20)
cll.add_end(30)
cll.add_end(40)

cll.print_list()
