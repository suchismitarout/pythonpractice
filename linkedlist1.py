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

    def insert_at_beginning(self, new_data):
        if self.head is None:
            return
        node = Node(new_data)
        node.set_next(self.head)
        self.head = node

    def insert_at_end(self, new_data):
        if self.head is None:
            return
        node = Node(new_data)
        temp = self.head
        while temp.get_next() is not None:
            temp = temp.get_next()
        temp.set_next(node)

    def insert_at_pos(self, pos, new_data):
        count = 1
        node = Node(new_data)
        cur = self.head
        prev = self.head
        while cur:
            prev = cur
            cur = cur.get_next()
            count += 1
            if count == pos:
                next = cur.get_next()
                prev.set_next(node)
                node.set_next(next)

    def delete_first_node(self):
        cur = self.head
        next = cur.get_next()
        self.head = next

    def delete_last_node(self):
        prev = self.head
        cur = self.head
        while cur.get_next() is not None:
            prev = cur
            cur = cur.get_next()
        prev.set_next(None)

    def delete_at_pos(self, pos):
        count = 1
        prev = self.head
        cur = self.head
        while cur:
            prev = cur
            cur = cur.get_next()
            count += 1
            if count == pos:
                next = cur.get_next()
                prev.set_next(next)

    def reverse_linked_list(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.get_next()
            cur.set_next(prev)
            prev = cur
            cur = next
        self.head = prev

    def find_middle_node(self):
        first_pointer = self.head
        second_pointer = self.head.get_next().get_next()
        while first_pointer and second_pointer.get_next() is not None:
            first_pointer = first_pointer.get_next()
            second_pointer = second_pointer.get_next()
        return first_pointer.get_data()

    def sort_linked_list_ascending(self):
        current = self.head
        if self.head is None:
            return
        else:
            while current != None:
                index = current.get_next()
                while index != None:
                    if current.get_data() > index.get_data():
                        temp = current.get_data()
                        current.data = index.get_data()
                        index.data = temp
                    index = index.get_next()
                current = current.get_next()

    def sort_linked_list_descending(self):
        current = self.head
        if current is None:
            return
        else:
            while current != None:
                index = current.get_next()
                while index != None:
                    if current.data < index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.get_next()
                current = current.get_next()

    def remove_duplicates(self):
        current = self.head
        if current is None:
            return


    def print_llist(self):
        temp = self.head
        res = []
        while temp is not None:

            print(temp.get_data(), '->', end='')
            temp = temp.get_next()




node1 = Node(4)
node2 = Node(1)
node3 = Node(5)
node4 = Node(3)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
llist = LinkedList(node1)
# llist.print_llist()
# print("\n")
# llist.insert_at_beginning(8)
llist.insert_at_end(6)
# llist.print_llist()
# print("\n")
llist.insert_at_pos(2, 7)
# llist.print_llist()
# print("\n")
# llist.delete_first_node()
# llist.print_llist()
# print("\n")
# llist.delete_last_node()
# llist.print_llist()
# llist.delete_at_pos(2)
# llist.print_llist()
# print("\n")
# llist.reverse_linked_list()
# llist.print_llist()
# print("\n")
# print(llist.find_middle_node())
llist.sort_linked_list_ascending()
print(llist.print_llist())
# llist.sort_linked_list_descending()
# print(llist.print_llist())
