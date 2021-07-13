import sys


class MinHeap2:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [0] * (self.max_size + 1)
        self.heap[0] = -1 * sys.maxsize
        self.size = 0
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def is_leaf_node(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        return False

    def minheapify(self, pos):
        if not self.is_leaf_node(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.minheapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.minheapify(self.right_child(pos))

    def insert(self, ele):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = ele
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.minheapify(self.front)
        return popped

    def print(self):
        for i in range(1, self.size + 1):
            print(self.heap[i], '->', end='')

    def min_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.minheapify(i)


min_h = MinHeap2(7)
l = [23, 14, 36, 2, 7, 26, 19]

for i in l:
    min_h.insert(i)
min_h.min_heap()
min_h.print()
print("-----------")
c=0
for i in range(1,3):
    c=min_h.remove()
print(c)


