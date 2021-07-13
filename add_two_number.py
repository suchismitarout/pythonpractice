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

    def printlist(self):
        res = []
        current = self.head
        while current:
            res.append(current.get_data())
            current = current.get_next()
        return res

node = Node()
node.set_data(2)
node1 = Node()
node1.set_data(4)
node2 = Node()
node2.set_data(3)
llist = LinkedList()
llist.set_head(node)
node.set_next(node1)
node1.set_next(node2)
print(llist.printlist())

def add_two_numbers(l1, l2):
    first = [str(x) for x in l1]
    sec = [str(x) for x in l2]
    first1 = ''.join(first)
    sec1 = ''.join(sec)
    r = str(int(first1)+int(sec1))
    r_m = list(map(int, r))

    r_m.reverse()
    t = []
    for i in range(len(r_m)):
        r = Node(r_m[i])
        t.append(r)
        print(r)
    print(t)






add_two_numbers([2, 4, 3], [5, 6, 4])
