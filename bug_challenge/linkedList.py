class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next 
        cur.next = new_node

    def display(self):
        elements = []
        cur_node = self.head.next  # Start from the first actual node
        while cur_node is not None:
            elements.append(cur_node.data)
            cur_node = cur_node.next  # Move to the next node
        print(elements)

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.display()
