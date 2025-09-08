class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, items=None):
        self.head = None
        if items:
            for item in items:
                self.append(item)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next

        print(" -> ".join(nodes))
