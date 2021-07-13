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


class Linkedlist:
    def __init__(self, head=Node):
        self.head = head

    def set_head(self, new_head):
        self.head = new_head

    def get_head(self):
        return self.head

    def printlist(self):
        current = self.head
        while current:
            print(current.get_data(), '->', end='')
            current = current.get_next()

    def reverse_llist(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = next
        self.head = prev


    def remove_nth_from_llist(self, pos):
        current = self.head
        prev = self.head
        counter = 1
        while current.get_next():
            prev = current
            current = current.get_next()
            counter += 1
            if counter == pos:
                next = current.get_next()
                prev.set_next(next)

    def remove_nth_from_last(self, pos):
        stk = []
        current = self.head
        temp = self.head
        if current.get_next() is None and pos == 1:
            current = current.get_next()
        while current:
            stk.append(current)
            current = current.get_next()
        for i in range(pos):
            l = stk.pop()
        if len(stk) == 0:
            current = temp.get_next()
        current = stk.pop()
        n = l.get_next()
        current.set_next(n)


node = Node()
node.set_data(1)
# node1 = Node()
# node1.set_data(2)
# node2 = Node()
# node2.set_data(3)
# node3 = Node()
# node3.set_data(4)
# node4 = Node()
# node4.set_data(5)
# node.set_next(node1)
# node1.set_next(node2)
# node2.set_next(node3)
# node3.set_next(node4)
llist = Linkedlist()
llist.set_head(node)
llist.printlist()
print("\n")
# llist.reverse_llist()
# llist.printlist()
# print("\n")
llist.remove_nth_from_last(1)
llist.printlist()