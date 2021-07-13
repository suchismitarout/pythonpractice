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


def lca_from_bst(root, first, second):
    if not root:
        return None
    if root.get_val() == first.get_val() or root.get_val() == second.get_val():
        return root.get_val()
    left = lca_from_bst(root.get_left(), first, second)
    right = lca_from_bst(root.get_right(), first, second)
    if left and right:
        return root.get_val()
    return left if left else right


root = Node(20)
node1 = Node(6)
node2 = Node(3)
node3 = Node(8)
node4 = Node(25)
node5 = Node(22)
node6 = Node(28)
root.set_left(node1)
root.set_right(node4)
node1.set_left(node2)
node1.set_right(node3)
node4.set_left(node5)
node4.set_right(node6)

print(lca_from_bst(root, node2,node3))