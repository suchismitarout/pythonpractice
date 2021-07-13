class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, new):
        self.data = new

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right


def insert_node(root,new):
    if not root:
        return
    if new.get_data() < root.get_data():
        if root.get_left() is None:
            root.set_left(new)
        else:
            insert_node(root.get_left(), new)
    else:
        if root.get_right() is None:
            root.set_right(new)
        else:
            insert_node(root.get_right(), new)


def inorder(root):
    if not root:
        return
    inorder(root.get_left())
    print(root.get_data(),'->', end='')
    inorder(root.get_right())


root = Node()
root.set_data(12)
node1 = Node()
node1.set_data(5)
node2 = Node()
node2.set_data(10)
node3 = Node()
node3.set_data(23)
node4 = Node()
node4.set_data(7)
node5 = Node()
node5.set_data(8)
l = [node1,node2,node3,node4]
for i in l:
    insert_node(root,i)
inorder(root)


