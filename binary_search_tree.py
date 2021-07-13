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


def inorder_traverse(root):
    if root:
        inorder_traverse(root.get_left())
        print(root.get_data(), '->', end=' ')
        inorder_traverse(root.get_right())

def zigzag_traverse(root):
    if root is None:
        return
    cur = []
    next = []
    res = []
    ltr = True
    cur.append(root)
    while len(cur) > 0:
        temp = cur.pop(-1)
        res.append(temp.get_data())
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
        if len(cur) == 0:
            cur, next = next, cur
            ltr = not ltr

    print(res)




root = Node()
root.set_data(12)
node = Node()
node.set_data(7)
node1 = Node()
node1.set_data(23)
node2 =Node()
node2.set_data(5)
node3 = Node()
node3.set_data(8)
node4 = Node()
node4.set_data(15)
node5 = Node()
node5.set_data(24)
l = [node, node1, node2, node3, node4, node5]
for i in l:
    insert_node(root, i)
inorder_traverse(root)
print('\n')
zigzag_traverse(root)




