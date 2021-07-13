class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, data_):
        self.data = data_

    def get_data(self):
        return self.data

    def set_next(self, next_):
        self.next = next_

    def get_next(self):
        return self.next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def set_head(self, head_):
        self.head = head_

    def get_head(self):
        return self.head

    def printList(self):
        temp = self.head
        l = []
        while temp:
            l.append(temp.get_data())
            temp = temp.get_next()
        print(*l, sep='->')

    def swap_kth_node(self, pos):
        res = []
        temp = self.head
        prev = None
        while temp:
            res.append(temp)
            temp = temp.get_next()
        res[pos-1], res[-pos] = res[-pos], res[pos-1]
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        res[-1].next = prev




node = Node()
node.set_data(12)
node1 = Node()
node1.set_data(9)
node2 = Node()
node2.set_data(10)
node3 = Node()
node3.set_data(7)
node4 = Node()
node4.set_data(11)
node.set_next(node1)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
llist = LinkedList()
llist.set_head(node)
llist.printList()
llist.swap_kth_node(2)
print("\n")
llist.printList()