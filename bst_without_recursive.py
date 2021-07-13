class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data_):
        self.data = data_

    def get_data(self):
        return self.data

    def set_left(self, left_):
        self.left = left_

    def set_right(self, right_):
        self.right = right_

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


def inorder(root):
    current = root
    st = []
    while True:
        if current is not None:
            st.append(current)
            current = current.get_left()
        elif st:
            current = st.pop()
            print(current.get_data(), '->', end='')
            current = current.get_right()
        else:
            break

def preorder(root):
    current = root
    st = []
    l = []
    l.append(current)
    while True:
        if current is not None:
            current = current.get_left()
            st.append(current)
        elif st:
            current = st.pop()
            print(current.get_data(), '->', end='')
            current = current.get_right()
            st.append(l.pop())
        else:
            break



node = Node()
node.set_data(10)
node1 = Node()
node1.set_data(5)
node2 = Node()
node2.set_data(3)
node3 = Node()
node3.set_data(6)
node4 = Node()
node4.set_data(15)
node5 = Node()
node5.set_data(12)
node6 = Node()
node6.set_data(17)
node.set_left(node1)
node1.set_left(node2)
node1.set_right(node3)
node.set_right(node4)
node4.set_left(node5)
node4.set_right(node6)
inorder(node)
print("\n")
preorder(node)