class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_val(self, new_val):
        self.val = new_val

    def get_val(self):
        return self.val

    def set_left(self, new_left):
        self.left = new_left

    def get_left(self):
        return self.left

    def set_right(self, new_right):
        self.right = new_right

    def get_right(self):
        return self.right


def create_mirror_bst(root):
    if root is not None:
        create_mirror_bst(root.get_left())
        create_mirror_bst(root.get_right())
        temp = root.get_left()
        root.left = root.right
        root.right = temp
    return root


root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
root.set_left(node1)
root.set_right(node2)
node1.set_left(node3)
node1.set_right(node4)
print(create_mirror_bst(root))