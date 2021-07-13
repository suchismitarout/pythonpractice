class Node():
    def __init__(self, data):
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

    def insert_at_beginning(self, data):
        temp = self.head
        data.set_next(temp)
        self.head = data

    def insert_at_end(self, data):
        temp = self.head
        while temp.get_next() != None:
            temp = temp.get_next()
        temp.set_next(data)

    def insert_at_pos(self, pos, data):
        count = 1
        temp = self.head
        while temp.get_next() != None:
            prev = temp
            temp = temp.get_next()
            count += 1
            if pos == count:
                next = temp.get_next()
                data.set_next(next)
                prev.set_next(data)

    def delete_first_node(self):
        temp = self.head
        next = temp.get_next()
        self.head = next

    def delete_last_node(self):
        temp = self.head
        prev = temp
        while temp.get_next() != None:
            prev = temp
            temp = temp.get_next()
        prev.set_next(None)

    def delete_at_pos(self, pos):
        temp = self.head
        count = 1
        while temp.get_next() != None:
            prev = temp
            temp = temp.get_next()
            count += 1
            if pos == count:
                next = temp.get_next()
                prev.set_next(next)

    def reverse_linkedlist(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.get_next()
            cur.set_next(prev)
            prev = cur
            cur = next
        self.head = prev

    def find_mid_node(self):
        temp = self.head
        slow_pointer = temp
        fast_pointer = temp
        if temp != None:
            while fast_pointer is not None and fast_pointer.get_next() is not None:
                fast_pointer = fast_pointer.get_next().get_next()
                slow_pointer = slow_pointer.get_next()

            print(slow_pointer.get_data())


    def printList(self):
        temp = self.head
        while temp:
            print(temp.get_data(), '->', end=' ')
            temp = temp.get_next()

node = Node(12)
node1 = Node(6)
node2 = Node(24)
node3 = Node(18)
node4 = Node(10)
node5 = Node(15)
node6 = Node(24)
node.set_next(node1)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
node4.set_next(node5)
llist = LinkedList()
llist.set_head(node)
llist.printList()
print("\n")
# llist.insert_at_beginning(node4)
# llist.printList()
# print("\n")
# llist.insert_at_end(node4)
# llist.printList()
# print('\n')
# llist.insert_at_pos(3, node5)
# llist.printList()
# llist.delete_first_node()
# llist.printList()
# llist.delete_last_node()
# llist.printList()

# llist.delete_at_pos(3)
# llist.printList()
llist.reverse_linkedlist()
llist.printList()
print("\n")
llist.find_mid_node()