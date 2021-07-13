import sys


class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [0] * (self.max_size + 1)
        self.heap[0] = sys.maxsize
        self.size = 0
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

    def max_heapify(self, pos):
        if not self.is_leaf_node(pos):
            if self.heap[pos] < self.heap[self.left_child(pos)] or self.heap[pos] < self.heap[self.right_child(pos)]:
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size += 1
        self.heap[self.size] = element
        current = self.size
        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.max_heapify(self.front)
        return popped

    def print_maxheap(self):
        for i in range(1, self.size // 2 + 1):
            print(self.heap[i], self.heap[2 * i], self.heap[(2 * i) + 1])

    def max_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.max_heapify(i)


max_h = MaxHeap(7)
r = [5, 10, 3, 4, 9, 2]
for i in r:
    max_h.insert(i)
max_h.print_maxheap()

def find_min_ele(heap, n):
    min_ele = heap[n//2]

    for i in range(n//2, n+1):
        min_ele = min(min_ele, heap[i])
    return min_ele

print(find_min_ele(max_h.heap,len(r)))