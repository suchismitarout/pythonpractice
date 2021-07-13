import sys


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0] * (self.max_size + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return (2 * pos) + 1

    def is_leaf_node(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        return False

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def mean_heapify(self, pos):
        if not self.is_leaf_node(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.mean_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.mean_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped_ele = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.mean_heapify(self.front)
        return popped_ele

    def print_minheap(self):
        for i in range(1, self.size // 2 + 1):
            print(self.heap[i], self.heap[2 * i], self.heap[(2 * i) + 1])

    def mean_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.mean_heapify(i)


m_heap = MinHeap(9)
# print(m_heap.size)
r = [7, 9, 8, 2, 4, 5, 1, 3]
for i in r:
    m_heap.insert(i)
m_heap.print_minheap()
# print(m_heap.heap)
# print(m_heap.size)
# m_heap.mean_heap()
# m_heap.print_minheap()
# print(m_heap.heap)
n = len(r)


def find_max_ele(heap, n):
    max_ele = heap[n//2]
    for i in range(1+n//2, n+1):
        max_ele = max(max_ele, heap[i])
    return max_ele


print(find_max_ele(m_heap.heap, n))
