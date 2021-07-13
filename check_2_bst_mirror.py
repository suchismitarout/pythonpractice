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

def check_is_mirror(root1,root2):
    if root1 == None and root2 == None:
        return 1
    if root1 == None or root2 == None:
        return 0
    if root1.get_val() != root2.get_val():
        return 0
    else:
        return check_is_mirror(root1.get_left(), root2.get_right()) and check_is_mirror(root1.get_right(), root2.get_left())




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

root1 = Node(30)
node1 = Node(7)
node2 = Node(4)
node3 = Node(9)
node4 = Node(26)
node5 = Node(23)
node6 = Node(29)
root1.set_left(node1)
root1.set_right(node4)
node1.set_left(node2)
node1.set_right(node3)
node4.set_left(node5)
node4.set_right(node6)
print(check_is_mirror(root, root1))