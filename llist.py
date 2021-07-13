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
        current = self.head
        if current is None:
            return new_data
        new_data.set_next(current)
        self.head = new_data

    def insert_at_end(self, new_data):
        current = self.head
        if current is None:
            return new_data
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_data)

    def insert_at_pos(self, pos, new_data):
        count = 1
        current = self.head
        while current:
            prev = current
            current = current.get_next()
            count += 1
            if count == pos:
                next = current.get_next()
                prev.set_next(new_data)
                new_data.set_next(next)

    def delete_first_node(self):
        current = self.head
        if current is None:
            return
        next = current.get_next()
        self.head = next

    def delete_last_node(self):
        current = self.head
        prev = self.head
        if current is None:
            return
        while current.get_next():
            prev = current
            current = current.get_next()
        prev.set_next(None)

    def delete_from_pos(self, pos):
        current = self.head
        count = 1
        if current is None:
            return
        while current:
            prev = current
            current = current.get_next()
            count += 1
            if count == pos:
                next = current.get_next()
                prev.set_next(next)
                current = prev

    def find_middle_node(self):
        current = self.head
        if current is None:
            return
        first_pointer = current
        second_pointer = current.get_next().get_next()
        while first_pointer and second_pointer.get_next():
            first_pointer = first_pointer.get_next()
            second_pointer = second_pointer.get_next()
        return first_pointer.get_data()

    def reverse_llist(self):
        current = self.head
        prev = None
        if current is None:
            return
        while current:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.head = prev

    def sort_in_ascending(self):
        current = self.head
        if current is None:
            return
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next

    def sort_in_descending(self):
        current = self.head
        if current is None:
            return
        while current:
            index = current.next
            while index:
                if current.data < index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next

    def remove_duplicates(self):
        current = self.head
        if current is None:
            return
        while current:
            index = current.next
            while index:
                if current.data == index.data:
                    next = index.next
                    current.set_next(next)
                index = index.next
            current = current.next

    def remove_all_nodes_having_duplicates(self):
        current = self.head
        if current is None:
            return
        while current:
            temp = current.next
            while temp:
                if current.data == temp.data:
                    current, temp = temp, current
                    if current.data == current.next.data:
                        current, current.next = current.next, current
                temp = temp.next
            current = current.next

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.get_data(), '->', end='')
            current = current.get_next()


node = Node()
node.set_data(12)
node1 = Node()
node1.set_data(10)
node2 = Node()
node2.set_data(9)
node3 = Node()
node3.set_data(13)
node4 = Node()
node4.set_data(17)
node5 = Node()
node5.set_data(10)
node.set_next(node1)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
llist = LinkedList()
llist.set_head(node)
llist.printlist()
print("\n")
llist.insert_at_beginning(node5)
# llist.printlist()
# llist.insert_at_end(node1)
# llist.printlist()
# llist.insert_at_pos(3, node5)
# llist.printlist()
# llist.delete_first_node()
# llist.printlist()
# llist.delete_last_node()
# llist.printlist()
# llist.delete_from_pos(2)
# llist.printlist()
# print(llist.find_middle_node())
# llist.reverse_llist()
# llist.printlist()
llist.sort_in_ascending()
# llist.printlist()
# print("\n")
# llist.sort_in_descending()
# llist.printlist()
# llist.remove_duplicates()
# llist.printlist()
llist.remove_all_nodes_having_duplicates()
llist.printlist()
