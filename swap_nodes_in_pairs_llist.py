class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def set_head(self, new_head):
        self.head = new_head

    def get_head(self):
        return self.head

    def insert_node(self, node):
        node = Node(node)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(node)

    def printllist(self):
        current = self.head
        l = []
        while current:
            l.append(current.get_data())
            current = current.get_next()
        return l

    def swap_nodes_in_pairs(self):
        current = self.head
        if not current or not current.get_next():
            return current
        while current.get_next():
            next = current.get_next()
            current.data, next.data = next.data, current.data
            if not next.get_next() or not next.get_next().get_next():
                return current
            current = next.get_next()
        return current






llist = LinkedList()
x = [1,2,3,4]
for i in x:
    llist.insert_node(i)
print(llist.printllist())
llist.swap_nodes_in_pairs()
print(llist.printllist())

