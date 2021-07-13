class TreeNode:
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


def bst_from_pre_in_rec(preorder, inorder, preindex, inindex, length):
    if length == 0:
        return None

    root = TreeNode(preorder[preindex])
    count = 0
    for i in range(inindex, inindex + length):
        if inorder[i] == preorder[preindex]:
            break
        count += 1
    root.set_left(bst_from_pre_in_rec(preorder, inorder, preindex + 1, inindex, count))
    root.set_right(
        bst_from_pre_in_rec(preorder, inorder, preindex + count + 1, inindex + count + 1, length - 1 - count))
    return root


def bst_from_pre_in(preorder, inorder):
    return bst_from_pre_in_rec(preorder, inorder, 0, 0, len(preorder))


print(bst_from_pre_in(['A', 'B', 'D', 'E', 'C', 'F'], ['D', 'B', 'E', 'A', 'F', 'C']))
