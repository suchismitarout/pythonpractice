class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, new_left):
        self.left = new_left

    def get_left(self):
        return self.left

    def set_right(self, new_right):
        self.right = new_right

    def get_right(self):
        return self.right


def insert_node(root, node):
    if root is None:
        return
    else:
        if node.get_data() < root.get_data():
            if root.get_left() is None:
                root.set_left(node)
            else:
                insert_node(root.get_left(), node)
        else:
            if root.get_right() is None:
                root.set_right(node)
            else:
                insert_node(root.get_right(), node)


def inorder_travseral(root):
    if root:
        inorder_travseral(root.get_left())
        print(root.get_data(), '->', end='')
        inorder_travseral(root.get_right())


def preorder_traversal(root):
    if root:
        print(root.get_data(), '->', end='')
        preorder_traversal(root.get_left())
        preorder_traversal(root.get_right())


def post_traversal(root):
    if root:
        preorder_traversal(root.get_left())
        preorder_traversal(root.get_right())
        print(root.get_data(), '->', end='')


def zigzag_traversal(root):
    if not root:
        return

    next = []
    current = []
    result = []
    current.append(root)
    ltr = True
    while len(current) > 0:
        temp = current.pop(-1)
        result.append(temp.get_data())
        if ltr:
            if temp.get_left():
                next.append(temp.get_left())
            if temp.get_right():
                next.append(temp.get_right())
        else:
            if temp.get_right():
                next.append(temp.get_right())
            if temp.get_left():
                next.append(temp.get_left())
        if len(current) == 0:
            ltr = not ltr
            current, next = next, current
    return result



root = Node()
root.set_data(23)
node1 = Node()
node1.set_data(12)
node2 = Node()
node2.set_data(25)
insert_node(root, node1)
insert_node(root, node2)
inorder_travseral(root)
print("\n")
preorder_traversal(root)
print("\n")
post_traversal(root)
print("\n")
print(zigzag_traversal(root))