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

    def get_left(self):
        return self.left

    def set_right(self, right_):
        self.right = right_

    def get_right(self):
        return self.right


def insert_node(root, node):
    if root is None:
        return
    while True:
        if root.get_left() is None:
            root.set_left(node)
            break
        else:
            if root.get_right() is None:
                root.set_right(node)
                break


def inorder(root):
    if root:
        inorder(root.get_left())
        print(root.get_data(), '->', end=' ')
        inorder(root.get_right())


root = Node()
root.set_data(12)
node = Node()
node.set_data(25)
n1 = Node()
n1.set_data(15)
insert_node(root, node)
inorder(root)
