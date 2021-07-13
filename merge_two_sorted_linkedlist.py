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

    def merge_two_sorted_lists(self, l1, l2):
        final = dummy = Node()
        while l1 and l2:
            if l1.data <= l2.data:
                dummy.set_next(l1)
                l1 = l1.get_next()
            else:
                dummy.set_next(l2)
                l2 = l2.get_next()
            dummy = dummy.get_next()
        if l1: dummy.set_next(l1)
        if l2: dummy.set_next(l2)
        return final.next

    def merge_ksorted_lists(self, l):
        length = len(l)
        if length == 0:
            return None
        if length == 1:
            return l[0]
        if length == 2:
            return self.merge_two_sorted_lists(l[0], l[1])
        mid = length // 2
        left = self.merge_ksorted_lists(l[:mid])
        right = self.merge_ksorted_lists(l[mid:])
        return self.merge_two_sorted_lists(left, right)


llist = LinkedList()
llist.insert_node(2)
llist.insert_node(4)
llist.insert_node(5)
l1 = llist.printllist()
# print(l1)
llist1 = LinkedList()
llist1.insert_node(1)
llist1.insert_node(1)
llist1.insert_node(3)
l2 = llist1.printllist()
# print(l2)
ll4 = LinkedList()
ll4.insert_node(6)
ll4.insert_node(8)
ll4.insert_node(9)
l3 = ll4.printllist()
ll3 = LinkedList()
# ll3.head = ll3.merge_two_sorted_lists(llist.head, llist1.head)
# print(ll3.printllist())
ll5 = LinkedList()
ll5.head = ll5.merge_ksorted_lists([llist.head, llist1.head, ll4.head])
print(ll5.printllist())


