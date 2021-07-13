from mean_heap_imp import MinHeap

class Node:
    def __init__(self, val=None):
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


def insert_node(root, ele):
    node = ele
    if not root:
        return
    else:
        if root.get_val() > node.get_val():
            if root.get_left() is None:
                root.set_left(node)
            else:
                insert_node(root.get_left(), ele)
        else:
            if root.get_right() is None:
                root.set_right(node)
            else:
                insert_node(root.get_right(), ele)


def inorder(root, r):
    if not root:
        return root
    inorder(root.get_left(), r)
    r.append(root.get_val())
    inorder(root.get_right(), r)
    return r


def sorted_list_to_bst(num_list):
    if not num_list:
        return None
    mid = len(num_list) // 2
    root = Node(num_list[mid])
    root.set_left(sorted_list_to_bst(num_list[:mid]))
    root.set_right(sorted_list_to_bst(num_list[mid + 1:]))
    return root

def preorder(root):
    if not root:
        return root
    print(root.get_val(),'->', end='')
    preorder(root.get_left())
    preorder(root.get_right())

def delete_node(root, ele):
    if not root:
        return root
    if root.get_val() > ele:
        root.set_left(delete_node(root.get_left(), ele))
    elif root.get_val() < ele:
        root.set_right(delete_node(root.get_right(), ele))
    else:
        if not root.get_left():
            return root.get_right()
        if not root.get_right():
            return root.get_left()
        temp = root.get_right()
        min_v = temp.get_val()
        while temp.get_left():
            temp = temp.get_left()
            min_v = temp.get_val()
        root.set_val(min_v)
        root.set_right(delete_node(root.get_right(), min_v))
    return root

def get_smallest_element(root):
    while root.get_left():
        root = root.get_left()
    return root.get_val()

def get_largest_element(root):
    while root.get_right():
        root = root.get_right()
    return root.get_val()


def get_kth_smallest_element(root, k):
    r = inorder(root, [])
    for i in range(len(r)):
        if i == k-1:
            return r[i]



# root = Node()
# root.set_val(24)
# l = [30, 20, 15, 28, 12, 34, 22, 26]
# min_heap = MinHeap(9)
# for i in l:
#     i = Node(i)
#     insert_node(root, i)
# print(inorder(root, []))
# print("\n")
# print(get_kth_smallest_element(root, 2))

list1= [1,2,3,4,5,6,7]
r = sorted_list_to_bst(list1)
preorder(r)