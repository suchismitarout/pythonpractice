class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

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
        while temp is not None:
            print(temp.get_data(), '->', end='')
            temp = temp.get_next()

    def reverse_llist(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.head = prev

    def addition_of_nodes(self):
        temp = self.head
        sum_nodes = 0
        while temp != None:
            sum_nodes += temp.get_data()
            temp = temp.get_next()
        return sum_nodes

    def delete_first_node(self):
        current = self.head
        next = current.get_next()
        self.head = next

    def delete_last_node(self):
        current = self.head
        prev = None
        while current.get_next() != None:
            prev = current
            current = current.get_next()
        prev.set_next(None)

    def delete_at_pos(self, n):
        count = 1
        current = self.head
        prev = None
        if n == count:
            current = self.head
            next = current.get_next()
            self.head = next
        while current.get_next() != None:
            prev = current
            current = current.get_next()
            count +=1
            if count == n:
                next = current.get_next()
                prev.set_next(next)

    def insertion_sort(self):
        current = self.head
        while current:
            prev =current
            current = current.get_next()











node = Node()
node.set_data(12)
node1 = Node()
node1.set_data(4)
node2 = Node()
node2.set_data(13)
node3 = Node()
node3.set_data(9)
node4 = Node()
node4.set_data(11)
node.set_next(node1)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
llist = LinkedList()
llist.set_head(node)
llist.printList()
print("\n")
llist.reverse_llist()
llist.printList()
print("\n")
# print(llist.addition_of_nodes())
# print("\n")
# llist.delete_first_node()
# print(llist.printList())
# llist.delete_last_node()
# llist.printList()
llist.delete_at_pos(2)
print(llist.printList())