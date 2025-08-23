class Node:
    def __init__(self, data):
        self.data = data   # store data
        self.next = None   # initially no next node
class LinkedList:
    def __init__(self):
        self.head = None   # start with an empty list

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Create linked list
ll = LinkedList()

# Add elements
ll.append(10)
ll.append(20)
ll.append(30)

# Display list
ll.display()
